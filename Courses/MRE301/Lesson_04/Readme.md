# Lesson 4 Embed Documents, Store Vectors, and Retrieve Smarter with LangChain

Imagine a huge library where nobody has labelled the shelves. You could still find a book, but only by reading every spine, one by one. Now imagine a librarian who has read every book and placed it on a giant map, so that books with similar meaning sit close together. When you ask a question, the librarian walks straight to the right corner of the map. That map is made of **embeddings**, and the building that stores it is a **vector database**. In this lesson you will learn how to turn your document chunks into embeddings using IBM watsonx's embedding model, how to store them in vector databases such as **Chroma DB** and **FAISS**, and how to prepare your documents with LangChain before embedding them. Then you will meet four smarter ways of searching, called **retrievers**: the Vector Store-Based, Multi-Query, Self-Query, and Parent Document retrievers. Finally, you will compare RAG with fine-tuning through **InstructLab**, so you can decide which approach fits your own project best.

## What You Will Learn

- Explain what **embeddings** are and what role they play in a RAG pipeline.
- Embed documents with the **watsonx embedding model** through LangChain.
- Prepare, clean, and enrich documents with LangChain before embedding them.
- Create, configure, save, load, and update **Chroma DB** and **FAISS** vector stores.
- Use and compare the **Vector Store-Based**, **Multi-Query**, **Self-Query**, and **Parent Document** retrievers.
- Compare **RAG** with **fine-tuning using InstructLab**, and choose the right one for a given problem.

## Map of This Lesson

- 🧰 **Setup first:** Setup and Installation (run this block before everything else)
- 🗺️ **Foundations:** What Are Embeddings, The Role of Embeddings in RAG
- 🧪 **Preparation:** Embedding Documents with watsonx, Preprocessing Documents with LangChain
- 🗄️ **Vector Stores:** How Vector Stores Compare Vectors, Chroma DB, FAISS
- 🔎 **Retrievers:** Vector Store-Based, Multi-Query, Self-Query, Parent Document, Choosing a Retriever
- ⚖️ **RAG or Fine-Tuning:** How InstructLab Works, Choosing Between RAG and Fine-Tuning
- 🏋️ **Practice:** Troubleshooting, Summary, Exercises, Solutions

## Setup and Installation

### 📖 The Story

Before Chef Lina opens the restaurant, she checks the stove, the knives, and the fridge. We do the same: we install the libraries, prepare a few sample documents, and create two helper functions that give us an **embedding model** and a **language model**. A single switch decides whether they are the offline toy versions or the real watsonx ones.

### 💡 The Explanation

You will use:

- `langchain`, `langchain-community`: the framework, plus the Chroma and FAISS connectors.
- `chromadb` and `faiss-cpu`: the two vector databases of this lesson.
- `lark`: needed by the Self-Query retriever.
- `langchain-ibm` and `ibm-watsonx-ai`: the watsonx connectors (only needed if `USE_WATSONX = True`).

The versions match Lesson 2 (`langchain 0.2.7`). Everything in this lesson was tested with those versions plus `langchain-ibm 0.1.12`, `chromadb 1.5.9`, and `faiss-cpu 1.16.0`. In newer LangChain releases some classes moved (for example Chroma is also available as `langchain_chroma.Chroma`), so keep versions consistent when you follow along.

**Using real watsonx models.** Set `USE_WATSONX = True`, then provide:

- an IBM Cloud **API key** in the environment variable `WATSONX_APIKEY`,
- your watsonx **project ID**, and the **URL** of your region (for example `https://us-south.ml.cloud.ibm.com`).

Model names are retired from time to time, so check the current list of embedding and foundation models in the watsonx.ai documentation and update `WATSONX_EMBED_ID` and `WATSONX_LLM_ID` if needed. Many later blocks use `docs`, `companypolicies`, `get_embeddings()`, and `get_llm()` from this block, so **run it first**.

### 💻 The Code

```python
%%capture
!pip install "langchain==0.2.7" "langchain-core==0.2.20" "langchain-text-splitters==0.2.2" "langchain-community==0.2.7"
!pip install chromadb faiss-cpu lark numpy
!pip install "langchain-ibm<0.2" ibm-watsonx-ai        # only needed for the watsonx switch

import math, os, re, zlib
from typing import List
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_community.llms.fake import FakeListLLM

# ---------- The switch ----------
USE_WATSONX = False                                    # True = real watsonx models
WATSONX_URL = "https://us-south.ml.cloud.ibm.com"      # your region
WATSONX_PROJECT_ID = "PASTE-YOUR-PROJECT-ID"           # from your watsonx project
WATSONX_EMBED_ID = "ibm/slate-125m-english-rtrvr-v2"   # embedding model (check the docs for current names)
WATSONX_LLM_ID = "ibm/granite-3-8b-instruct"           # text model (check the docs for current names)
# The API key is read from the environment variable WATSONX_APIKEY.

# ---------- A tiny offline embedding model (counts shared words) ----------
STOPWORDS = {"the", "a", "an", "of", "to", "for", "in", "on", "at", "by", "is", "are", "be", "do",
             "does", "how", "what", "many", "much", "i", "my", "can", "may", "must", "and", "or",
             "per", "up", "with", "within"}

class ToyEmbeddings(Embeddings):
    """Hashes the first 5 letters of each word into a 256-number vector."""
    def __init__(self, dim: int = 256):
        self.dim = dim

    def _embed(self, text: str) -> List[float]:
        vec = [0.0] * self.dim
        for word in re.findall(r"[a-z0-9']+", text.lower()):
            if word in STOPWORDS:
                continue
            vec[zlib.crc32(word[:5].encode()) % self.dim] += 1.0
        norm = math.sqrt(sum(v * v for v in vec)) or 1.0
        return [v / norm for v in vec]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self._embed(t) for t in texts]

    def embed_query(self, text: str) -> List[float]:
        return self._embed(text)

# ---------- Helper functions: one switch, two worlds ----------
def get_embeddings():
    if USE_WATSONX:
        from langchain_ibm import WatsonxEmbeddings
        from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames as EmbedParams
        return WatsonxEmbeddings(
            model_id=WATSONX_EMBED_ID,
            url=WATSONX_URL,
            project_id=WATSONX_PROJECT_ID,
            params={EmbedParams.TRUNCATE_INPUT_TOKENS: 512},
        )
    return ToyEmbeddings()

def get_llm(scripted_replies=None):
    """Real watsonx LLM, or a stand-in that returns the replies you script for it."""
    if USE_WATSONX:
        from langchain_ibm import WatsonxLLM
        return WatsonxLLM(
            model_id=WATSONX_LLM_ID,
            url=WATSONX_URL,
            project_id=WATSONX_PROJECT_ID,
            params={"max_new_tokens": 300},
        )
    return FakeListLLM(responses=scripted_replies or ["(no scripted reply)"])

# ---------- Sample documents with metadata ----------
def make(text, department, year):
    return Document(page_content=text,
                    metadata={"source": "handbook", "department": department, "year": year})

docs = [
    make("Full-time employees receive 20 days of paid annual leave per year.", "HR", 2023),
    make("Sick leave is granted for up to 10 days per year and may require a doctor's note.", "HR", 2024),
    make("Parental leave is available to all employees after six months of service.", "HR", 2022),
    make("Employees may work remotely up to three days per week with manager approval.", "HR", 2024),
    make("Passwords must be at least 12 characters long and changed every 90 days.", "IT", 2024),
    make("Lost or stolen devices must be reported to the IT team within 24 hours.", "IT", 2023),
    make("Confidential data must never be shared through personal email accounts.", "IT", 2022),
    make("Travel expenses must be submitted within 30 days with receipts attached.", "Finance", 2024),
    make("Employees may claim up to 50 dollars per day for meals during business travel.", "Finance", 2023),
]

# ---------- A longer document (same handbook as Lesson 2) ----------
companypolicies = """Company Policies Handbook

1. Code of Conduct
All employees must act with honesty and respect. Harassment of any kind is not tolerated.
Employees should report any violation to the Human Resources department immediately.

2. Remote Work Policy
Employees may work remotely up to three days per week with manager approval.
Remote workers must be available during core hours, from 10 AM to 3 PM.
Company equipment must be kept secure at all times.

3. Leave Policy
Full-time employees receive 20 days of paid annual leave per year.
Sick leave is granted for up to 10 days per year and may require a doctor's note.
Parental leave is available to all employees after six months of service.

4. Information Security
Passwords must be at least 12 characters long and changed every 90 days.
Confidential data must never be shared through personal email accounts.
Lost or stolen devices must be reported to the IT team within 24 hours.
"""

print("Documents ready:", len(docs), "| long document:", len(companypolicies), "characters")
# Output: Documents ready: 9 | long document: 927 characters
```

