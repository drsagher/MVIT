# Lesson 3 Turn Text Chunks into Embeddings and Store Them in Vector Stores for Smart Retrieval

In Lesson 2 you learned to cut long documents into neat chunks. But a pile of chunks is still just a pile of text. If a user asks, "How many days of sick leave do I get?", the computer must somehow find the one chunk that answers it, and it cannot simply read every chunk each time. The trick is to give every chunk a **meaning address**: a list of numbers, called an **embedding**, that places the chunk on an invisible "map of meaning", where chunks about similar ideas sit close together. We then store those addresses in a special database called a **vector store**, which can find the closest chunks to a question in a flash. In this lesson, you will learn what embeddings are and how to compare them, how to build and plug in an embedding model, how to store chunks in FAISS and Chroma, how to search with metadata filters, and how retrievers hand the best chunks to your AI. By the end, you will have a complete "split → embed → store → retrieve" pipeline that is ready to connect to a language model.

## What You Will Learn

- Explain what an **embedding** is and why similar meanings give similar numbers.
- Measure closeness with **cosine similarity**, **dot product**, and **Euclidean distance**.
- Use the LangChain **`Embeddings`** interface (`embed_query` and `embed_documents`), and build your own.
- Pick a real embedding model and avoid the classic "mismatched model" mistake.
- Store chunks in a **vector store** (FAISS and Chroma), search them, and **filter by metadata**.
- Turn a vector store into a **retriever**, and use **MMR** to avoid repetitive results.
- See how **chunk size** from Lesson 2 changes what retrieval finds.
- Build a mini RAG retrieval pipeline that prepares a prompt for an LLM.

## Map of This Lesson

- 🗺️ **Foundations:** Why Do We Need Embeddings, Measuring Similarity
- 🧰 **Preparation:** Setup and Installation, The Embeddings Interface, Real Embedding Models
- 🧱 **Building Blocks:** From Chunks to Vectors, What Is a Vector Store, FAISS, Chroma
- 🔎 **Retrieval:** Retrievers and MMR, How Chunk Size Affects Retrieval
- 🧩 **Wrap-up:** Common Mistakes and Troubleshooting, Summary
- 🏋️ **Practice:** Exercises and Solutions

## Why Do We Need Embeddings?

### 📖 The Story

Captain Luna ran a **floating library on a ship**. Her shelves held thousands of notes, and sailors kept asking her questions. At first she arranged the notes **alphabetically**. But when a sailor asked about "tiny baby cats", the alphabetical shelf found nothing, because the note was titled *"Kitten care"*. Different words, same idea!

So Luna drew a **treasure map of meaning** on the cabin wall. Notes about *cats* and *kittens* went close together. Notes about *dogs* went a little farther away. Notes about *trucks* and *cars* went to the opposite corner of the map. To find an answer, she no longer searched for **matching words**. She marked where the question landed on the map and grabbed the notes **nearest** to that spot.

### 💡 The Explanation

An **embedding** is a list of numbers (a **vector**) that acts as the **coordinates** of a piece of text on that map of meaning. Texts with similar meanings get **similar vectors**, even if they use different words.

- A map on paper has **2 numbers** per spot (left-right, up-down).
- A real embedding has **hundreds or thousands** of numbers (for example 384 or 1536), which lets it capture many shades of meaning at once.
- The number of values in each vector is the **dimension**. All vectors from the same model have the same dimension.

The code below uses a hand-made 3-number "map" (animal-ness, smallness, vehicle-ness) so you can **see** closeness with your own eyes. These are made-up numbers, not a real model.

### 💻 The Code

```python
import numpy as np

# A hand-made map of meaning: [animal-ness, smallness, vehicle-ness]
vectors = {
    "cat":    [0.9, 0.80, 0.00],
    "kitten": [0.9, 0.95, 0.00],
    "dog":    [0.9, 0.50, 0.00],
    "car":    [0.0, 0.40, 0.95],
    "truck":  [0.0, 0.10, 0.95],
}

def cosine(a, b):
    a, b = np.array(a), np.array(b)
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

# Which words are closest in meaning to "kitten"?
for word, vec in vectors.items():
    if word != "kitten":
        print(f"kitten vs {word:6} -> similarity {cosine(vectors['kitten'], vec):.3f}")

# Output:
# kitten vs cat    -> similarity 0.996
# kitten vs dog    -> similarity 0.954
# kitten vs car    -> similarity 0.282
# kitten vs truck  -> similarity 0.076
# Cats and dogs are close to "kitten"; vehicles are far away. That is meaning as geometry.
```

## Measuring Similarity

### 📖 The Story

Two explorers, Ravi and Mia, stood on the deck of Luna's ship. Luna asked, "How **similar** are your two paths?" Ravi pointed out that they both walked **in the same direction**, even though Mia walked twice as far. Luna said: "If we care about **direction**, you are identical. If we care about **how far apart your end points are**, you are not." Different questions give different rulers.

### 💡 The Explanation

Three common ways to compare two vectors:

| Measure | What it looks at | Range | Bigger means |
|---|---|---|---|
| **Cosine similarity** | The **angle** (direction) between vectors | -1 to 1 | More similar |
| **Dot product** | Direction **and** length | any number | More similar |
| **Euclidean distance** (L2) | Straight-line **distance** between end points | 0 and up | **Less** similar |

Important points:

- **Cosine similarity** is the most popular for text, because it ignores how long the vectors are.
- If all vectors are **normalised** (scaled to length 1), then dot product and cosine similarity give the **same ranking**.
- Euclidean distance works the opposite way: **smaller number = closer**. Many vector stores report distance, not similarity, so always check which one you are looking at.

### 💻 The Code

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 4, 6])      # same direction as a, but twice as long
c = np.array([-1, -2, -3])   # exactly the opposite direction

def cosine(x, y):
    return float(x @ y / (np.linalg.norm(x) * np.linalg.norm(y)))

print("Cosine  a vs b:", cosine(a, b))      # same direction
print("Cosine  a vs c:", cosine(a, c))      # opposite direction
print("Dot     a . b :", int(a @ b))        # grows with length
print("Dot     a . c :", int(a @ c))
print("Euclid  a to b:", round(float(np.linalg.norm(a - b)), 3))   # they are NOT at the same spot

# Output:
# Cosine  a vs b: 1.0
# Cosine  a vs c: -1.0
# Dot     a . b : 28
# Dot     a . c : -14
# Euclid  a to b: 3.742
# Cosine says a and b are identical in direction, while Euclidean distance says they are
# 3.742 apart. Same vectors, different rulers.
```

## Setup and Installation

### 📖 The Story

Before sailing, Captain Luna checks her ship: ropes, sails, and a compass. For our voyage, the "ropes and sails" are the libraries, and the "cargo" is a small sample company handbook that we will search throughout this lesson.

### 💡 The Explanation

You will use:

- `langchain-core`: the `Embeddings` interface and the `Document` object.
- `langchain-community`: the **FAISS** vector store (a fast similarity search library from Meta).
- `langchain-chroma`: the **Chroma** vector store (a database that can save to disk).
- `langchain-text-splitters`: the splitters from Lesson 2.
- `numpy`: number crunching.
- Optional: `langchain-huggingface` and `sentence-transformers` for a real embedding model.

This lesson was tested with `langchain-core` 1.8, `langchain-community` 0.4, and `faiss-cpu` 1.16. Newer or slightly older versions should work, but if something fails, check the package's changelog.

The block below installs the libraries and defines two shared pieces of cargo: the `companypolicies` text from Lesson 2, and `policy_docs`, six short `Document` objects with a `topic` label in their metadata.

### 💻 The Code

```python
%%capture
!pip install langchain-core langchain-community langchain-text-splitters
!pip install faiss-cpu langchain-chroma numpy
# Optional, only for the real-model section:
# !pip install langchain-huggingface sentence-transformers

from langchain_core.documents import Document

# ---- Sample text from Lesson 2 ----
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

# ---- Six ready-made chunks with a topic label ----
policy_docs = [
    Document(page_content="Employees may work remotely up to three days per week with manager approval.", metadata={"topic": "remote"}),
    Document(page_content="Remote workers must be available during core hours, from 10 AM to 3 PM.", metadata={"topic": "remote"}),
    Document(page_content="Full-time employees receive 20 days of paid annual leave per year.", metadata={"topic": "leave"}),
    Document(page_content="Sick leave is granted for up to 10 days per year and may require a doctor's note.", metadata={"topic": "leave"}),
    Document(page_content="Passwords must be at least 12 characters long and changed every 90 days.", metadata={"topic": "security"}),
    Document(page_content="Lost or stolen devices must be reported to the IT team within 24 hours.", metadata={"topic": "security"}),
]

print(len(companypolicies), "characters,", len(policy_docs), "documents")
# Output: 927 characters, 6 documents
```

## The Embeddings Interface

### 📖 The Story

At the ship's harbour, there was a **translator booth**. Anyone could walk up with a note, and the translator would hand back the note's **map coordinates**. The booth had two windows. Window one, **"Question window"**, took one question at a time. Window two, **"Library window"**, took a whole stack of notes at once and returned a stack of coordinates, which was faster.

Different translators worked in the booth over the years. As long as they all used the **same two windows**, the rest of the ship never had to change how it worked.

### 💡 The Explanation

In LangChain, every embedding model follows the same **`Embeddings` interface** with two methods:

| Method | Input | Output | Used for |
|---|---|---|---|
| `embed_query(text)` | one string | one vector (list of floats) | The user's **question** |
| `embed_documents(texts)` | list of strings | list of vectors | Your **chunks** (in batches, faster) |

Because every model has the same two windows, you can swap a cheap model for a stronger one **without rewriting the rest of your code**.

The block below does three things:

1. It builds **`ToyEmbeddings`**, a tiny model of our own. It simply counts which words a text contains, using the first five letters of each word so that "change" and "changed" match. It understands **words**, not true **meaning**, but it is perfect for learning because everything is visible and runs offline.
2. It shows the two windows in action.
3. It shows `DeterministicFakeEmbedding`, a built-in LangChain fake model that returns the **same random vector for the same text**. It is useful for testing code, but its vectors carry **no meaning**.

### 💻 The Code

```python
import re
import numpy as np
from langchain_core.embeddings import Embeddings, DeterministicFakeEmbedding

# Small words we ignore, and a helper that turns text into word-stems
STOP = {"the", "a", "an", "of", "do", "i", "how", "many", "must", "is", "to", "get", "my",
        "often", "for", "and", "in", "at", "be", "by", "or", "are", "on", "with", "any",
        "may", "per", "up", "can", "all", "after", "should", "what", "does", "it"}

def words(text):
    return [w[:5] for w in re.findall(r"[a-z0-9']+", text.lower()) if w not in STOP]