## What Are Embeddings

### 📖 The Story

Mia the map-maker was asked to draw a **treasure map of words**. She decided that words with similar meanings should live close together. *Puppy* went next to *dog*. *Dog* went near *cat*. *Rocket* went far away on the other side of the map, near *planet*.

To describe where each word lives, Mia gave it **coordinates**, just like a street address. A tiny map needs only two numbers (left-right, up-down). Mia's real map was huge, so every word needed **hundreds of numbers**. Now, to find words that mean the same thing, Mia did not need to read anything. She just measured **how close the addresses were**.

### 💡 The Explanation

An **embedding** is a list of numbers (a **vector**) that represents the **meaning** of a piece of text. An **embedding model** is the map-maker that produces those numbers.

- Texts with **similar meaning** get vectors that point in **similar directions**.
- The number of values in each vector is the **dimension** (for example 256, 384, or 768). Every vector from the same model has the same dimension.
- We compare two vectors with **cosine similarity**: a score near `1.0` means "very similar", near `0.0` means "unrelated".

**An honest note about our toy model.** To let you run every example offline, this lesson includes a small `ToyEmbeddings` class. It only **counts shared words**, so it cannot understand that *vacation* and *annual leave* mean the same thing. A real model such as watsonx's Slate models learns meaning from huge amounts of text and normally handles such synonyms much better. The toy model is perfect for learning the **mechanics**, and the real model is what you use in production.

### 💻 The Code

This block uses the helper functions from the Setup section above.

```python
import numpy as np

embeddings = get_embeddings()          # ToyEmbeddings offline, watsonx when USE_WATSONX = True

def cosine(x, y):
    x, y = np.array(x), np.array(y)
    return float(x @ y / (np.linalg.norm(x) * np.linalg.norm(y)))

pairs = [
    ("sick leave days", "sick leave granted"),   # shares words
    ("sick leave days", "password changed"),     # unrelated
    ("vacation days", "annual leave"),           # same MEANING, different words
]

for a, b in pairs:
    score = cosine(embeddings.embed_query(a), embeddings.embed_query(b))
    print(f"{a:16} vs {b:20} -> similarity {score:.3f}")

# Output with the toy embedder:
# sick leave days  vs sick leave granted   -> similarity 0.667
# sick leave days  vs password changed     -> similarity 0.000
# vacation days    vs annual leave         -> similarity 0.000
#
# The last pair scores 0.000 only because the toy model counts words.
# A real embedding model should score that pair clearly higher.
```

## The Role of Embeddings in RAG

### 📖 The Story

Chef Lina runs a restaurant with **two shifts**. In the **morning prep shift**, she chops vegetables, labels them, and stores them in the fridge. That takes a while, but she does it **once**. In the **evening service shift**, a customer orders, and she grabs exactly the right ingredients from the fridge within seconds.

If she chopped everything from scratch for every order, no customer would ever be served on time. Preparation first, then fast service: that is the secret.

### 💡 The Explanation

A RAG pipeline also has **two shifts**:

| Shift | When | Steps |
|---|---|---|
| **Prep (indexing)** | Once, or when documents change | Load → Split into chunks → **Embed** each chunk → **Store** vectors in a vector database |
| **Service (querying)** | Every user question | **Embed the question** → **Search** the database for the closest vectors → Give the matching chunks to the LLM → Answer |

Two golden rules come from this:

1. **Use the same embedding model for chunks and questions.** Different models draw different maps, so their numbers cannot be compared.
2. Embeddings are what make **meaning-based search** possible. Without them, you can only match exact words.

### 💻 The Code

The block below builds a complete retrieval system **from scratch with plain NumPy**, so you can see exactly what a vector database does for you.

```python
import numpy as np

embeddings = get_embeddings()

# ----- PREP SHIFT (done once) -----
texts = [d.page_content for d in docs]
matrix = np.array(embeddings.embed_documents(texts))     # one row per chunk
print("Stored matrix shape:", matrix.shape)              # (number of chunks, dimension)

# ----- SERVICE SHIFT (done for every question) -----
question = "How often should passwords be changed?"
q_vector = np.array(embeddings.embed_query(question))    # SAME model as the chunks
scores = matrix @ q_vector                               # similarity of the question to every chunk
best = np.argsort(-scores)[:2]                           # indexes of the 2 highest scores

for i in best:
    print(f"{scores[i]:.3f} | {texts[i]}")

# Output with the toy embedder:
# Stored matrix shape: (9, 256)
# 0.333 | Passwords must be at least 12 characters long and changed every 90 days.
# 0.000 | Full-time employees receive 20 days of paid annual leave per year.
```

## Embedding Documents with watsonx

### 📖 The Story

Omar needs to send **letters to a foreign country**, but he does not speak the language. So he visits a **translation office**. He hands in his letters (the text) and receives them back **written in the foreign language** (the numbers). The office has a rule: *one translator for the whole project*. If he used a different translator for the reply, the words would no longer match.

The watsonx embedding model is that translation office. It turns human text into the numeric language that vector databases understand.

### 💡 The Explanation

LangChain talks to watsonx through the **`WatsonxEmbeddings`** class (package `langchain-ibm`). It follows the standard LangChain `Embeddings` interface, so anything you learn here works for every other embedding provider too. Only **two methods** matter:

| Method | Input | Output | Used for |
|---|---|---|---|
| `embed_documents(texts)` | a **list** of strings | a list of vectors | The prep shift: embedding chunks |
| `embed_query(text)` | **one** string | one vector | The service shift: embedding the question |

Settings you will meet:

- `model_id`: which embedding model (for example the Slate family, such as `ibm/slate-125m-english-rtrvr-v2`).
- `url` and `project_id`: where your watsonx project lives. The API key comes from `WATSONX_APIKEY`.
- `params` with `TRUNCATE_INPUT_TOKENS`: embedding models accept a limited number of tokens (for the Slate models, roughly 512). Longer text is cut off, which is one more reason to **split into chunks first**.

Always check two numbers after embedding: **how many vectors** you got (it must equal the number of texts) and **the dimension** (it must be identical for documents and questions).

### 💻 The Code

```python
embeddings = get_embeddings()            # WatsonxEmbeddings when USE_WATSONX = True

texts = [d.page_content for d in docs]
vectors = embeddings.embed_documents(texts)                       # many texts, many vectors
query_vector = embeddings.embed_query("How many sick days do I get?")   # one text, one vector

print("Documents embedded      :", len(vectors))
print("Vector size (dimension) :", len(vectors[0]))
print("Query vector size       :", len(query_vector))
print("First five numbers      :", [round(x, 3) for x in vectors[0][:5]])
print("Same dimension?         :", len(vectors[0]) == len(query_vector))

# Output with the toy embedder:
# Documents embedded      : 9
# Vector size (dimension) : 256
# Query vector size       : 256
# First five numbers      : [0.0, 0.0, 0.0, 0.0, 0.0]
# Same dimension?         : True
#
# With a watsonx Slate model the dimension is larger (typically 768 for the 125m model)
# and the numbers are all non-zero decimals.
```

## Preprocessing Documents with LangChain

### 📖 The Story

Grandma Ruth packs **lunchboxes** for the whole school trip. She never throws food in unwashed. She **washes** the apples, **removes** the rotten ones, **cuts** big sandwiches into portions, and **sticks a name label** on each box. Because of this care, nothing spoils and nobody gets lost.

Documents need the same care before embedding. Messy spaces, empty pages, repeated text, and missing labels all make embeddings worse and retrieval confusing.

### 💡 The Explanation

A good preprocessing routine has five steps:

1. **Load** documents into LangChain `Document` objects. Loaders exist for text, PDF, web pages, and more (for example `TextLoader`, `PyPDFLoader`, `WebBaseLoader`).
2. **Clean** the text: remove page markers, repeated spaces, and extra blank lines.
3. **Filter** out pages and chunks that are empty or too short to carry meaning.
4. **Split** into chunks (Lesson 2) with `split_documents`, which keeps the metadata.
5. **Enrich and de-duplicate**: add useful metadata (department, year, chunk id) and drop exact duplicates.

Metadata is not wasted effort. It becomes the **filter** that the Self-Query retriever uses later in this lesson.

### 💻 The Code

```python
import re
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ---------- Step 1: "loaded" pages (normally from a loader such as PyPDFLoader) ----------
raw_pages = [
    Document(page_content="  Company   Policies\n\n\n1. Leave Policy\nFull-time employees receive 20 days of paid annual leave per year.   \n\n\nSick leave is granted for up to 10 days per year.\n\n[PAGE 2]\n\n\n\n",
             metadata={"source": "handbook.pdf", "page": 1}),
    Document(page_content="   \n\n", metadata={"source": "handbook.pdf", "page": 2}),   # an empty page
    Document(page_content="2. Information Security\nPasswords must be at least 12 characters long and changed every 90 days.\nLost or stolen devices must be reported to the IT team within 24 hours.",
             metadata={"source": "handbook.pdf", "page": 3}),
    Document(page_content="2. Information Security\nPasswords must be at least 12 characters long and changed every 90 days.\nLost or stolen devices must be reported to the IT team within 24 hours.",
             metadata={"source": "handbook.pdf", "page": 4}),                          # a duplicated page
]

# ---------- Step 2: clean ----------
def clean(text):
    text = re.sub(r"\[PAGE \d+\]", "", text)     # remove page markers
    text = re.sub(r"[ \t]+", " ", text)          # collapse repeated spaces
    text = re.sub(r"\n{3,}", "\n\n", text)       # collapse blank lines
    return text.strip()

# ---------- Step 3: filter empty pages, and add metadata ----------
cleaned = []
for page in raw_pages:
    text = clean(page.page_content)
    if len(text) < 20:
        continue                                 # skip empty or tiny pages
    department = "HR" if "Leave" in text else "IT"
    cleaned.append(Document(page_content=text, metadata={**page.metadata, "department": department}))
print("Pages:", len(raw_pages), "->", len(cleaned))

# ---------- Step 4: split (metadata is copied to every chunk) ----------
splitter = RecursiveCharacterTextSplitter(chunk_size=120, chunk_overlap=20)
chunks = [c for c in splitter.split_documents(cleaned) if len(c.page_content.strip()) >= 20]

# ---------- Step 5: remove exact duplicates, add a chunk id ----------
seen, unique_chunks = set(), []
for i, chunk in enumerate(chunks):
    key = chunk.page_content.lower()
    if key in seen:
        continue
    seen.add(key)
    chunk.metadata["chunk_id"] = i
    unique_chunks.append(chunk)

print("Chunks:", len(chunks), "-> unique:", len(unique_chunks))
for c in unique_chunks:
    print(c.metadata, "|", repr(c.page_content[:45]))

# Output:
# Pages: 4 -> 3
# Chunks: 6 -> unique: 4
# {'source': 'handbook.pdf', 'page': 1, 'department': 'HR', 'chunk_id': 0} | 'Company Policies\n\n1. Leave Policy\nFull-time e'
# {'source': 'handbook.pdf', 'page': 1, 'department': 'HR', 'chunk_id': 1} | 'Sick leave is granted for up to 10 days per y'
# {'source': 'handbook.pdf', 'page': 3, 'department': 'IT', 'chunk_id': 2} | '2. Information Security\nPasswords must be at '
# {'source': 'handbook.pdf', 'page': 3, 'department': 'IT', 'chunk_id': 3} | 'Lost or stolen devices must be reported to th'
```

## How Vector Stores Compare Vectors

### 📖 The Story

Three friends, Ana, Ben, and Cy, stand in a field. The teacher asks, "Who is **most similar** to Ana?" There are three ways to judge it. You can measure the **straight distance** between people (*who stands closest?*). You can check **which direction** each person is facing (*who looks the same way?*). Or you can multiply their positions together and see **how strongly they line up** (*dot product*).

Each rule is useful, but each answers a slightly different question. Vector databases let you choose the rule.

### 💡 The Explanation

| Metric | Idea | Bigger score means | Notes |
|---|---|---|---|
| **Cosine similarity** | The angle between two vectors | More similar (max `1.0`) | Ignores vector length. The most popular choice for text. |
| **Euclidean (L2) distance** | Straight-line distance | **Less** similar | Lower is better. Many stores report the **squared** distance. |
| **Dot product (inner product)** | Direction **and** length together | More similar | Same as cosine when vectors have length 1. |

A useful fact: when all vectors are **normalised to length 1** (most embedding models do this), the three metrics rank results **in the same order**, and squared L2 distance equals `2 × (1 − cosine)`.

**Careful: lower can be better.** Chroma and FAISS often return a **distance** (lower is better), while LangChain's "relevance score" is a similarity (higher is better). Always check which one you are looking at.

### 💻 The Code

```python
import numpy as np

emb = get_embeddings()
a = np.array(emb.embed_query("sick leave days"))
b = np.array(emb.embed_query("sick leave granted"))      # similar to a
c = np.array(emb.embed_query("password changed"))        # unrelated to a

def cosine(x, y): return float(x @ y / (np.linalg.norm(x) * np.linalg.norm(y)))
def l2(x, y): return float(np.linalg.norm(x - y))
def dot(x, y): return float(x @ y)

print("pair | cosine | L2 distance | dot")
for name, (x, y) in {"a-b (similar)": (a, b), "a-c (unrelated)": (a, c)}.items():
    print(f"{name:16} {cosine(x, y):.3f}   {l2(x, y):.3f}        {dot(x, y):.3f}")

# The squared-L2 shortcut for length-1 vectors
print("squared L2 a-b :", round(l2(a, b) ** 2, 3), "| 2*(1-cosine):", round(2 * (1 - cosine(a, b)), 3))

# Vector LENGTH matters for dot and L2, but not for cosine
x, y = np.array([1.0, 0.0]), np.array([3.0, 0.0])
print("same direction, different length -> cosine:", cosine(x, y), "| L2:", l2(x, y), "| dot:", dot(x, y))

# Output with the toy embedder:
# pair | cosine | L2 distance | dot
# a-b (similar)    0.667   0.816        0.667
# a-c (unrelated)  0.000   1.414        0.000
# squared L2 a-b : 0.667 | 2*(1-cosine): 0.667
# same direction, different length -> cosine: 1.0 | L2: 2.0 | dot: 3.0
```

## Chroma DB

### 📖 The Story

Chroma is a **friendly neighbourhood library**. It opens its doors in one minute, needs no big building, and keeps books on a shelf in your own house (a folder on your computer). Every book has a **label card** (metadata), so you can ask, "Show me only the Finance books." If you stop by tomorrow, the books are still there.

### 💡 The Explanation

**Chroma DB** is an open-source vector database that is easy to start with and supports **persistence** (saving to disk) and **metadata filtering**.

Key settings:

| Setting | What it does |
|---|---|
| `collection_name` | The name of the "shelf". Must be 3 or more characters. |
| `persist_directory` | A folder where data is saved. Leave it out to keep everything in memory only. Current Chroma versions save automatically, so the old `.persist()` call is no longer needed. |
| `collection_metadata={"hnsw:space": "cosine"}` | Chooses the distance rule: `"l2"` (default), `"cosine"`, or `"ip"`. |
| `filter={...}` | Restricts a search to documents whose metadata match. Use operators like `$and`, `$gte`. |

Useful operations: `from_documents`, `similarity_search`, `similarity_search_with_score`, `add_documents`, `delete`, and reloading from the same folder.

Watch out: running `from_documents` again on a folder that already contains the collection **adds the documents a second time** (duplicates). Section "Troubleshooting" shows this.

### 💻 The Code