class ToyEmbeddings(Embeddings):
    """A tiny embedding model: one number per known word, then scaled to length 1."""

    def __init__(self, corpus):
        vocab = sorted({w for text in corpus for w in words(text)})
        self.index = {w: i for i, w in enumerate(vocab)}      # word -> position

    def _embed(self, text):
        vec = np.zeros(len(self.index))
        for w in words(text):
            if w in self.index:
                vec[self.index[w]] += 1
        norm = np.linalg.norm(vec)
        return (vec / norm).tolist() if norm else vec.tolist()

    def embed_documents(self, texts):          # Library window
        return [self._embed(t) for t in texts]

    def embed_query(self, text):               # Question window
        return self._embed(text)

# ---------- The two windows ----------
mini_corpus = ["Cats purr and sleep.", "Dogs bark at strangers.", "Birds sing every morning."]
toy = ToyEmbeddings(mini_corpus)

print("Dimension (vocabulary size):", len(toy.index))
print("Query vector (first 6 values):", toy.embed_query("Cats purr")[:6])

doc_vectors = toy.embed_documents(mini_corpus)
print("Documents:", len(doc_vectors), "vectors, each of length", len(doc_vectors[0]))

# ---------- A built-in fake model, for testing code ----------
fake = DeterministicFakeEmbedding(size=6)
v1 = fake.embed_query("hello")
v2 = fake.embed_query("hello")
print("Fake vector length:", len(v1), "| same text, same vector:", v1 == v2,
      "| different text, same vector:", fake.embed_query("bye") == v1)

# Output:
# Dimension (vocabulary size): 10
# Query vector (first 6 values): [0.0, 0.0, 0.7071067811865475, 0.0, 0.0, 0.0]
# Documents: 3 vectors, each of length 10
# Fake vector length: 6 | same text, same vector: True | different text, same vector: False
```

## Real Embedding Models

### 📖 The Story

One day, the harbour translator got tired of counting words. Captain Luna hired a **world-famous translator** who had read millions of books. This new translator knew that *"kitten"*, *"baby cat"*, and *"young feline"* all mean nearly the same thing, even though they share no words. The answers got much better, but the translator charged a fee, or needed a bigger desk (a computer with more memory).

There was also a **golden rule** in the harbour: *the same translator must handle both the library notes and the questions.* If notes are translated by one person and questions by another, the coordinates live on two different maps, and nothing lines up.

### 💡 The Explanation

Real embedding models are neural networks trained on huge amounts of text. They capture **meaning**, not just words. Popular choices:

| Model (example) | Where it runs | Dimension | Notes |
|---|---|---|---|
| `sentence-transformers/all-MiniLM-L6-v2` | Your own computer (free) | 384 | Small, fast, great for learning |
| `BAAI/bge-small-en-v1.5` | Your own computer (free) | 384 | Strong small English model |
| `text-embedding-3-small` (OpenAI) | Cloud API (paid, needs key) | 1536 | Good quality, easy to use |
| `text-embedding-3-large` (OpenAI) | Cloud API (paid, needs key) | 3072 | Higher quality, bigger vectors |

How to choose:

- **Quality vs. cost vs. privacy.** Local models keep your data on your machine. API models are often stronger but send text to a provider.
- **Language.** If your documents are not English (for example Urdu or Arabic), pick a **multilingual** model.
- **Dimension.** Bigger vectors cost more storage and search time.
- **Golden rule:** use the **same model** to embed your chunks and your questions. If you change the model, you must **re-embed everything**.

> The code below needs `langchain-huggingface` and `sentence-transformers` installed and an internet connection the first time, to download the model. It is not run in this lesson's other examples, so no output is shown. Use it when you are ready for real semantic search.

### 💻 The Code

```python
# Optional: a real, free embedding model that runs on your own computer
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

query_vector = embeddings.embed_query("How many days of sick leave do I get?")
print("Dimension:", len(query_vector))          # expected: 384 for this model

chunk_vectors = embeddings.embed_documents([
    "Sick leave is granted for up to 10 days per year.",
    "Passwords must be changed every 90 days.",
])
print("Vectors created:", len(chunk_vectors))   # expected: 2

# The rest of this lesson works unchanged with this model:
# just replace ToyEmbeddings(...) with `embeddings` in the later code blocks.

# Cloud alternative (needs an API key, shown only as a pattern):
# from langchain_openai import OpenAIEmbeddings
# embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
```

## From Chunks to Vectors

### 📖 The Story

Luna's crew had a long scroll, the company handbook. First they **cut it into cards** (Lesson 2). Then the translator wrote the **map coordinates** on the back of each card. Finally, a sailor asked a question, the translator wrote coordinates for the question too, and Luna **measured which cards were closest**. No magic, only cutting, labelling, and measuring.

### 💡 The Explanation

This is the heart of RAG retrieval, done **by hand** so you can see every step:

1. **Split** the document into chunks (Lesson 2).
2. **Embed** every chunk to get a matrix: one row per chunk, one column per dimension.
3. **Embed** the question to get one vector.
4. **Compare** the question with every chunk and keep the closest ones.

Because our vectors have length 1, the dot product equals the cosine similarity, so `matrix @ query_vector` gives every similarity score in one line. This block uses `ToyEmbeddings` from the Embeddings Interface section and `companypolicies` from the Setup section.

### 💻 The Code

```python
import numpy as np
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step 1: split
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.split_text(companypolicies)

# Step 2: embed all chunks (the model learns its vocabulary from the chunks)
model = ToyEmbeddings(chunks)
matrix = np.array(model.embed_documents(chunks))
print("Matrix shape (chunks x dimensions):", matrix.shape)

# Step 3: embed the question
question = "How many days of sick leave do I get?"
query_vector = np.array(model.embed_query(question))

# Step 4: compare (dot product of unit vectors = cosine similarity) and keep the top 2
scores = matrix @ query_vector
for i in np.argsort(-scores)[:2]:
    print(f"chunk {i} | score {scores[i]:.3f} | {chunks[i][:70]!r}")

# Output:
# Matrix shape (chunks x dimensions): (8, 83)
# chunk 4 | score 0.612 | '3. Leave Policy\nFull-time employees receive 20 days of paid annual lea'
# chunk 5 | score 0.218 | 'Parental leave is available to all employees after six months of servi'
# The Leave Policy chunk wins, because it contains the sick-leave sentence.
```

## What Is a Vector Store?

### 📖 The Story

Searching Luna's cards by measuring **every card, every time**, worked for 8 cards. But the ship's library grew to **one million cards**, and each question took all night. So Luna built a **smart cabinet**: cards were stored by **neighbourhood on the map**, so to find the nearest cards she only had to open a few drawers instead of all of them. The cabinet also remembered each card's **label** (its source and topic), and could save itself to a notebook so nothing was lost when the ship docked.

### 💡 The Explanation

A **vector store** (or vector database) is that smart cabinet. It does four jobs:

1. **Stores** vectors together with the original text and **metadata**.
2. **Searches** quickly for the vectors closest to a query vector (called **similarity search** or nearest-neighbour search).
3. **Filters** by metadata (for example, only chunks with `topic = leave`).
4. **Persists** data to disk, in many stores.

| Vector store | Style | Good for |
|---|---|---|
| **FAISS** | A library (runs in your program, in memory) | Fast experiments and small to medium data |
| **Chroma** | A lightweight database (saves to disk) | Prototypes and local apps |
| Others (Pinecone, Weaviate, Qdrant, pgvector, and more) | Servers or cloud services | Large production systems |

LangChain gives all of them the same methods, such as `from_documents`, `similarity_search`, and `as_retriever`, so what you learn here transfers.

To prove that a vector store is not magic, the block below builds a **tiny one from scratch** in about 15 lines. It uses `ToyEmbeddings` from the Embeddings Interface section.

### 💻 The Code

```python
import numpy as np

class TinyVectorStore:
    """A vector store in 15 lines: it stores texts and vectors, and finds the closest ones."""

    def __init__(self, embedding):
        self.embedding = embedding
        self.texts = []
        self.vectors = []

    def add_texts(self, texts):
        self.texts += texts
        self.vectors += self.embedding.embed_documents(texts)

    def search(self, query, k=2):
        q = np.array(self.embedding.embed_query(query))
        scores = np.array(self.vectors) @ q
        best = np.argsort(-scores)[:k]
        return [(self.texts[i], round(float(scores[i]), 3)) for i in best]

texts = [
    "Sick leave is granted for up to 10 days per year.",
    "Passwords must be changed every 90 days.",
    "Remote workers must be available from 10 AM to 3 PM.",
]

store = TinyVectorStore(ToyEmbeddings(texts))
store.add_texts(texts)
print(store.search("how many sick days", k=2))

# Output:
# [('Sick leave is granted for up to 10 days per year.', 0.577),
#  ('Passwords must be changed every 90 days.', 0.316)]
# Real vector stores do the same job, but with clever indexes that skip most of the cabinet.
```

## FAISS Vector Store

### 📖 The Story

Luna's friend Kai ran the **speed-reading desk**. He kept the whole map **in his head** (in memory), so he answered questions in a flash. His only weakness: if the lights went out, he forgot everything, unless he wrote it into his notebook first (`save_local`) and read it back later (`load_local`).

### 💡 The Explanation

**FAISS** (Facebook AI Similarity Search) is a fast in-memory library. In LangChain you use it through `langchain_community.vectorstores.FAISS`.

Key methods:

- `FAISS.from_documents(docs, embedding)`: embed documents and build the store.
- `similarity_search(query, k=2)`: return the `k` closest **Documents**.
- `similarity_search_with_score(query, k=2)`: also return a **score**. For FAISS the score is a **distance**, so **lower means closer** (the opposite of similarity).
- `add_documents([...])`: add more chunks later.
- `save_local(folder)` and `FAISS.load_local(folder, embedding, ...)`: save and reload. Loading needs `allow_dangerous_deserialization=True`, because the saved file can run code when loaded. **Only load files that you created yourself.**
- `filter={"topic": "leave"}`: search only chunks whose metadata matches.

This block uses `ToyEmbeddings` and `policy_docs` from earlier sections.

### 💻 The Code

```python
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

embedding = ToyEmbeddings([d.page_content for d in policy_docs])

# ---------- Build the store ----------
store = FAISS.from_documents(policy_docs, embedding)

# ---------- Plain similarity search ----------
for d in store.similarity_search("How many days of sick leave?", k=2):
    print(d.metadata, "|", d.page_content[:50])

# ---------- Search with scores (these are DISTANCES: lower = closer) ----------
for d, score in store.similarity_search_with_score("How many days of sick leave?", k=3):
    print(round(float(score), 3), d.metadata)

# ---------- Add a new chunk later ----------
print("Before:", store.index.ntotal)
store.add_documents([Document(page_content="Parental leave is available after six months of service.",
                              metadata={"topic": "leave"})])
print("After :", store.index.ntotal)