```python
import shutil
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

embeddings = get_embeddings()
shutil.rmtree("./chroma_db", ignore_errors=True)          # start from a clean folder

# ---------- Create and save ----------
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="policies",
    persist_directory="./chroma_db",
    collection_metadata={"hnsw:space": "cosine"},         # use cosine distance
)
print("Stored vectors:", vectordb._collection.count())

# ---------- Search with scores (Chroma returns a DISTANCE: lower = closer) ----------
results = vectordb.similarity_search_with_score("sick leave days", k=2)
for doc, distance in results:
    print(f"distance={distance:.3f} | {doc.page_content[:45]}")

# ---------- Search with a metadata filter ----------
finance_only = vectordb.similarity_search("days", k=3, filter={"department": "Finance"})
print("Finance only:", [d.page_content[:30] for d in finance_only])

hr_recent = vectordb.similarity_search(
    "days", k=5, filter={"$and": [{"department": "HR"}, {"year": {"$gte": 2023}}]}
)
print("HR, 2023 or later:", [d.page_content[:30] for d in hr_recent])

# ---------- Add and delete ----------
new_doc = Document(page_content="Employees receive a 100 dollar wellness stipend each year.",
                   metadata={"source": "handbook", "department": "HR", "year": 2024})
new_ids = vectordb.add_documents([new_doc])
print("After add   :", vectordb._collection.count())
vectordb.delete(ids=new_ids)
print("After delete:", vectordb._collection.count())

# ---------- Reload from disk later (no need to embed again) ----------
reloaded = Chroma(collection_name="policies", persist_directory="./chroma_db",
                  embedding_function=embeddings)
print("Reloaded vectors:", reloaded._collection.count())

# Output with the toy embedder:
# Stored vectors: 9
# distance=0.423 | Sick leave is granted for up to 10 days per y
# distance=0.635 | Full-time employees receive 20 days of paid a
# Finance only: ['Travel expenses must be submit', 'Employees may claim up to 50 d']
# HR, 2023 or later: ['Employees may work remotely up', 'Sick leave is granted for up t', 'Full-time employees receive 20']
# After add   : 10
# After delete: 9
# Reloaded vectors: 9
```

## FAISS

### 📖 The Story

FAISS is a **lightning-fast warehouse robot** built by Facebook's research team. It is extremely quick at one job: finding the closest items among millions. But the robot is a bit plain. It stores numbers on shelves and keeps a separate **notebook** (the docstore) that connects each shelf position to the original text and label. It does not have fancy filtering machinery of its own, and you save its whole warehouse as a **file** when you are done.

### 💡 The Explanation

**FAISS** (Facebook AI Similarity Search) is a **library**, not a server. It runs inside your Python process and is built for **speed** on large collections.

| Topic | FAISS | Chroma |
|---|---|---|
| What it is | A fast similarity-search library | A full vector database |
| Saving | `save_local(folder)` and `load_local(folder, embeddings)` | Automatic, with `persist_directory` |
| Default distance in LangChain | **Squared L2** (lower is better) | L2 unless you choose cosine |
| Metadata filtering | Basic (`filter=` on metadata in LangChain) | Rich operators (`$and`, `$gte`, ...) |
| Best for | Speed, large local indexes, experiments | Easy apps with filtering and persistence |

Important facts:

- Because the vectors are length 1, FAISS's squared L2 score equals `2 × (1 − cosine)`. A score of `0.845` means cosine similarity of about `0.577`.
- To get **similarity** (higher is better) instead, pass `distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT`.
- `load_local` needs `allow_dangerous_deserialization=True`, because the docstore is stored with Python's pickle format. **Only load files you created yourself.**
- `merge_from(other)` combines two FAISS stores, and `delete(ids)` removes items.

### 💻 The Code

```python
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy

embeddings = get_embeddings()

# ---------- Create ----------
faiss_db = FAISS.from_documents(docs, embeddings)
print("Vectors:", faiss_db.index.ntotal, "| dimension:", faiss_db.index.d)

# ---------- Search (default score is squared L2 distance: lower = closer) ----------
for doc, distance in faiss_db.similarity_search_with_score("sick leave days", k=2):
    print(f"L2 distance={float(distance):.3f} | {doc.page_content[:45]}")

# ---------- Save and load ----------
faiss_db.save_local("faiss_index")
loaded = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
print("Loaded vectors:", loaded.index.ntotal, "|", loaded.similarity_search("password", k=1)[0].page_content[:30])

# ---------- Merge a second store, then delete one item ----------
extra = FAISS.from_texts(["Extra policy about parking."], embeddings,
                         metadatas=[{"department": "Facilities", "year": 2024}])
loaded.merge_from(extra)
print("After merge :", loaded.index.ntotal, "|", loaded.similarity_search("parking", k=1)[0].metadata)

first_id = list(loaded.docstore._dict.keys())[0]
loaded.delete([first_id])
print("After delete:", loaded.index.ntotal)

# ---------- A similarity score instead of a distance ----------
similarity_db = FAISS.from_documents(docs, embeddings, distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT)
for doc, score in similarity_db.similarity_search_with_score("sick leave days", k=2):
    print(f"similarity={float(score):.3f} | {doc.page_content[:45]}")

# Output with the toy embedder:
# Vectors: 9 | dimension: 256
# L2 distance=0.845 | Sick leave is granted for up to 10 days per y
# L2 distance=1.270 | Full-time employees receive 20 days of paid a
# Loaded vectors: 9 | Passwords must be at least 12 
# After merge : 10 | {'department': 'Facilities', 'year': 2024}
# After delete: 9
# similarity=0.577 | Sick leave is granted for up to 10 days per y
# similarity=0.365 | Full-time employees receive 20 days of paid a
```

## Vector Store-Based Retriever

### 📖 The Story

Chef Lina's fridge is the vector store. But customers do not walk into the fridge. They talk to a **waiter**. The waiter takes the order, goes to the fridge, and brings back the **best few items**. The fridge stores; the waiter fetches.

In LangChain, the **retriever** is the waiter. You tell it *how* to fetch: "the 2 closest items", "the closest items but varied", or "only items that are close enough".

### 💡 The Explanation

Every vector store can become a retriever with **`.as_retriever()`**. A retriever has one standard method, **`.invoke(question)`**, that returns a list of `Document` objects. (The older `get_relevant_documents` is deprecated.) You choose the **search type**:

| `search_type` | Meaning | When to use |
|---|---|---|
| `"similarity"` (default) | The `k` closest chunks | Most questions |
| `"mmr"` (maximal marginal relevance) | Close chunks that are also **different from each other** (`fetch_k` candidates, `lambda_mult` balances relevance and variety) | When top results are near-duplicates |
| `"similarity_score_threshold"` | Only chunks above a minimum relevance (`score_threshold`) | When "no answer" is better than a bad answer |

Key settings go inside `search_kwargs`: `k`, `filter`, `fetch_k`, `lambda_mult`, `score_threshold`.

### 💻 The Code

```python
from langchain_community.vectorstores import Chroma

embeddings = get_embeddings()
store = Chroma.from_documents(
    docs, embeddings, collection_name="retriever_demo",
    collection_metadata={"hnsw:space": "cosine"},         # in memory only: no persist_directory
)

# ---------- 1) Plain similarity ----------
similarity = store.as_retriever(search_type="similarity", search_kwargs={"k": 2})
print("similarity:", [d.page_content[:25] for d in similarity.invoke("sick leave days")])

# ---------- 2) MMR: relevant AND varied ----------
mmr = store.as_retriever(search_type="mmr", search_kwargs={"k": 2, "fetch_k": 6, "lambda_mult": 0.5})
print("mmr       :", [d.page_content[:25] for d in mmr.invoke("employees days")])

# ---------- 3) Score threshold: only good matches ----------
strict = store.as_retriever(search_type="similarity_score_threshold",
                            search_kwargs={"score_threshold": 0.3, "k": 5})
print("threshold 0.3:", [d.page_content[:25] for d in strict.invoke("sick leave days")])

very_strict = store.as_retriever(search_type="similarity_score_threshold",
                                 search_kwargs={"score_threshold": 0.9, "k": 5})
print("threshold 0.9:", very_strict.invoke("sick leave days"))      # nothing is good enough

# Output with the toy embedder:
# similarity: ['Sick leave is granted for', 'Full-time employees recei']
# mmr       : ['Employees may work remote', 'Full-time employees recei']
# threshold 0.3: ['Sick leave is granted for', 'Full-time employees recei']
# threshold 0.9: []        (LangChain also prints a warning: no relevant docs were retrieved)
```

## Multi-Query Retriever

### 📖 The Story