# ---------- Save, reload, and search with a metadata filter ----------
store.save_local("faiss_policies")
loaded = FAISS.load_local("faiss_policies", embedding, allow_dangerous_deserialization=True)
print("Reloaded:", loaded.index.ntotal)
for d in loaded.similarity_search("days per year", k=2, filter={"topic": "leave"}):
    print(d.metadata, "|", d.page_content[:40])

# Output:
# {'topic': 'leave'} | Sick leave is granted for up to 10 days per year a
# {'topic': 'leave'} | Full-time employees receive 20 days of paid annual
# 0.845 {'topic': 'leave'}
# 1.27 {'topic': 'leave'}
# 1.592 {'topic': 'remote'}
# Before: 6
# After : 7
# Reloaded: 7
# {'topic': 'leave'} | Sick leave is granted for up to 10 days per year
# {'topic': 'leave'} | Full-time employees receive 20 days of paid annual
# Notice the scores go UP as results get worse: they are distances.
```

## Chroma Vector Store

### 📖 The Story

Luna's other friend, Nia, ran the **record room**. Unlike Kai, Nia wrote every card into a **sturdy ledger on the shelf** as soon as it arrived. If the lights went out, the ledger was still there in the morning. She could also **count her cards** at any time and look up cards by their label.

### 💡 The Explanation

**Chroma** is a lightweight vector database. Give it a `persist_directory` and it **saves automatically to disk**. In LangChain you use it through the `langchain_chroma` package.

Key points:

- `Chroma.from_documents(docs, embedding, persist_directory=..., collection_name=...)` builds (or opens) a collection.
- A **collection** is a named group of vectors, like a table.
- Search methods are the same as FAISS: `similarity_search`, `similarity_search_with_score`, `as_retriever`, and `filter=`.
- Scores are **distances** here too (lower is closer).
- You can count what is stored with `store._collection.count()`.

This block uses `ToyEmbeddings` and `policy_docs` from earlier sections.

### 💻 The Code

```python
from langchain_chroma import Chroma

embedding = ToyEmbeddings([d.page_content for d in policy_docs])

# Build the collection and save it automatically in the folder "chroma_policies"
chroma_store = Chroma.from_documents(
    policy_docs,
    embedding,
    persist_directory="chroma_policies",
    collection_name="policies",
)

# Plain search
for d in chroma_store.similarity_search("password length", k=1):
    print(d.metadata, "|", d.page_content[:40])

# Search with scores, restricted to the "leave" topic
for d, score in chroma_store.similarity_search_with_score("sick leave", k=2, filter={"topic": "leave"}):
    print(round(float(score), 3), "|", d.page_content[:40])

# How many chunks are stored?
print("Stored chunks:", chroma_store._collection.count())

# Output:
# {'topic': 'security'} | Passwords must be at least 12 characters
# 1.057 | Sick leave is granted for up to 10 days
# 1.553 | Full-time employees receive 20 days of p
# Stored chunks: 6
# Next time your program starts, open the same folder and collection name to reuse the data
# without embedding everything again.
```

## Retrievers and MMR

### 📖 The Story

Luna asked a helper, "Bring me the **3 best notes** about sick leave." The helper returned three notes, but they were all **almost the same sentence** written three ways. Luna sighed: "I wanted *useful variety*, not three copies!"

So she changed her request: "Bring me notes that are **relevant**, but also **different from each other**." This is like picking guests for a party: you want people who fit the theme, but you do not want three guests with identical stories.

### 💡 The Explanation

A **retriever** is a simple wrapper with one job: *given a question, return relevant Documents*. Every vector store can create one with `as_retriever()`, and you call it with `retriever.invoke("question")`. Retrievers plug straight into LangChain chains.

| Setting | Meaning |
|---|---|
| `search_type="similarity"` (default) | Return the `k` closest chunks |
| `search_type="mmr"` | **Maximal Marginal Relevance**: pick chunks that are relevant **and** different from those already picked |
| `search_kwargs={"k": 3}` | How many chunks to return |
| `fetch_k` (MMR) | How many candidates to consider before choosing the diverse `k` |
| `lambda_mult` (MMR) | `1` = only relevance, `0` = only diversity. Lower values give more variety |

MMR helps when your documents contain many repeated or overlapping chunks (a side effect of `chunk_overlap`). In the example below, the first three similarity results are all about sick leave, but MMR with a low `lambda_mult` deliberately picks different chunks. With our toy model, the "different" chunks can be only loosely related, so **do not set the diversity too low in real projects**. Try values between 0.5 and 0.7 first.

### 💻 The Code

```python
from langchain_community.vectorstores import FAISS

texts = [
    "Sick leave is granted for up to 10 days per year.",
    "Employees get up to 10 days of sick leave each year.",
    "Sick leave needs a doctor's note after 3 days.",
    "Annual leave is 20 days per year for full-time staff.",
    "Passwords must be changed every 90 days.",
]
store = FAISS.from_texts(texts, ToyEmbeddings(texts))
question = "sick leave days per year"

# ---------- Plain similarity retriever ----------
similarity = store.as_retriever(search_kwargs={"k": 3})
print("SIMILARITY")
for d in similarity.invoke(question):
    print("  ", d.page_content)

# ---------- MMR retriever: relevant AND different ----------
mmr = store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "fetch_k": 5, "lambda_mult": 0.3},
)
print("MMR")
for d in mmr.invoke(question):
    print("  ", d.page_content)