Zoe lost her blue umbrella and asked the school secretary, "Did anyone find a **rain thing**?" The secretary shrugged. So Zoe asked three friends to ask for her, each in different words: "a blue **umbrella**", "a **parasol** left in class", "a **rainy-day** item with a handle". One of the three questions finally matched the label on the lost-property box.

One question can miss good answers just because of **its wording**. Asking the same thing in several ways catches more.

### 💡 The Explanation

The **`MultiQueryRetriever`** uses an **LLM** to rewrite your question into several versions (by default three). It runs a search for **each version** and returns the **combined, de-duplicated** results.

How it works:

1. The user asks one question.
2. The LLM writes several alternative questions.
3. The base retriever searches for each one (here with `k=1` to keep the demo short).
4. The unique documents from all searches are merged.

Trade-offs: it improves **recall** (finding more relevant chunks) but adds **one LLM call and several searches** to every question, so it costs more time and money. You can see the generated questions by turning on `INFO` logging for `langchain.retrievers.multi_query`.

In the block below, `get_llm(...)` is told exactly what to reply, so you can see the mechanics **offline**. With `USE_WATSONX = True` a real watsonx model writes the alternative questions by itself.

### 💻 The Code

```python
import logging
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.vectorstores import Chroma

embeddings = get_embeddings()
store = Chroma.from_documents(docs, embeddings, collection_name="multiquery_demo",
                              collection_metadata={"hnsw:space": "cosine"})
base_retriever = store.as_retriever(search_kwargs={"k": 1})

# Show the questions that the LLM writes
logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

llm = get_llm(scripted_replies=[
    "How many sick days am I allowed?\n"
    "What is the sick leave policy?\n"
    "When do I need a doctor's note for sick leave?"
])
multi_query = MultiQueryRetriever.from_llm(retriever=base_retriever, llm=llm)

question = "How much time off do I get when I am ill?"

print("Normal retriever:")
for d in base_retriever.invoke(question):
    print("  -", d.page_content[:55])

print("Multi-query retriever:")
for d in multi_query.invoke(question):
    print("  -", d.page_content[:55])

# Output with the toy embedder (the INFO log line also lists the 3 generated questions):
# Normal retriever:
#   - Full-time employees receive 20 days of paid annual leav
# Multi-query retriever:
#   - Sick leave is granted for up to 10 days per year and ma
#
# The normal retriever matched the word "time" inside "Full-time" and returned the WRONG policy.
# The rewritten questions mention "sick" and "leave", so the multi-query retriever found the right one.
```

## Self-Query Retriever

### 📖 The Story

Omar goes to a movie rental shop and says, "I want a **funny** movie, made **after 2010**, from the **comedy** shelf." A clumsy clerk would search only for the word "funny". A smart clerk understands that the sentence has **two parts**: *what it is about* (funny) and *rules about the labels* (after 2010, comedy shelf). The smart clerk first **narrows the shelves by the labels**, then looks for the funny ones.

### 💡 The Explanation

The **`SelfQueryRetriever`** gives your retriever that same skill. An **LLM reads the user's question** and splits it into:

- a **query** for the meaning search, such as `"leave"`, and
- a **filter** on metadata, such as `department == "HR" and year > 2022`.

It then runs a filtered vector search. For this to work you must describe your metadata to the LLM using **`AttributeInfo`** (name, description, type), and describe the documents in one sentence (`document_content_description`). The package `lark` must be installed, and the vector store must support the filter language (Chroma does).

This is where the **metadata** from the preprocessing section pays off. Without good metadata, there is nothing to filter on.

As before, the LLM here is **scripted** so that you can run the block offline. A real LLM produces that same JSON by itself.

### 💻 The Code

```python
import json
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_community.vectorstores import Chroma

embeddings = get_embeddings()
store = Chroma.from_documents(docs, embeddings, collection_name="selfquery_demo",
                              collection_metadata={"hnsw:space": "cosine"})

# Describe the metadata so that the LLM knows which filters exist
metadata_field_info = [
    AttributeInfo(name="department",
                  description="The department that owns the policy: HR, IT or Finance",
                  type="string"),
    AttributeInfo(name="year",
                  description="The year the policy was last updated",
                  type="integer"),
]

# What a real LLM would answer for the question below (scripted here, so the block runs offline)
payload = {"query": "leave", "filter": 'and(eq("department", "HR"), gt("year", 2022))'}
fence = "`" * 3                                   # the LLM wraps its JSON answer in a code fence
scripted_reply = f"{fence}json\n{json.dumps(payload, indent=4)}\n{fence}"

self_query = SelfQueryRetriever.from_llm(
    llm=get_llm(scripted_replies=[scripted_reply]),
    vectorstore=store,
    document_contents="Short company policy statements",
    metadata_field_info=metadata_field_info,
)

results = self_query.invoke("HR policies about leave updated after 2022")
for d in results:
    print(d.metadata["department"], d.metadata["year"], "|", d.page_content[:45])

# Output with the toy embedder (the order of the three results can vary):
# HR 2024 | Sick leave is granted for up to 10 days per y
# HR 2023 | Full-time employees receive 20 days of paid a
# HR 2024 | Employees may work remotely up to three days
#
# Only HR documents newer than 2022 came back. The 2022 parental leave policy and the
# IT and Finance policies were filtered out BEFORE the similarity search.
```

## Parent Document Retriever

### 📖 The Story

Ben the librarian has a problem. **Tiny index cards** are easy to match with a question, but a single card, such as "every 90 days.", does not explain anything. A **whole chapter** gives full context, but it is too big to match precisely.

Ben's clever solution: he writes **small index cards** that each point to **the full chapter they came from**. A reader's question is matched against the tiny cards (precise!), but Ben then hands over the **whole chapter** (full context!). Best of both worlds.

### 💡 The Explanation

The **`ParentDocumentRetriever`** solves the chunk-size dilemma from Lesson 2:

- **Small chunks** are better for **searching** (precise meaning).
- **Large chunks** are better for **answering** (enough context for the LLM).

It uses **two splitters** and **two stores**:

| Piece | Job |
|---|---|
| `child_splitter` | Cuts documents into **small child chunks**. These get embedded and stored in the **vector store**. |
| `parent_splitter` | Cuts documents into **larger parent chunks**. These are stored in a plain **docstore** (here `InMemoryStore`). |
| Retrieval | Search finds the best **child**, then the retriever returns its **parent**. |

Each child remembers its parent through a hidden id. If you leave out `parent_splitter`, the whole original document becomes the parent.

### 💻 The Code

```python
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

embeddings = get_embeddings()

parent_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=0)   # big pieces for answers
child_splitter = RecursiveCharacterTextSplitter(chunk_size=80, chunk_overlap=0)     # small pieces for search

child_store = Chroma(collection_name="children_demo", embedding_function=embeddings)
parent_store = InMemoryStore()

retriever = ParentDocumentRetriever(
    vectorstore=child_store,          # holds the small children (embedded)
    docstore=parent_store,            # holds the big parents (plain text)
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)

retriever.add_documents([Document(page_content=companypolicies, metadata={"source": "handbook"})])
print("Parents:", len(list(parent_store.yield_keys())), "| children:", child_store._collection.count())

question = "password changed"

# What a plain vector search would give: only the small child
child = child_store.similarity_search(question, k=1)[0]
print("CHILD :", len(child.page_content), "characters ->", repr(child.page_content))

# What the parent document retriever gives: the whole parent
parent = retriever.invoke(question)[0]
print("PARENT:", len(parent.page_content), "characters ->", repr(parent.page_content[:110]), "...")

# Output with the toy embedder:
# Parents: 4 | children: 19
# CHILD : 72 characters -> 'Passwords must be at least 12 characters long and changed every 90 days.'
# PARENT: 240 characters -> '4. Information Security\nPasswords must be at least 12 characters long and changed every 90 days.\nConfidential data must ' ...
```

## Choosing a Retriever

### 📖 The Story

Eli stands in front of four tools on a workbench. A **plain net** catches most fish. A **set of three nets of different shapes** catches fish that hide. A **net with a filter** only catches fish of a chosen colour. A **big basket attached to a tiny net** brings back the whole shoal that one fish belongs to. The skilled fisher does not use all four every time. They **look at the water** and pick.

### 💡 The Explanation

| Retriever | Fixes this problem | Extra cost | Needs |
|---|---|---|---|
| **Vector store-based** (similarity, MMR, threshold) | The default: find close chunks | None | A vector store |
| **Multi-Query** | The question's wording misses relevant chunks | One LLM call plus several searches per question | An LLM |
| **Self-Query** | Questions contain filters ("after 2022", "HR only") | One LLM call per question | An LLM and good metadata |
| **Parent Document** | Small chunks search well but lack context for answers | Two stores to maintain | A docstore plus a vector store |

They can also be **combined** (for example, a Parent Document retriever as the base of a Multi-Query retriever), but start simple and add one tool at a time, measuring whether answers improve.

### 💻 The Code

The function below turns the table into code.

```python
def choose_retriever(situation: dict) -> str:
    """Suggest a retriever from a few yes/no facts about your project."""
    if situation.get("questions_contain_filters") and situation.get("has_metadata"):
        return "SelfQueryRetriever"
    if situation.get("answers_need_surrounding_context"):
        return "ParentDocumentRetriever"
    if situation.get("users_phrase_questions_in_many_ways"):
        return "MultiQueryRetriever"
    if situation.get("results_are_repetitive"):
        return "Vector store retriever with search_type='mmr'"
    return "Vector store retriever with search_type='similarity'"

cases = {
    "Show me HR policies from 2024": {"questions_contain_filters": True, "has_metadata": True},
    "Answers look cut off and lack context": {"answers_need_surrounding_context": True},
    "Users ask the same thing in many styles": {"users_phrase_questions_in_many_ways": True},
    "Top 4 results are near-duplicates": {"results_are_repetitive": True},
    "Simple FAQ bot": {},
}
for name, facts in cases.items():
    print(f"{name:42} -> {choose_retriever(facts)}")

# Output:
# Show me HR policies from 2024              -> SelfQueryRetriever
# Answers look cut off and lack context      -> ParentDocumentRetriever
# Users ask the same thing in many styles    -> MultiQueryRetriever
# Top 4 results are near-duplicates          -> Vector store retriever with search_type='mmr'
# Simple FAQ bot                             -> Vector store retriever with search_type='similarity'
```

## How InstructLab Works

### 📖 The Story

Two students prepare for an exam about the company handbook. **Student Rita** is allowed an **open book**. She does not memorise anything. During the exam she quickly looks up the right page and answers. **Student Finn** is not allowed a book. He **studies for weeks**, writes his own practice questions, and trains until the knowledge is in his head. Rita is flexible and always up to date (just swap the book). Finn answers fast and in the right style, but if the handbook changes, he must study again.

Rita is **RAG**. Finn is **fine-tuning**, and **InstructLab** is the method that helps Finn study.

### 💡 The Explanation

**InstructLab** is an open-source project (started by IBM Research and Red Hat) for **adding new knowledge and skills to a language model** through a community-friendly process. The "LAB" stands for **Large-scale Alignment for chatBots**. You do not need to write thousands of training examples by hand. Instead:

1. **Taxonomy:** you write a small number of **seed examples** in a `qna.yaml` file, organised in a folder tree. *Knowledge* contributions come with source documents. *Skills* contributions teach how to do something.
2. **Synthetic data generation:** a **teacher model** reads your seed examples and creates a large set of new training examples (`ilab data generate`).
3. **Training:** the student model is **fine-tuned** on that synthetic data (`ilab model train`).
4. **Chat and serve:** you test the tuned model (`ilab model chat`) and serve it for applications (`ilab model serve`).

Practical facts to remember:

- Fine-tuning changes the **model's weights**, so you need serious **compute (usually GPUs)** and time. A laptop gives only a low-fidelity approximation.
- Commands and requirements change between versions (for example, some versions do not support the newest Python releases). Always run `ilab --help` and follow the current InstructLab documentation.
- The exact `qna.yaml` rules (such as the minimum number of seed examples) also change, so treat the file below as a **shape**, not a final contribution.

### 💻 The Code

This is a shell script, not Python. Run it in a terminal on a machine suited for training.

```bash
# ---------- 1) Set up (check the docs for the Python version your ilab release supports) ----------
python3.11 -m venv venv
source venv/bin/activate
pip install instructlab

ilab config init                      # creates the config and the local taxonomy folder
ilab model download                   # downloads the base model(s) used by default

# ---------- 2) Add knowledge to the taxonomy ----------
mkdir -p taxonomy/knowledge/company/policies

cat > taxonomy/knowledge/company/policies/qna.yaml <<'EOF'
version: 3
created_by: your-github-username
domain: company_policies
seed_examples:
  - context: |
      Full-time employees receive 20 days of paid annual leave per year.
      Sick leave is granted for up to 10 days per year and may require a doctor's note.
    questions_and_answers:
      - question: How many days of paid annual leave do full-time employees receive?
        answer: Full-time employees receive 20 days of paid annual leave per year.
      - question: Can sick leave require a doctor's note?
        answer: Yes. Sick leave is granted for up to 10 days per year and may require a doctor's note.
      - question: How many sick leave days are granted per year?
        answer: Up to 10 days per year.
  # ... add more seed examples here (real contributions need several contexts)
document_outline: Summary of the company leave and security policies
document:
  repo: https://github.com/your-org/company-policies-docs
  commit: REPLACE_WITH_COMMIT_ID
  patterns:
    - handbook.md
EOF

# ---------- 3) Check, generate, train, test ----------
ilab taxonomy diff                    # validates that your new files are in the right shape
ilab data generate                    # the teacher model writes synthetic training data
ilab model train                      # fine-tunes the student model (GPU recommended)
ilab model chat                       # ask: "How many days of paid annual leave do I get?"

# ---------- 4) Serve the tuned model for your apps ----------
ilab model serve
```

## Choosing Between RAG and Fine-Tuning

### 📖 The Story

The school principal asks Rita (the open-book student) and Finn (the studied student) to compete in **three challenges**. In challenge one, the handbook changes **every week**. Rita wins easily, because she just reads the new page. Finn has to study again. In challenge two, the school wants answers **always written in a friendly, special style**. Finn wins, because the style lives inside his head. In challenge three, the principal asks "**which page did you use?**" Rita proudly points to the page. Finn cannot say.

Neither student is the best. Each wins **different challenges**.

### 💡 The Explanation

| Question | RAG | Fine-tuning (InstructLab) |
|---|---|---|
| How is knowledge added? | Stored in a **vector database** and looked up at question time | Learned into the **model's weights** |
| When data changes often | ✅ Update the database in minutes | ❌ Needs new data generation and training |
| Source citations | ✅ Easy: return the retrieved chunks | ❌ Hard: the model cannot point to a source |
| Hallucination control | ✅ Strong: the answer is grounded in the retrieved text | ⚠️ Can still hallucinate |
| Teaching a new **style or skill** | ❌ Limited | ✅ Strong |
| Cost to start | ✅ Low: no training | ❌ High: GPUs, time, data work |
| Cost per question | ⚠️ Higher: retrieval plus a longer prompt | ✅ Lower: no retrieval step |
| Data privacy and access control | ✅ Filter or restrict documents per user | ⚠️ Knowledge is baked in for everyone |

The practical rule: **use RAG for facts that change and need sources; use fine-tuning for behaviour, style, and stable specialised knowledge; combine them when you need both.** Many teams fine-tune a model for tone and domain vocabulary, then add RAG for fresh facts.

### 💻 The Code

A simple scoring helper to start a team discussion (it is a conversation tool, not a law).

```python
def recommend_approach(project: dict) -> str:
    """Score a project: positive points favour RAG, negative points favour fine-tuning."""
    score = 0
    score += 2 if project.get("data_changes_often") else -1
    score += 2 if project.get("needs_source_citations") else 0
    score += 1 if project.get("limited_gpu_budget") else -1
    score += 1 if project.get("per_user_access_control") else 0
    score -= 2 if project.get("needs_new_style_or_skill") else 0
    score -= 1 if project.get("stable_specialised_knowledge") else 0

    if score >= 3:
        return f"RAG (score {score})"
    if score <= -2:
        return f"Fine-tuning with InstructLab (score {score})"
    return f"Combine both (score {score})"