# Output:
# SIMILARITY
#    Sick leave is granted for up to 10 days per year.
#    Employees get up to 10 days of sick leave each year.
#    Sick leave needs a doctor's note after 3 days.
# MMR
#    Sick leave is granted for up to 10 days per year.
#    Passwords must be changed every 90 days.
#    Annual leave is 20 days per year for full-time staff.
# MMR skipped the near-duplicate sick-leave sentences and picked different chunks.
# (lambda_mult=0.3 is very diverse; the password chunk is only loosely related.)
```

## How Chunk Size Affects Retrieval

### 📖 The Story

Luna ran an experiment with three card sizes. With **tiny cards**, the sick-leave card said exactly what the sailor needed, with no distractions. With **medium cards**, the answer shared a card with *annual leave* rules, so the sailor read a little extra. With **giant cards**, the answer was buried inside a whole page about all leave types. The sailor found it, but it took longer and the page held many other facts.

### 💡 The Explanation

In Lesson 2 you chose `chunk_size`. Now you can **see its effect on retrieval**. The experiment below splits the same handbook with three sizes, builds a store for each, and asks the same question. Look at the **length of the top chunk**: the smaller it is, the more precisely the answer is isolated. But remember that very small chunks may lose context. The best size is a balance, and you should test it on your own questions.

### 💻 The Code

```python
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

question = "How many days of sick leave?"