projects = {
    "Daily-changing HR chatbot": {"data_changes_often": True, "needs_source_citations": True,
                                  "limited_gpu_budget": True, "per_user_access_control": True},
    "Pirate-style storytelling assistant": {"needs_new_style_or_skill": True,
                                            "stable_specialised_knowledge": True},
    "Support bot with a brand voice and weekly price changes": {"data_changes_often": True,
                                                                 "needs_new_style_or_skill": True},
}
for name, facts in projects.items():
    print(f"{name:55} -> {recommend_approach(facts)}")

# Output:
# Daily-changing HR chatbot                               -> RAG (score 6)
# Pirate-style storytelling assistant                     -> Fine-tuning with InstructLab (score -5)
# Support bot with a brand voice and weekly price changes -> Combine both (score -1)
```

## Common Mistakes and Troubleshooting

### 📖 The Story

Pip the baker's **"Oops Notebook"** from Lesson 2 is back, now with a new chapter about vectors. Each page says what went wrong, why, and how to fix it.

### 💡 The Explanation

| Problem | Cause | Fix |
|---|---|---|
| Search results look random | Chunks and questions were embedded with **different models** (or different settings) | Use one embedding model for both. Re-embed everything if you change models. |
| `AssertionError` or dimension error when searching | Vector sizes differ (for example a 64-number query against a 256-number index) | Check `len(vector)` for both and make sure the same model is used |
| Duplicate results after re-running your script | `from_documents` on an existing Chroma folder **adds the documents again** | Delete the folder first, use `get_or_create` logic, or add documents only once |
| `ValueError: The de-serialization relies loading a pickle file` | `FAISS.load_local` without the safety flag | Add `allow_dangerous_deserialization=True`, only for files you created yourself |
| Chroma error about the collection name | The name is shorter than 3 characters or has invalid characters | Use 3 or more letters, digits, `.`, `_`, or `-` |
| Scores look "backwards" | Distance (lower is better) versus similarity (higher is better) | Check the store's metric. Convert with `1 − distance` for cosine distance |
| Self-Query returns nothing or errors | Missing `lark`, vague `AttributeInfo` descriptions, or a filter on a field that does not exist | Install `lark`, describe each field clearly, and check the metadata names |
| Multi-Query is slow and costly | One LLM call plus many searches per question | Use it only where recall matters, and reduce `k` |
| Parent Document returns huge text | `parent_splitter` missing or `chunk_size` too large | Set a parent splitter with a sensible size |
| watsonx authentication error | Missing `WATSONX_APIKEY`, wrong URL, or wrong project ID | Check the environment variable, region URL, and project ID |

### 💻 The Code

The block reproduces three classic mistakes on purpose, with their messages.

```python
import shutil
from langchain_community.vectorstores import Chroma, FAISS

embeddings = get_embeddings()

# ---------- Mistake 1: a query vector from a DIFFERENT model (different dimension) ----------
faiss_db = FAISS.from_documents(docs, embeddings)                  # 256 numbers per vector
wrong_vector = ToyEmbeddings(dim=64).embed_query("sick leave")     # 64 numbers per vector
try:
    faiss_db.similarity_search_by_vector(wrong_vector, k=1)
except AssertionError:
    print("Mistake 1: AssertionError - the vector sizes do not match (64 vs 256)")

# ---------- Mistake 2: loading FAISS without the safety flag ----------
faiss_db.save_local("faiss_oops")
try:
    FAISS.load_local("faiss_oops", embeddings)
except ValueError as error:
    print("Mistake 2: ValueError -", str(error)[:60], "...")

# ---------- Mistake 3: running from_documents twice on the same Chroma folder ----------
shutil.rmtree("./chroma_oops", ignore_errors=True)
for run in (1, 2):
    db = Chroma.from_documents(docs, embeddings, collection_name="oops_demo",
                               persist_directory="./chroma_oops")
    print(f"Mistake 3: after run {run} the collection holds", db._collection.count(), "vectors")

# Output:
# Mistake 1: AssertionError - the vector sizes do not match (64 vs 256)
# Mistake 2: ValueError - The de-serialization relies loading a pickle file. Pickle fi ...
# Mistake 3: after run 1 the collection holds 9 vectors
# Mistake 3: after run 2 the collection holds 18 vectors
```

## Summary

### 📖 The Story

At the end of the term, Chef Lina, Mia the map-maker, and Ben the librarian sat together. Mia said: "I turn meaning into numbers." Lina said: "I store them and fetch them quickly." Ben said: "I choose the cleverest way to ask." Together they built the best library in the school, and the students never went hungry for answers.

### 💡 The Explanation

- An **embedding** is a list of numbers that captures the meaning of text. The **dimension** is its length, and the same model must embed chunks and questions.
- RAG has a **prep shift** (load, split, embed, store) and a **service shift** (embed the question, search, generate).
- **`WatsonxEmbeddings`** turns text into vectors with `embed_documents` and `embed_query`.
- **Preprocess** documents: clean, filter, split, add metadata, and remove duplicates.
- Vector stores compare vectors with **cosine**, **L2**, or **dot product**. Remember whether a score is a distance or a similarity.
- **Chroma** is an easy database with persistence and rich filtering. **FAISS** is a very fast library saved as files.
- **Retrievers:** vector store-based (similarity, MMR, threshold), **Multi-Query** (better recall), **Self-Query** (LLM-written metadata filters), **Parent Document** (search small, answer big).
- **RAG** is best for changing facts and citations. **Fine-tuning with InstructLab** is best for style, skills, and stable specialised knowledge. They can be combined.

### 💻 The Code

A compact cheat sheet you can keep.

```python
from langchain_community.vectorstores import Chroma, FAISS

embeddings = get_embeddings()

# Chroma: create, search, filter
chroma_db = Chroma.from_documents(docs, embeddings, collection_name="cheatsheet_chroma",
                                  collection_metadata={"hnsw:space": "cosine"})
print("Chroma  :", chroma_db.similarity_search("sick leave", k=1)[0].page_content[:40])
print("Filtered:", chroma_db.similarity_search("days", k=1, filter={"department": "Finance"})[0].page_content[:40])

# FAISS: create, search, retriever
faiss_db = FAISS.from_documents(docs, embeddings)
print("FAISS   :", faiss_db.similarity_search("sick leave", k=1)[0].page_content[:40])
print("Retriever:", len(faiss_db.as_retriever(search_kwargs={"k": 3}).invoke("passwords")), "documents")

# Output with the toy embedder:
# Chroma  : Sick leave is granted for up to 10 days 
# Filtered: Travel expenses must be submitted within
# FAISS   : Sick leave is granted for up to 10 days 
# Retriever: 3 documents
```

## Exercises

### Exercise 1: The Two Warehouses (Chroma versus FAISS)

📖 **Story:** Rita built her library in Chroma and Finn built his in FAISS. Both asked the same question, but Rita's librarian said "0.423" and Finn's said "0.845". They argued about who found the better match, until Mia the map-maker reminded them that **they use different rulers**.

**Your task:** build a Chroma store (with cosine distance) and a FAISS store (default L2) from `docs`. Ask both: *"sick leave days"* with `k=1`. Then **convert both scores to cosine similarity** so that they can be compared.

> **Hint:** Chroma cosine distance → similarity = `1 − distance`. FAISS squared L2 on length-1 vectors → similarity = `1 − distance / 2`.

### Exercise 2: Be the Self-Query Robot

📖 **Story:** The LLM in the Self-Query retriever is on holiday. Omar must do its job **by hand**: read a sentence, and write the **metadata filter** himself.

**Your task:** for the question *"IT policies updated after 2022"*, write the Chroma `filter` dictionary yourself, run `similarity_search` on a Chroma store built from `docs`, and print the results. Then write a small function `multi_query_search(store, queries, k)` that runs **several rewritten questions** and returns the **unique** results (this is the Multi-Query idea without an LLM).

### Exercise 3 (Capstone): The Handbook Assistant

📖 **Story:** The principal wants an **assistant for the Employee Handbook**. It must answer questions using the right section, filter by department when asked, and then decide whether the school should use RAG or fine-tuning.

Here is the handbook:

```python
handbook_md = """# Employee Handbook

## Remote Work
Employees may work remotely up to three days per week with manager approval. Remote workers must be available during core hours, from 10 AM to 3 PM. Company equipment must be kept secure at all times.

## Leave Policy
### Annual Leave
Full-time employees receive 20 days of paid annual leave per year. Leave requests should be submitted at least two weeks in advance.
### Sick Leave
Sick leave is granted for up to 10 days per year and may require a doctor's note.

## Information Security
Passwords must be at least 12 characters long and changed every 90 days. Lost or stolen devices must be reported to the IT team within 24 hours.
"""
```

**Your tasks:**

1. Split `handbook_md` in **two stages** (`MarkdownHeaderTextSplitter` with `strip_headers=False`, then `RecursiveCharacterTextSplitter` with `chunk_size=200`, `chunk_overlap=30`).
2. Add a **`section`** metadata value to every chunk (use the `Header 2` name).
3. Embed the chunks and store them in **Chroma** (cosine distance).
4. Write `ask(question, section=None, k=2)` that returns the best chunks, with an optional **section filter**.
5. Test it with *"How many days of sick leave do I get?"* (no filter, then filtered to `"Leave Policy"`).
6. Use `recommend_approach` from this lesson to decide between RAG and fine-tuning for this assistant when the handbook changes monthly and answers must cite the section.

## Solutions

### Solution 1: The Two Warehouses

**Explanation.** Chroma (with `hnsw:space = cosine`) reports a **cosine distance**, so similarity is `1 − distance`. FAISS reports **squared L2**, which for length-1 vectors equals `2 × (1 − cosine)`, so similarity is `1 − distance / 2`. Both converted scores are the same number, about `0.577`. The two stores found the **same best chunk**. They only used different rulers.

```python
from langchain_community.vectorstores import Chroma, FAISS