for size in (100, 200, 400):
    splitter = RecursiveCharacterTextSplitter(chunk_size=size, chunk_overlap=size // 10)
    chunks = splitter.split_text(companypolicies)
    store = FAISS.from_texts(chunks, ToyEmbeddings(chunks))
    top = store.similarity_search(question, k=1)[0].page_content
    print(f"chunk_size={size:3} | chunks={len(chunks):2} | top chunk length={len(top):3} | {top[:55]!r}")

# Output:
# chunk_size=100 | chunks=13 | top chunk length= 81 | 'Sick leave is granted for up to 10 days per year and may '
# chunk_size=200 | chunks= 8 | top chunk length=164 | '3. Leave Policy\nFull-time employees receive 20 days of p'
# chunk_size=400 | chunks= 4 | top chunk length=238 | '3. Leave Policy\nFull-time employees receive 20 days of p'
# With 100, the top chunk is exactly the sick-leave sentence.
# With 200 and 400, the answer is mixed with annual-leave and parental-leave text.
```

## Common Mistakes and Troubleshooting

### 📖 The Story

Luna kept a **logbook of shipwrecks**, a record of every time the ship went wrong, so the next voyage was safer. Three wrecks happened again and again: sailors used **two different translators** for notes and questions, the record room filled up with **duplicate cards** after every restart, and apprentices read the speed desk's scores **backwards**.

### 💡 The Explanation

| Problem | Cause | Fix |
|---|---|---|
| Error or nonsense results when searching | The chunks were embedded with **one model** and the question with **another** (different dimension or different map) | Use the **same embedding model** for indexing and querying. Re-embed everything if you change the model |
| Duplicate chunks pile up in Chroma after each run | `from_documents` adds new entries every time it runs | Give each chunk a fixed **`ids=[...]`**, or open the existing collection instead of rebuilding it |
| "Higher score is better" assumption fails | FAISS and Chroma return **distances** by default (lower is closer) | Check the docs for your store, or use relevance-score methods |
| Retrieval finds the wrong topic | Chunks too big or too small, or a weak embedding model | Test several `chunk_size` values. Try a stronger model |
| Many near-identical results | Heavy `chunk_overlap` or repeated text | Use MMR, or reduce the overlap |
| `load_local` raises a safety error | FAISS needs explicit permission to load pickled files | Pass `allow_dangerous_deserialization=True`, **only for files you created yourself** |
| Header-only or tiny chunks pollute the results | Markdown header splitting can create chunks with only a title | Drop chunks shorter than a few dozen characters before indexing |
| Search is slow on huge data | Exact search over many vectors | Use a store with an approximate index, or a server-based vector database |

The block below reproduces three of these wrecks on purpose, with their fixes.

### 💻 The Code

```python
import shutil
from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma
from langchain_core.documents import Document

texts = [
    "Sick leave is granted for up to 10 days per year.",
    "Passwords must be changed every 90 days.",
    "Remote workers must be available from 10 AM to 3 PM.",
]
docs = [Document(page_content=t, metadata={"i": i}) for i, t in enumerate(texts)]
embedding = ToyEmbeddings(texts)

# ---------- Wreck 1: a different embedding model for the question ----------
store = FAISS.from_documents(docs, embedding)
other_model = ToyEmbeddings(["a completely different vocabulary here"])   # different dimension
try:
    store.similarity_search_by_vector(other_model.embed_query("different"), k=1)
except Exception as error:
    print("Wreck 1:", type(error).__name__)
# Output: Wreck 1: AssertionError
# The vector sizes did not match. Always use the same model for chunks and questions.

# ---------- Wreck 2: duplicates after running the build twice ----------
shutil.rmtree("chroma_dup", ignore_errors=True)
for _ in range(2):
    dup = Chroma.from_documents(docs, embedding, persist_directory="chroma_dup", collection_name="dup")
print("Without ids:", dup._collection.count())
# Output: Without ids: 6   (3 chunks were added twice)

shutil.rmtree("chroma_ids", ignore_errors=True)
for _ in range(2):
    fixed = Chroma.from_documents(docs, embedding, ids=["0", "1", "2"],
                                  persist_directory="chroma_ids", collection_name="ids")
print("With ids   :", fixed._collection.count())
# Output: With ids   : 3   (same ids replace the old entries)

# ---------- Wreck 3: reading scores backwards ----------
results = store.similarity_search_with_score("sick days", k=3)
print("Scores:", [round(float(score), 2) for _, score in results])
# Output: Scores: [0.85, 1.37, 2.0]
# The FIRST result has the SMALLEST number. These are distances: lower is closer.
```

## Summary

### 📖 The Story

When the voyage ended, Luna gathered her crew and read out the lessons from the logbook: *give every note a map address, always use the same translator, store the addresses in a smart cabinet, ask for relevant and varied notes, and keep the cards the right size.* The sailors cheered, and every question after that found its answer on the first try.

### 💡 The Explanation

- An **embedding** is a vector that places text on a map of meaning. Similar meanings give similar vectors.
- Compare vectors with **cosine similarity** (direction), **dot product**, or **Euclidean distance** (lower is closer).
- Every LangChain embedding model has `embed_query` (one question) and `embed_documents` (many chunks).
- Always use the **same embedding model** for your chunks and your questions.
- A **vector store** stores vectors, text, and metadata, and finds the nearest chunks quickly. **FAISS** is fast and in memory. **Chroma** saves to disk.
- Search with `similarity_search`, add scores with `similarity_search_with_score` (distance, lower is closer), and narrow results with `filter=`.
- A **retriever** (`as_retriever`) wraps a vector store for chains. Use **MMR** to get relevant but varied results.
- `chunk_size` from Lesson 2 directly changes retrieval quality. Test it on real questions.
- The full pipeline is **load → split → embed → store → retrieve → (generate)**.

### 💻 The Code

A compact cheat sheet that runs the whole pipeline in a few lines. It uses `ToyEmbeddings` from the Embeddings Interface section.

```python
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = ("Sick leave is granted for up to 10 days per year.\n\n"
        "Passwords must be changed every 90 days.\n\n"
        "Remote workers must be available from 10 AM to 3 PM.")

chunks = RecursiveCharacterTextSplitter(chunk_size=60, chunk_overlap=0).split_text(text)   # split
embedding = ToyEmbeddings(chunks)                                                           # embed model
store = FAISS.from_texts(chunks, embedding)                                                 # embed + store
retriever = store.as_retriever(search_kwargs={"k": 1})                                      # retrieve

print(retriever.invoke("password rules")[0].page_content)

# Output: Passwords must be changed every 90 days.
```

## Exercises

### Exercise 1: The Compass Story (Cosine Similarity)

📖 **Story:** Three explorers leave the ship at the same time. **Ana** walks due east, **Ben** walks mostly east but slightly north, and **Cleo** walks due north. Captain Luna wants to know **how similar their directions are**.

Their directions are the vectors `ana = [1.0, 0.0]`, `ben = [0.8, 0.6]`, and `cleo = [0.0, 1.0]`.

**Your task:**

1. Write a `cosine(x, y)` function with NumPy.
2. Compute the similarity for the pairs (Ana, Ben), (Ana, Cleo), and (Ben, Cleo).
3. Which two explorers are the most alike? Which pair has nothing in common (similarity 0)?

### Exercise 2: The Topic Cabinet (FAISS with Metadata Filters)

📖 **Story:** Kai at the speed-reading desk wants to answer questions faster by looking only in the **right drawer**. The drawers are labelled with topics: `remote`, `leave`, and `security`.

**Your task:** using `policy_docs` and `ToyEmbeddings`:

1. Build a FAISS store from `policy_docs`.
2. Search for `"remote work hours"` (no filter) and print the topics of the top 2 results.
3. Search for `"days per year"` with `filter={"topic": "leave"}`, and then with `filter={"topic": "security"}`. How do the results change?
4. Explain in one sentence why filters are useful in a large company handbook.

### Exercise 3 (Capstone): The Robo-Lib Prompt Builder

📖 **Story:** Robo-Lib, the robot librarian from Lesson 2, is ready for its next upgrade. It must now (a) **split** the handbook, (b) **embed and store** the chunks, (c) **retrieve** the best chunks for a question, and (d) **write a prompt** that a language model could answer, quoting its sources.

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

1. Split `handbook_md` in two stages (`MarkdownHeaderTextSplitter` with `strip_headers=False`, then `RecursiveCharacterTextSplitter` with `chunk_size=200`, `chunk_overlap=30`).
2. Remove chunks shorter than 60 characters (header-only chunks), and print how many chunks remain.
3. Build a FAISS store with `ToyEmbeddings`, and create a retriever with `k=2`.
4. Write `build_prompt(question)` that retrieves the chunks and returns a prompt string with numbered context, the section name for each chunk, and the question.
5. Test it with: *"How many days of sick leave do I get?"* and *"What time are remote workers available?"*
6. Reflect: what would you change to make Robo-Lib work for questions that use **different words** from the handbook (for example, "How many sick days am I allowed?" or "Can I work from home?")?

## Solutions

### Solution 1: The Compass Story

**Explanation.** Cosine similarity looks only at the **angle** between the vectors. Ana `[1, 0]` and Ben `[0.8, 0.6]` point in nearly the same direction (similarity 0.8). Ana and Cleo are at a right angle, so they share **nothing** (similarity 0.0). Ben and Cleo are in between (0.6), because Ben leans a little north.

```python
import numpy as np

ana = np.array([1.0, 0.0])
ben = np.array([0.8, 0.6])
cleo = np.array([0.0, 1.0])

def cosine(x, y):
    return float(x @ y / (np.linalg.norm(x) * np.linalg.norm(y)))

print("Ana  vs Ben :", round(cosine(ana, ben), 2))
print("Ana  vs Cleo:", round(cosine(ana, cleo), 2))
print("Ben  vs Cleo:", round(cosine(ben, cleo), 2))

# Output:
# Ana  vs Ben : 0.8
# Ana  vs Cleo: 0.0
# Ben  vs Cleo: 0.6
# Most alike: Ana and Ben. Nothing in common: Ana and Cleo (a right angle).
```

### Solution 2: The Topic Cabinet

**Explanation.** Without a filter, the question about remote work finds the two `remote` chunks. With a filter, the search is **restricted to one topic**. The same question, "days per year", returns leave chunks under `leave` but security chunks under `security`, because the filter allows only that drawer, even when the match is weak. **Why filters matter:** in a large handbook, a filter stops the search from wandering into unrelated sections (for example, the wrong department or an outdated year), which makes answers more accurate and faster.

```python
from langchain_community.vectorstores import FAISS

embedding = ToyEmbeddings([d.page_content for d in policy_docs])
store = FAISS.from_documents(policy_docs, embedding)

# No filter
results = store.similarity_search("remote work hours", k=2)
print("remote work hours | no filter   :", [d.metadata["topic"] for d in results])

# Filter: leave drawer
results = store.similarity_search("days per year", k=2, filter={"topic": "leave"})
print("days per year     | topic=leave :", [d.page_content[:22] for d in results])

# Filter: security drawer
results = store.similarity_search("days per year", k=2, filter={"topic": "security"})
print("days per year     | topic=security:", [d.page_content[:22] for d in results])

# Output:
# remote work hours | no filter   : ['remote', 'remote']
# days per year     | topic=leave : ['Sick leave is granted ', 'Full-time employees re']
# days per year     | topic=security: ['Passwords must be at l', 'Lost or stolen devices']
```

### Solution 3 (Capstone): The Robo-Lib Prompt Builder

**Explanation.** Stage 1 cuts the handbook at its headers, and Stage 2 cuts any chunk that is longer than 200 characters. We then **drop tiny, header-only chunks**, because they hold no answer and would only add noise. Next we embed the chunks, store them in FAISS, and turn the store into a retriever. `build_prompt` places the retrieved chunks into a template that tells the language model to answer **only from the context**, which reduces made-up answers. Each chunk shows its section name (from the metadata), so the model, and the user, can see where the information came from.

Two things to notice in the output:

- For the sick-leave question, the **Sick Leave** chunk is ranked first.
- The second chunk is the **Annual Leave** chunk, which also contains the header `## Leave Policy`. That is normal: retrieval returns the *closest* chunks, not only perfect ones.

```python
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

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

# ---------- Task 1: two-stage split ----------
headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
stage1 = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on,
                                    strip_headers=False).split_text(handbook_md)
docs = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30).split_documents(stage1)

# ---------- Task 2: drop tiny header-only chunks ----------
docs = [d for d in docs if len(d.page_content) > 60]
print("Chunks kept:", len(docs))

# ---------- Task 3: embed, store, retrieve ----------
embedding = ToyEmbeddings([d.page_content for d in docs])
store = FAISS.from_documents(docs, embedding)
retriever = store.as_retriever(search_kwargs={"k": 2})

# ---------- Task 4: build the prompt ----------
def build_prompt(question):
    hits = retriever.invoke(question)
    context = "\n\n".join(
        f"[{i}] ({h.metadata.get('Header 3') or h.metadata.get('Header 2')}) {h.page_content}"
        for i, h in enumerate(hits, start=1)
    )
    return (f"Answer using ONLY the context.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {question}\nAnswer:")

# ---------- Task 5: test ----------
print(build_prompt("How many days of sick leave do I get?"))
print("=" * 40)
print(build_prompt("What time are remote workers available?"))

# Output:
# Chunks kept: 4
# Answer using ONLY the context.
#
# Context:
# [1] (Sick Leave) ### Sick Leave
# Sick leave is granted for up to 10 days per year and may require a doctor's note.
#
# [2] (Annual Leave) ## Leave Policy
# ### Annual Leave
# Full-time employees receive 20 days of paid annual leave per year. Leave requests should be submitted at least two weeks in advance.
#
# Question: How many days of sick leave do I get?
# Answer:
# ========================================
# For the second question, context [1] is the (Remote Work) chunk that contains
# "Remote workers must be available during core hours, from 10 AM to 3 PM."
# (the exact text of the second chunk can differ slightly between versions).
```

**Task 6: Reflection.** `ToyEmbeddings` only matches **words**, so a question like "Can I work from home?" or "How many sick days am I allowed?" can fail when the handbook says "work remotely" or "sick leave". The fix is to switch to a **real embedding model**, such as `HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")`, which places "sick days" and "sick leave" close together on the map of meaning. Because every LangChain embedding model has the same interface, you change **one line**: replace `ToyEmbeddings(...)` with the real model. Remember the golden rule: use the same model for chunks and questions, and **re-embed all chunks** after the switch.

### Bonus Challenges

1. Swap `ToyEmbeddings` for `HuggingFaceEmbeddings` and compare which chunks are retrieved for "Can I work from home?"
2. Store the capstone chunks in **Chroma** with fixed `ids`, restart your notebook, reopen the collection, and search again without re-embedding.
3. Add a **MMR retriever** to Robo-Lib and compare its prompts with the plain similarity ones.
4. Connect the prompt from `build_prompt` to a real language model and see whether the answers stay inside the context.

*End of Lesson 3. Next up: connecting a language model to your retriever to build a complete RAG question-answering chain.*