embeddings = get_embeddings()
query = "sick leave days"

chroma_db = Chroma.from_documents(docs, embeddings, collection_name="ex1_chroma",
                                  collection_metadata={"hnsw:space": "cosine"})
faiss_db = FAISS.from_documents(docs, embeddings)

chroma_doc, chroma_distance = chroma_db.similarity_search_with_score(query, k=1)[0]
faiss_doc, faiss_distance = faiss_db.similarity_search_with_score(query, k=1)[0]

chroma_similarity = 1 - chroma_distance
faiss_similarity = 1 - float(faiss_distance) / 2

print(f"Chroma: raw distance {chroma_distance:.3f} -> similarity {chroma_similarity:.3f} | {chroma_doc.page_content[:35]}")
print(f"FAISS : raw distance {float(faiss_distance):.3f} -> similarity {faiss_similarity:.3f} | {faiss_doc.page_content[:35]}")
print("Same best chunk?", chroma_doc.page_content == faiss_doc.page_content)

# Output with the toy embedder:
# Chroma: raw distance 0.423 -> similarity 0.577 | Sick leave is granted for up to 10 
# FAISS : raw distance 0.845 -> similarity 0.577 | Sick leave is granted for up to 10 
# Same best chunk? True
```

### Solution 2: Be the Self-Query Robot

**Explanation.** The question has two parts: the **topic** ("policies") and the **rules** (`department = IT`, `year > 2022`). Chroma filters use `$and`, `$gt`, and similar operators, so the filter is `{"$and": [{"department": "IT"}, {"year": {"$gt": 2022}}]}`. For the multi-query helper, we run each rewritten question and keep only unique documents. Notice how **different wordings** retrieve **different documents**, and the union covers more.

```python
from langchain_community.vectorstores import Chroma

embeddings = get_embeddings()
store = Chroma.from_documents(docs, embeddings, collection_name="ex2_store",
                              collection_metadata={"hnsw:space": "cosine"})

# ---------- Part 1: the filter that the Self-Query LLM would write ----------
it_filter = {"$and": [{"department": "IT"}, {"year": {"$gt": 2022}}]}
for d in store.similarity_search("policies", k=5, filter=it_filter):
    print(d.metadata["department"], d.metadata["year"], "|", d.page_content[:45])

# ---------- Part 2: multi-query without an LLM ----------
def multi_query_search(vector_store, queries, k=2):
    unique, seen = [], set()
    for q in queries:
        for doc in vector_store.similarity_search(q, k=k):
            if doc.page_content not in seen:
                seen.add(doc.page_content)
                unique.append(doc)
    return unique

queries = ["How much time can I take off when ill?",
           "sick leave days",
           "doctor's note for sick leave"]
results = multi_query_search(store, queries, k=1)
print("\nQuestions:", len(queries), "| unique documents:", len(results))
for d in results:
    print(" -", d.page_content[:50])

# Output with the toy embedder (the order of the first two lines may vary):
# IT 2024 | Passwords must be at least 12 characters long
# IT 2023 | Lost or stolen devices must be reported to th
#
# Questions: 3 | unique documents: 2
#  - Full-time employees receive 20 days of paid annual
#  - Sick leave is granted for up to 10 days per year a
```

### Solution 3 (Capstone): The Handbook Assistant

**Explanation.** Stage 1 cuts the handbook by headers and Stage 2 limits the chunk size. Each chunk receives a `section` label (from `Header 2`), which lets `ask` filter by section. Notice how the **filter** makes sure that a question about leave only searches the Leave Policy section. For Task 6, a handbook that changes monthly and needs citations is a very strong **RAG** case: updating a database is far cheaper than retraining a model, and the `section` metadata gives you the citation for free.

```python
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

handbook_md = """# Employee Handbook

## Remote Work
Employees may work remotely up to three days per week with manager approval. Remote workers must be available during core hours, from 10 AM to 3 PM. Company equipment must be kept secure at all times.

## Leave Policy
### Annual Leave
Full-time employees receive 20 days of paid annual leave per year. Leave requests should be submitted at least two weeks in advance.
### Sick Leave
Sick leave is granted for up to 10 days per year and may require a doctor's note.

## Information Security
Passwords must be at least 12 characters long and changed every 90 days. Lost or stolen devices must be reported to the IT team within 24 hours.
"""

# ---------- Task 1 and 2: two-stage split, then add a "section" label ----------
headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
stage1 = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on,
                                    strip_headers=False).split_text(handbook_md)
chunks = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30).split_documents(stage1)
chunks = [c for c in chunks if len(c.page_content.strip()) >= 40]       # drop the header-only chunk
for c in chunks:
    c.metadata["section"] = c.metadata.get("Header 2", "General")

# ---------- Task 3: embed and store ----------
embeddings = get_embeddings()
store = Chroma.from_documents(chunks, embeddings, collection_name="capstone_handbook",
                              collection_metadata={"hnsw:space": "cosine"})

# ---------- Task 4: the assistant's search function ----------
def ask(question, section=None, k=2):
    filter_ = {"section": section} if section else None
    return store.similarity_search(question, k=k, filter=filter_)

# ---------- Task 5: test ----------
question = "How many days of sick leave do I get?"
print("No filter:")
for d in ask(question):
    print("  -", d.metadata["section"], "|", d.page_content[:55].replace("\n", " "))

print("Filtered to 'Leave Policy':")
for d in ask(question, section="Leave Policy"):
    print("  -", d.metadata["section"], "|", d.page_content[:55].replace("\n", " "))

# ---------- Task 6: RAG or fine-tuning? ----------
handbook_project = {"data_changes_often": True, "needs_source_citations": True,
                    "limited_gpu_budget": True, "per_user_access_control": False}
print("Decision:", recommend_approach(handbook_project))

# Output with the toy embedder:
# No filter:
#   - Leave Policy | ### Sick Leave Sick leave is granted for up to 10 days 
#   - Leave Policy | ## Leave Policy   ### Annual Leave Full-time employees 
# Filtered to 'Leave Policy':
#   - Leave Policy | ### Sick Leave Sick leave is granted for up to 10 days 
#   - Leave Policy | ## Leave Policy   ### Annual Leave Full-time employees 
# Decision: RAG (score 5)
```

### Bonus Challenges

1. Turn on `USE_WATSONX = True` (with your credentials) and compare how the real embedding model handles the *"vacation days"* versus *"annual leave"* pair from the first section.
2. Add a **Parent Document retriever** to the capstone, using whole sections as parents and sentences as children.
3. Replace the scripted LLM in the Self-Query example with a real watsonx LLM, and test five questions with different filters.
4. Create a real `qna.yaml` for your own handbook and run the InstructLab workflow on a GPU machine. Compare its answers with your RAG assistant on the same ten questions.

*End of Lesson 3. Next up: putting retrieval and generation together into a complete question-answering chain.*
