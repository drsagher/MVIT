# Lesson 2: Apply Text Splitting Techniques to Enhance Model Responsiveness

## Introduction

Imagine handing someone a 500-page book and asking them a question about one small rule on page 312. They would not read every page again. They would flip to the right chapter and read only the part that matters. AI models work in a very similar way. They can only read a limited amount of text at one time, so large documents such as policy handbooks, websites, or code files must first be cut into smaller, meaningful pieces called **chunks**. This cutting step is called **text splitting**, and it is one of the most important steps in building a Retrieval-Augmented Generation (RAG) system. If the pieces are cut well, the system finds the right information quickly and gives accurate answers. If they are cut badly, with sentences broken in half or many topics mixed together, even a powerful model will give weak or wrong responses. In this lesson, you will learn how text splitting works, why settings like `chunk_size` and `chunk_overlap` matter, and how to use LangChain's splitters for plain text, code, Markdown, HTML, and JSON. By the end, you will be able to choose the right splitter for any document and prepare your data so that your AI responds with speed and precision.

## What You Will Learn

- Explain **why** text splitting is needed and how it affects RAG quality.
- Use the key parameters: `separator`, `chunk_size`, `chunk_overlap`, `length_function`.
- Create and read LangChain `Document` objects, including metadata.
- Use `CharacterTextSplitter`, `RecursiveCharacterTextSplitter`, code splitters, `MarkdownHeaderTextSplitter`, `HTMLHeaderTextSplitter`, `HTMLSectionSplitter`, `RecursiveJsonSplitter`, and token-based splitters.
- Combine a structure-aware splitter with a size-based splitter.
- Choose sensible chunk sizes and pick the right splitter for each file type.

## Map of This Lesson

- 🍕 **Foundations:** Why Do We Split Text, Where Splitting Fits in RAG
- 🧰 **Preparation:** Setup and Installation, Key Parameters, The Document Object, Three Ways to Call a Splitter
- ✂️ **The Splitters:** Split by Character, Recursive Split, Split Code, Markdown Headers, HTML, JSON, Tokens
- 🧩 **Putting It Together:** Two-Stage Pipeline, Choosing Sizes, Which Splitter to Use, Troubleshooting, Summary
- 🏋️ **Practice:** Exercises and Solutions

## Why Do We Split Text?

### 📖 The Story

Pip the baker made a **giant pizza** for a party. A hungry guest tried to eat the whole thing in one bite and got stuck. 😅 Pip grabbed a knife and cut the pizza into **slices**. Now every guest could hold a slice, and every slice still tasted like pizza.

But Pip learned something important. If he cut the pizza **right through the middle of a mushroom**, the slice looked messy. If he cut **between the toppings**, each slice looked neat. A good cut follows the natural lines of the pizza.

### 💡 The Explanation

AI models like ChatGPT or Claude have a limited "mouth", called the **context window**. They can only read a certain amount of text at one time. A long document is the giant pizza, and we must slice it first.

| Pizza world | Text world |
|---|---|
| Whole pizza | A long document (a 200-page policy file, a book, a website) |
| A slice | A **chunk** of text |
| Size of a slice | `chunk_size` |
| A little cheese shared between two slices | `chunk_overlap` |
| The knife | The **text splitter** |

A **good splitter** cuts at natural places: paragraphs first, then sentences, then words. That way every chunk **makes sense on its own**.

### 💻 The Code

The code below shows a bad cut (blind, in the middle of a word) next to a good cut (at the end of a sentence).

```python
import re

sentence = "The cat sat on the mat. It was a sunny day."

# Bad cut: blindly cut after 20 characters
bad_cut = [sentence[:20], sentence[20:]]
print("BAD :", bad_cut)

# Good cut: cut right after each full stop
good_cut = re.split(r"(?<=\.)\s", sentence)
print("GOOD:", good_cut)

# Output:
# BAD : ['The cat sat on the m', 'at. It was a sunny day.']
# GOOD: ['The cat sat on the mat.', 'It was a sunny day.']
```

## Where Splitting Fits in RAG

### 📖 The Story

Maya is a student with an exam tomorrow. She does not remember the whole textbook, but she has a clever habit. When a question appears, she **looks up the best pages** in her notes, reads them quickly, and then **writes her answer** using those pages.

Now imagine her notes are one giant, uncut scroll. Finding the right part would take forever. But if her notes are cut into **neat, labelled cards**, she finds the answer in seconds. The quality of her cards decides the quality of her answer.

### 💡 The Explanation

**RAG** stands for **Retrieval-Augmented Generation**. The AI does not know your private documents, so before it answers we **look up** the best pieces and **hand them to the AI** like a cheat sheet.

The full journey is: **Load** the files → **Split** into chunks (**this lesson**) → **Embed** chunks into numbers → **Store** them in a vector database → **Retrieve** the best chunks for a question → **Generate** an answer with the LLM → **Answer** the user.

| If chunks are... | What goes wrong |
|---|---|
| **Too big** | Each chunk mixes many topics, so search gets "blurry". The model also wastes space on irrelevant text. |
| **Too small** | Each chunk loses its meaning ("It was approved by them." Who? What?). |
| **Cut in the wrong place** | An answer is split in half, and retrieval finds only half of it. |
| **Just right** | Each chunk is one clear idea. Search is sharp and answers are accurate. |

**Golden rule:** *Good chunks = good retrieval = good answers.*

### 💻 The Code

This is a tiny, runnable skeleton of the whole journey. The embedding and storing steps are replaced by a simple word-matching search, so you can run it without any API key. (Full RAG systems use embeddings instead.)

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1) LOAD: here we simply use a string instead of a real file
document = (
    "Employees receive 20 days of paid annual leave per year.\n\n"
    "Sick leave is granted for up to 10 days per year.\n\n"
    "Passwords must be changed every 90 days."
)

# 2) SPLIT: the step this whole lesson is about
splitter = RecursiveCharacterTextSplitter(chunk_size=60, chunk_overlap=0)
chunks = splitter.split_text(document)

# 3) EMBED + 4) STORE: skipped, we keep chunks in a plain Python list

# 5) RETRIEVE: pick the chunk that shares the most words with the question
def retrieve(question, chunks):
    q_words = set(question.lower().split())
    return max(chunks, key=lambda c: len(q_words & set(c.lower().split())))

best_chunk = retrieve("How many days of sick leave?", chunks)

# 6) GENERATE: a real system would send best_chunk to an LLM here
print("Chunks:", chunks)
print("Best chunk for the question:", best_chunk)

# Output:
# Chunks: ['Employees receive 20 days of paid annual leave per year.',
#          'Sick leave is granted for up to 10 days per year.',
#          'Passwords must be changed every 90 days.']
# Best chunk for the question: Sick leave is granted for up to 10 days per year.
```

## Setup and Installation

### 📖 The Story

Before Pip the baker can cook, he gathers his tools: a knife, a tray, and an oven. Programmers do the same. We install our libraries first, and we also prepare a small sample document, so that every experiment in this lesson has something to cut.

### 💡 The Explanation

You will use:

- [`langchain`, `langchain-text-splitters`](https://www.langchain.com/): the splitters themselves.
- [`lxml`](https://pypi.org/project/lxml/): needed for splitting HTML.
- `tiktoken` (optional): needed only for token-based splitting.

`%%capture` and `!pip` work in Jupyter or Colab notebooks. In a normal terminal, run `pip install ...` without the `!`.

The original lab used a file called `companypolicies.txt` but never showed how to create it. Below, we define a small sample called `companypolicies` so every example in this lesson is **runnable on its own**. Many later code blocks use this variable, so **run this block first**.

### 💻 The Code

```python
%%capture
!pip install "langchain==0.2.7"
!pip install "langchain-core==0.2.20"
!pip install "langchain-text-splitters==0.2.2"
!pip install "lxml==5.2.2"
!pip install tiktoken        # optional, only for the token section

# ---- Sample document used throughout the lesson ----
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

print(len(companypolicies), "characters")   # Output: 927 characters

# ---- Optional: load your own real file instead ----
# with open("companypolicies.txt", "r", encoding="utf-8") as f:
#     companypolicies = f.read()
```

## Key Parameters Explained

### 📖 The Story

Pip's cutting machine has four dials. The first dial, **Dotted Line**, tells the machine where it likes to cut. The second, **Slice Size**, sets the biggest slice allowed. The third, **Shared Cheese**, makes neighbouring slices share a bit of topping so no flavour is lost at the edge. The fourth, **Ruler Type**, decides whether slices are measured in centimetres or weighed in grams.

One day Pip set the Shared Cheese dial *bigger than* the Slice Size dial. The machine beeped angrily and refused to start. A slice cannot share more cheese than it holds!

### 💡 The Explanation

| Dial | Parameter | What it does |
|---|---|---|
| Dotted Line | `separator` / `separators` | The character(s) where the splitter prefers to cut |
| Slice Size | `chunk_size` | The **maximum** size of one chunk |
| Shared Cheese | `chunk_overlap` | How much of the end of chunk A is repeated at the start of chunk B |
| Ruler Type | `length_function` | How size is measured (`len` = characters; a token counter = tokens) |

**Why overlap helps.** Without overlap, an important sentence can be cut in half: `"... at least 12 char"` | `"acters long and changed ..."`. With overlap, both chunks share the middle part, so whichever chunk is retrieved, the idea survives.

**Facts beginners often miss:**

1. `chunk_size` is a **maximum**, not an exact size. Real chunks are often shorter.
2. `chunk_overlap` must be **smaller** than `chunk_size`, otherwise LangChain raises an error.
3. Splitters first **split on the separator**, then **merge small pieces back together** until the size limit is reached.
4. A single piece that is already bigger than `chunk_size`, and cannot be split further by that separator, is **kept whole** and you get a warning.

### 💻 The Code

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# All four dials in one splitter
splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],  # Dotted Line: try these cuts, in order
    chunk_size=100,                      # Slice Size: max 100 units per chunk
    chunk_overlap=20,                    # Shared Cheese: 20 units shared
    length_function=len,                 # Ruler Type: count characters
)
chunks = splitter.split_text(companypolicies)
print("Chunks created:", len(chunks))
print("Longest chunk :", max(len(c) for c in chunks), "characters")

# Output:
# Chunks created: 13
# Longest chunk : 98 characters   (never above chunk_size)

# What happens when Shared Cheese is bigger than Slice Size?
try:
    RecursiveCharacterTextSplitter(chunk_size=20, chunk_overlap=50)
except ValueError as error:
    print("Error:", error)

# Output:
# Error: Got a larger chunk overlap (50) than chunk size (20), should be smaller.
```

## The Document Object

### 📖 The Story

At the post office, Rosa never throws a letter into the sack bare. She puts every letter in a **box** and sticks a **label** on it: where it came from, what day it arrived, and who sent it. Later, when someone asks "where did this letter come from?", the label gives the answer instantly.

### 💡 The Explanation

In LangChain, every text chunk lives inside a **`Document`** object, the labelled box:

- `page_content` (a `str`): the actual text inside the box.
- `metadata` (a `dict`): the sticky label. It can hold a file name, page number, source, section title, date, and so on.

**Why metadata matters in RAG:** if the AI answers *"Employees get 20 days of leave"*, a good system can also say *"Source: Company Policies, section 3"*. That is possible only because the chunk carried its label with it.

### 💻 The Code

```python
from langchain_core.documents import Document

doc = Document(
    page_content="""Python is an interpreted high-level general-purpose programming language.
                    Python's design philosophy emphasizes code readability with its notable use of significant indentation.""",
    metadata={
        "my_document_id": 234234,
        "my_document_source": "About Python",
        "my_document_create_time": 1680013019,
    },
)

print(doc.page_content)                    # the text inside the box
print(doc.metadata)                        # the whole label
print(doc.metadata["my_document_source"])  # one item from the label

# Output (last line): About Python
```

## Three Ways to Call a Splitter

### 📖 The Story

Pip's cutting machine has three buttons. Button one takes a **plain pizza** and returns **plain slices**. Button two takes a plain pizza but also lets you **stick a label** on every slice. Button three takes a pizza that **already has a label** and makes sure every slice **inherits that label**.

### 💡 The Explanation

| Method | Input | Output | Use it when |
|---|---|---|---|
| `split_text(text)` | one string | list of **strings** | You just want raw text pieces |
| `create_documents([text], metadatas=[...])` | list of strings | list of **Document** objects | You have raw strings and want to attach metadata |
| `split_documents(docs)` | list of **Document** objects | list of **Document** objects | You already have `Document`s (for example from a loader) and want to keep their metadata |

### 💻 The Code

This block uses `companypolicies` from the Setup section.

```python
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=60, chunk_overlap=10)

# Button 1: strings in, strings out
strings = splitter.split_text(companypolicies)
print(type(strings[0]))             # <class 'str'>

# Button 2: strings in, Documents out (you add the label)
docs = splitter.create_documents(
    [companypolicies],
    metadatas=[{"source": "Company Policies"}],
)
print(type(docs[0]))                # Document
print(docs[0].metadata)             # {'source': 'Company Policies'}

# Button 3: Documents in, Documents out (labels are copied to every chunk)
original = [Document(page_content=companypolicies, metadata={"source": "Company Policies"})]
chunked = splitter.split_documents(original)
print(len(chunked), chunked[0].metadata)
```

## Split by Character

### 📖 The Story

Tom the tailor owns a pair of scissors that can cut **only along one kind of line**. If you tell him "cut at the blank lines", he cuts neatly between paragraphs. If you tell him "cut anywhere", he cuts every 40 centimetres without looking, even through the middle of a button. When a piece of cloth is too big and has no blank line to cut at, he just shrugs and hands it over whole, because he knows only one trick.

### 💡 The Explanation

`CharacterTextSplitter` is the **simplest** splitter.

- **How the text is split:** on **one** separator you choose (the default is `"\n\n"`, a blank line).
- **How chunk size is measured:** by number of characters.

The code below explores four ideas, one after another:

1. `separator=""`: the **blind knife**. It cuts every `chunk_size` characters, even inside words.
2. **Overlap**: a little repeated text at the start of the next chunk, so words are not lost.
3. **A real separator** (`"\n\n"` or `"\n"`): cuts at natural places.
4. **The oversize problem**: if a piece is too big and there is only one separator, the splitter keeps the piece whole and warns you.

### 💻 The Code

The first part uses `companypolicies` from the Setup section.

```python
from langchain.text_splitter import CharacterTextSplitter

# ---------- Part 1: the blind knife on our policies ----------
text_splitter = CharacterTextSplitter(
    separator="",         # cut anywhere
    chunk_size=200,       # max 200 characters per chunk
    chunk_overlap=20,     # share 20 characters between neighbours
    length_function=len,  # measure length in characters
)
texts = text_splitter.split_text(companypolicies)
print("Number of chunks:", len(texts))            # Output: 6

# Same split, but as Document objects that carry metadata
docs = text_splitter.create_documents(
    [companypolicies],
    metadatas=[{"document": "Company Policies"}],
)
print(docs[0].metadata)                           # {'document': 'Company Policies'}

# ---------- Part 2: a tiny text you can check by eye ----------
story = ("The cat sat on the mat. It was a sunny day. The cat was very happy. "
         "Then a dog came. The dog barked loudly. The cat ran away.")

no_overlap = CharacterTextSplitter(separator="", chunk_size=40, chunk_overlap=0)
for chunk in no_overlap.split_text(story):
    print(repr(chunk))
# Output:
# 'The cat sat on the mat. It was a sunny d'
# 'ay. The cat was very happy. Then a dog c'
# 'ame. The dog barked loudly. The cat ran'
# 'away.'
# Notice: "day" was cut into 'd' + 'ay', and "came" into 'c' + 'ame'.

# ---------- Part 3: add overlap ----------
with_overlap = CharacterTextSplitter(separator="", chunk_size=40, chunk_overlap=10)
for chunk in with_overlap.split_text(story):
    print(repr(chunk))
# Output:
# 'The cat sat on the mat. It was a sunny d'
# 'a sunny day. The cat was very happy. Th'
# 'happy. Then a dog came. The dog barked'
# 'og barked loudly. The cat ran away.'
# Each chunk now starts with a bit of the previous one, so "day" appears whole.

# ---------- Part 4: real separators on three paragraphs ----------
para = (
    "Paragraph one is about cats.\nCats are small.\n\n"
    "Paragraph two is about dogs.\nDogs are loud.\n\n"
    "Paragraph three is about birds.\nBirds can fly."
)

# Cut on blank lines: one paragraph per chunk
by_paragraph = CharacterTextSplitter(separator="\n\n", chunk_size=50, chunk_overlap=0)
print(by_paragraph.split_text(para))
# Output:
# ['Paragraph one is about cats.\nCats are small.',
#  'Paragraph two is about dogs.\nDogs are loud.',
#  'Paragraph three is about birds.\nBirds can fly.']

# Cut on single new lines with a small chunk size: one line per chunk
by_line = CharacterTextSplitter(separator="\n", chunk_size=35, chunk_overlap=0)
print(len(by_line.split_text(para)), "chunks")    # Output: 6 chunks

# The oversize problem: paragraphs are 43 to 46 characters, but the limit is 30
too_small = CharacterTextSplitter(separator="\n\n", chunk_size=30, chunk_overlap=0)
chunks = too_small.split_text(para)
print([len(c) for c in chunks])
# Output: [44, 43, 46]
# LangChain also prints warnings like:
# "Created a chunk of size 44, which is longer than the specified 30"
# The splitter has only ONE separator, so it cannot cut the paragraphs any smaller.
# This exact problem is solved by the recursive splitter in the next section.
```

## Recursively Split by Character

### 📖 The Story

Chef Lina must cut a huge cake so that **no piece is bigger than her palm**. She is clever and tries cuts in a smart order. First she cuts **between the big layers**. A layer still too big? She cuts **between the sections of the layer**. Still too big? She cuts **between the bites**. Only if one single bite is still enormous does she cut it crumb by crumb.

Lina follows one rule: *use the biggest, most natural cut first, and only get smaller when you must.* That is why her pieces always look tidy, and why she never leaves a giant piece on the plate.

### 💡 The Explanation

`RecursiveCharacterTextSplitter` is the splitter **recommended for generic text**. It takes a **list** of separators and tries them in order. The default list is `["\n\n", "\n", " ", ""]`:

1. Paragraphs (`"\n\n"`), then
2. Lines (`"\n"`), then
3. Words (`" "`), then
4. Letters (`""`), the last resort.

"Recursive" simply means: *any piece that is still too big is split again with the next separator.* This keeps paragraphs, then sentences, then words together as much as possible, because those are the most meaningfully related pieces of text.

| Feature | `CharacterTextSplitter` | `RecursiveCharacterTextSplitter` |
|---|---|---|
| Number of separators | One | A list, tried in order |
| Handles oversize pieces | No (warns, keeps them big) | Yes (tries the next separator) |
| Keeps paragraphs and sentences together | Only if the separator matches | Yes, as much as possible |
| Recommended for general text | Sometimes | **Yes, the default choice** |

### 💻 The Code

The first part uses `companypolicies` from the Setup section.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

# ---------- Part 1: basic usage on our policies ----------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)
texts = text_splitter.create_documents([companypolicies])
print("Number of chunks:", len(texts))                 # Output: 13
for t in texts[:3]:
    print(repr(t.page_content))
# Output:
# 'Company Policies Handbook'
# '1. Code of Conduct'
# 'All employees must act with honesty and respect. Harassment of any kind is not tolerated.'

# ---------- Part 2: no word is cut in half ----------
story = ("The cat sat on the mat. It was a sunny day. The cat was very happy. "
         "Then a dog came. The dog barked loudly. The cat ran away.")

splitter = RecursiveCharacterTextSplitter(chunk_size=60, chunk_overlap=10)
for chunk in splitter.split_text(story):
    print(repr(chunk))
# Output:
# 'The cat sat on the mat. It was a sunny day. The cat was very'
# 'was very happy. Then a dog came. The dog barked loudly. The'
# 'The cat ran away.'
# Every chunk ends on a whole word, because the splitter fell back to spaces.

# ---------- Part 3: the problem from the previous section is gone ----------
para = (
    "Paragraph one is about cats.\nCats are small.\n\n"
    "Paragraph two is about dogs.\nDogs are loud.\n\n"
    "Paragraph three is about birds.\nBirds can fly."
)
small = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=0)
print(small.split_text(para))
# Output:
# ['Paragraph one is about cats.', 'Cats are small.',
#  'Paragraph two is about dogs.', 'Dogs are loud.',
#  'Paragraph three is about', 'birds.', 'Birds can fly.']
# No warnings: the 31-character line was cut on a space, not in the middle of a word.

# ---------- Part 4: your own list of separators ----------
sentence_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ". ", " ", ""],   # added ". " so sentences are preferred
    chunk_size=80,
    chunk_overlap=10,
)
for chunk in sentence_splitter.split_text(story):
    print(repr(chunk))
# Output:
# 'The cat sat on the mat. It was a sunny day. The cat was very happy'
# '. Then a dog came. The dog barked loudly. The cat ran away.'
# Note: by default the separator (". ") is kept at the START of the next chunk,
# which is why the second chunk begins with a full stop. The keep_separator
# parameter controls this behaviour.
```

## Split Code

### 📖 The Story

Ben is a librarian for **recipe books**. He learned that you must never tear a recipe in the middle of a step, or the dish is ruined. So he marks the start of each recipe with a coloured tag, and cuts **only just before the tags**.

Programming code is like recipes. A function is one complete recipe. If a splitter cuts a function in half, neither half makes sense. The code splitters work like Ben's tags: they know the **keywords that start a new recipe** (`def`, `class`, `function`, and so on) and cut right before them.

### 💡 The Explanation

`RecursiveCharacterTextSplitter.from_language(...)` is the same recursive splitter, but its separator list is **language-aware**. For Python, it first tries to cut before a `class`, then before a `def`, then falls back to blank lines, lines, words, and letters.

> **Corrections to the original lesson:** it showed the *plain* recursive splitter here by mistake, it used `Language` without importing it, and it called the JavaScript example "JSON".

Key points:

- Import `Language` and pass `language=Language.PYTHON` (or `Language.JS`, `Language.JAVA`, and so on).
- Everything else (`chunk_size`, `chunk_overlap`) works as before.
- The same recipe works for many languages, including Java, Go, Rust, C++, PHP, Ruby, Markdown, LaTeX, and HTML.
- More details: [LangChain code splitter docs](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/code_splitter/).

### 💻 The Code

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# ---------- Which languages are supported? ----------
print([lang.value for lang in Language])
# Output (depends on your version): ['cpp', 'go', 'java', 'kotlin', 'js', 'ts', 'php',
# 'proto', 'python', 'r', 'rst', 'ruby', 'rust', 'scala', 'swift', 'markdown', 'latex',
# 'html', 'sol', 'csharp', 'cobol', 'c', 'lua', 'perl', 'haskell', 'elixir', ...]

# ---------- Python ----------
PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
for d in python_splitter.create_documents([PYTHON_CODE]):
    print(repr(d.page_content))
# Output:
# 'def hello_world():\n    print("Hello, World!")'
# '# Call the function\nhello_world()'

# Peek at the separators used for Python
print(RecursiveCharacterTextSplitter.get_separators_for_language(Language.PYTHON))
# Output: ['\nclass ', '\ndef ', '\n\tdef ', '\n\n', '\n', ' ', '']
# Read it as: cut before a class, else before a def, else before an indented def,
# else on blank lines, lines, words, letters.

# ---------- JavaScript ----------
print(RecursiveCharacterTextSplitter.get_separators_for_language(Language.JS))
# Output starts with: ['\nfunction ', '\nconst ', '\nlet ', '\nvar ', '\nclass ', ...]

JS_CODE = """
function helloWorld() {
  console.log("Hello, World!");
}

// Call the function
helloWorld();
"""

js_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JS, chunk_size=60, chunk_overlap=0
)
for d in js_splitter.create_documents([JS_CODE]):
    print(repr(d.page_content))
# Output:
# 'function helloWorld() {\n  console.log("Hello, World!");\n}'
# '// Call the function\nhelloWorld();'

# ---------- Any other language: change only Language.XXX ----------
java_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JAVA, chunk_size=200, chunk_overlap=20
)
```

## Markdown Header Text Splitter

### 📖 The Story

Nora wrote a **storybook** with chapters called *Pets*, *Cats*, *Kittens*, and *Dogs*. Her little brother tore it into pieces with a pair of scissors and a big grin. 😬 Pages about kittens got glued to pages about dogs, and nobody could read it.

Nora fixed it. She cut the book **only at the chapter titles**, and on the back of every piece she wrote its full address: *Pets → Cats → Kittens*. Now every piece was about **one topic**, and anyone could tell exactly where it belonged.

### 💡 The Explanation

A Markdown file is organised by **headers** (`#`, `##`, `###`), which are its chapters. `MarkdownHeaderTextSplitter` cuts at those headers and stores the header names in **metadata**, so each chunk remembers its full path (for example `Pets > Cats > Kittens`).

By default the header lines are **removed** from `page_content` (they live in the metadata). If you set **`strip_headers=False`**, the headers stay inside the text too. This often improves search, because when a chunk is later **embedded** (turned into numbers), the embedding sees only the text, not the metadata. A chunk that says "Cats purr." means more when it also says "## Cats".

> **Correction:** the original lesson used `md` and `headers_to_split_on` without ever defining them. The complete, runnable version is below.

### 💻 The Code

```python
from langchain_text_splitters import MarkdownHeaderTextSplitter

md = """# Pets
Intro to pets.
## Cats
Cats purr.
### Kittens
Kittens are tiny.
## Dogs
Dogs bark."""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

# ---------- Default: headers go to metadata only ----------
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
for d in markdown_splitter.split_text(md):
    print(d)
# Output:
# page_content='Intro to pets.' metadata={'Header 1': 'Pets'}
# page_content='Cats purr.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats'}
# page_content='Kittens are tiny.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats', 'Header 3': 'Kittens'}
# page_content='Dogs bark.' metadata={'Header 1': 'Pets', 'Header 2': 'Dogs'}
# Look at "Kittens are tiny.": its metadata holds the whole address Pets > Cats > Kittens.

# ---------- strip_headers=False: headers stay inside the text too ----------
keep_headers = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False,
)
for d in keep_headers.split_text(md):
    print(d)
# Output:
# page_content='# Pets\nIntro to pets.' metadata={'Header 1': 'Pets'}
# page_content='## Cats\nCats purr.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats'}
# page_content='### Kittens\nKittens are tiny.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats', 'Header 3': 'Kittens'}
# page_content='## Dogs\nDogs bark.' metadata={'Header 1': 'Pets', 'Header 2': 'Dogs'}
```

## Split by HTML

### 📖 The Story

Sam builds a **website about animals**. The page is full of invisible labels called tags: a big title `<h1>`, section titles `<h2>`, small titles `<h3>`, and paragraphs `<p>`. A robot helper must cut the page into study cards.

Sam gives the robot two different instructions. **Robot A** makes a card for *every single element* and writes the full chapter path on the back. **Robot B** makes one card per *section*, with the section title written on the front, together with its text. Both robots follow the page's own structure, so no card mixes two topics.

### 💡 The Explanation

HTML splitters are **structure-aware**: they use the page's heading tags as natural cutting lines, just like Markdown headers. They need the **`lxml`** library (installed in the Setup section).

| | `HTMLHeaderTextSplitter` (Robot A) | `HTMLSectionSplitter` (Robot B) |
|---|---|---|
| Header text appears in `page_content` | No (only in metadata) | **Yes** |
| Metadata | Full path (H1 > H2 > H3) | Only the section's own header |
| Chunk granularity | Element by element | Section by section |
| Good for | Rich metadata and filtering | Self-contained section chunks |

Both can also be combined with a recursive splitter in a pipeline (see the two-stage section).

### 💻 The Code

```python
from langchain_text_splitters import HTMLHeaderTextSplitter, HTMLSectionSplitter

html_string = """<html><body><div><h1>Foo</h1><p>Intro Foo.</p><div><h2>Bar</h2><p>Intro Bar.</p><h3>Sub 1</h3><p>Text 1.</p></div><div><h2>Baz</h2><p>Text Baz</p></div></div></body></html>"""

headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
]

# ---------- Robot A: split by HTML header ----------
header_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
for d in header_splitter.split_text(html_string):
    print(d)
# Output:
# page_content='Foo' metadata={'Header 1': 'Foo'}
# page_content='Intro Foo.' metadata={'Header 1': 'Foo'}
# page_content='Bar' metadata={'Header 1': 'Foo', 'Header 2': 'Bar'}
# page_content='Intro Bar.' metadata={'Header 1': 'Foo', 'Header 2': 'Bar'}
# page_content='Sub 1' metadata={'Header 1': 'Foo', 'Header 2': 'Bar', 'Header 3': 'Sub 1'}
# page_content='Text 1.' metadata={'Header 1': 'Foo', 'Header 2': 'Bar', 'Header 3': 'Sub 1'}
# page_content='Baz' metadata={'Header 1': 'Foo', 'Header 2': 'Baz'}
# page_content='Text Baz' metadata={'Header 1': 'Foo', 'Header 2': 'Baz'}

# ---------- Robot B: split by HTML section ----------
section_splitter = HTMLSectionSplitter(headers_to_split_on=headers_to_split_on)
for d in section_splitter.split_text(html_string):
    print(d)
# Output:
# page_content='Foo \n Intro Foo.' metadata={'Header 1': 'Foo'}
# page_content='Bar \n Intro Bar.' metadata={'Header 2': 'Bar'}
# page_content='Sub 1 \n Text 1.' metadata={'Header 3': 'Sub 1'}
# page_content='Baz \n Text Baz' metadata={'Header 2': 'Baz'}

# ---------- Optional: split a live web page (needs internet) ----------
# docs = header_splitter.split_text_from_url("https://example.com")
```

## Split JSON

### 📖 The Story

Kofi runs a **toy shop** and keeps his stock list in a neat box of labelled drawers: `{"toys": {...}, "games": [...]}`. When the box got too heavy to carry, he needed to split it into smaller boxes. But he made one strict rule: *never cut through a drawer, and every small box must still be a proper, complete box.* If a drawer were cut in half, the list would be nonsense.

### 💡 The Explanation

JSON is the format of API results and config files. `RecursiveJsonSplitter` splits JSON data into smaller pieces while keeping **every chunk valid JSON**. It never cuts in the middle of a key or a value.

Things to remember:

- It takes `max_chunk_size` (a soft limit) and has **no overlap option**.
- A single value that is larger than the limit is not broken apart.
- Its input is a Python dictionary (or parsed JSON), not free text.

### 💻 The Code

```python
from langchain_text_splitters import RecursiveJsonSplitter

data = {
    "a": {"b": "x" * 30, "c": "y" * 30},
    "d": [1, 2, 3],
}

json_splitter = RecursiveJsonSplitter(max_chunk_size=60)
for chunk in json_splitter.split_text(data):
    print(chunk)

# Output:
# {"a": {"b": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "c": "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"}}
# {"d": [1, 2, 3]}
# Each line is a complete, valid JSON object.
```

## Split by Tokens

### 📖 The Story

Zara posts parcels at a very strict post office. The clerk does not care how many **letters** are in your message. She cares only about **stamps**: each parcel may carry at most 50 stamps. A long word like *"unbelievable"* costs three stamps (`un`, `believ`, `able`), while a tiny word like *"cat"* costs one.

Zara first counted letters, packed her parcels, and was sent home, because her parcels had too many stamps. Then she learned to **count stamps instead of letters**, and every parcel was accepted.

### 💡 The Explanation

AI models do not read letters. They read **tokens**, which are small word-pieces. A rough rule for English: **1 token is about 4 characters, or about 0.75 of a word.** Models limit the number of **tokens** they accept, not characters, so when you must stay under a model's limit, **measure chunks in tokens**.

There are three ways to do it:

- **Option A: `TokenTextSplitter`** splits purely by token count.
- **Option B: `from_tiktoken_encoder(...)`** (often nicer) keeps the smart recursive separators (paragraph, line, word) and only changes the **ruler** to tokens.
- **Option C: your own `length_function`**: any function that takes a string and returns a number. Here we count **words**.

`tiktoken` may need internet access the first time it runs, to download its vocabulary files. The block uses `companypolicies` from the Setup section.

### 💻 The Code

```python
from langchain_text_splitters import TokenTextSplitter, RecursiveCharacterTextSplitter

# ---------- Option A: pure token splitting ----------
token_splitter = TokenTextSplitter(
    encoding_name="cl100k_base",  # tokenizer used by many OpenAI models
    chunk_size=50,                # 50 TOKENS, not characters
    chunk_overlap=5,
)
token_chunks = token_splitter.split_text(companypolicies)
print("Option A chunks:", len(token_chunks))

# ---------- Option B: recursive separators, measured in tokens ----------
token_recursive = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    chunk_size=50,
    chunk_overlap=5,
)
chunks_b = token_recursive.split_text(companypolicies)
print("Option B chunks:", len(chunks_b))

# ---------- Option C: your own ruler (count words) ----------
def word_count(text: str) -> int:
    return len(text.split())

word_splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,              # 20 WORDS
    chunk_overlap=3,
    length_function=word_count,
)
chunks_c = word_splitter.split_text(companypolicies)
print("Option C chunks:", len(chunks_c))     # Output: 12
print(repr(chunks_c[0]))                     # Output: 'Company Policies Handbook'
```

## Combining Splitters: A Two-Stage Pipeline

### 📖 The Story

Lila organises the school library. She works in **two steps**. In step one, she sorts books **by subject shelf**: animals here, space there. In step two, she checks each shelf and, if a shelf is overloaded, she splits it into **smaller boxes**, but she sticks the **subject label on every box** so nothing gets lost.

Step one keeps topics together. Step two keeps sizes under control. Together they make a perfect library.

### 💡 The Explanation

Real-world RAG almost always uses **two stages**:

1. **Stage 1, structure-aware** (Markdown or HTML header splitter): cut at chapters so each chunk is about one topic and carries header metadata.
2. **Stage 2, size-aware** (`RecursiveCharacterTextSplitter`): if a chapter is still too big, cut it down.

Why both? Header splitters do **not** limit chunk size. A single chapter could be 5,000 characters long. Stage 2 fixes that, and `split_documents` **copies the header metadata** onto every smaller piece. The same idea works for HTML: `HTMLHeaderTextSplitter` first, then the recursive splitter.

### 💻 The Code

```python
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

md = """# Pets
Intro to pets.
## Cats
Cats purr.
### Kittens
Kittens are tiny.
## Dogs
Dogs bark."""

headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]

# Stage 1: cut by chapters (structure)
stage1_docs = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
).split_text(md)

# Stage 2: make sure no chunk is bigger than chunk_size (size)
stage2 = RecursiveCharacterTextSplitter(chunk_size=12, chunk_overlap=0)
final_docs = stage2.split_documents(stage1_docs)

for d in final_docs:
    print(d)

# Output (chunk_size=12 is deliberately tiny, just to show the effect):
# page_content='Intro to' metadata={'Header 1': 'Pets'}
# page_content='pets.' metadata={'Header 1': 'Pets'}
# page_content='Cats purr.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats'}
# page_content='Kittens are' metadata={'Header 1': 'Pets', 'Header 2': 'Cats', 'Header 3': 'Kittens'}
# page_content='tiny.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats', 'Header 3': 'Kittens'}
# page_content='Dogs bark.' metadata={'Header 1': 'Pets', 'Header 2': 'Dogs'}
# "Intro to pets." was too long, so it became two pieces, and BOTH kept the label.
```

## Choosing chunk_size and chunk_overlap

### 📖 The Story

Goldilocks again! 🐻 She tried a **tiny** chunk: "every 90 days." Nobody knew what happened every 90 days. She tried a **huge** chunk: an entire handbook. It contained the answer, but also thousands of words nobody needed, and the search could not tell which part mattered. Then she tried a **medium** chunk: two or three sentences about one rule. *"Just right!"* she said.

### 💡 The Explanation

There is no single perfect number. Use these starting points, then **test with real questions**.

| Content type | Suggested `chunk_size` (characters) | Suggested overlap |
|---|---|---|
| Short FAQs, chat messages | 200 to 400 | 0 to 40 |
| Policies, articles, documentation | 500 to 1000 | 50 to 150 (about 10 to 20 percent) |
| Long technical or legal text where context matters | 1000 to 2000 | 100 to 300 |
| Source code | 500 to 1500 (cut at functions and classes) | 0 to 100 |

**The balancing act:**

| Small chunks | Large chunks |
|---|---|
| ✅ Precise search | ✅ More context per chunk |
| ✅ Cheaper to embed | ✅ Fewer chunks to manage |
| ❌ May lose context | ❌ Search gets "blurry" |
| ❌ Many more chunks | ❌ Uses more of the model's window |

**A simple testing recipe:** write 10 realistic questions, split with a few different sizes, and check whether the retrieved chunk actually contains the answer. Keep the size that wins most often. The block below prints useful statistics for several sizes and uses `companypolicies` from the Setup section.

### 💻 The Code

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Compare several chunk sizes (overlap = 10 percent of the size)
for size in (100, 200, 400, 800):
    splitter = RecursiveCharacterTextSplitter(chunk_size=size, chunk_overlap=size // 10)
    chunks = splitter.split_text(companypolicies)
    sizes = [len(c) for c in chunks]
    print(f"chunk_size={size:4} -> chunks={len(chunks):2} | smallest={min(sizes):3} | largest={max(sizes):3}")

# Output:
# chunk_size= 100 -> chunks=13 | smallest= 18 | largest= 98
# chunk_size= 200 -> chunks= 8 | smallest= 25 | largest=193
# chunk_size= 400 -> chunks= 4 | smallest=220 | largest=240
# chunk_size= 800 -> chunks= 2 | smallest=240 | largest=684
# Reading the table: bigger chunk_size means fewer, bigger chunks.
```

## Which Splitter Should I Use?

### 📖 The Story

A new helper, Eli, stood in front of a wall of tools and panicked. "Which one do I use?" Grandpa smiled and gave him a simple chart: *"Look at what you are holding, and the chart tells you the tool. If you are ever unsure, grab the all-purpose one."*

### 💡 The Explanation

| Your data | Best splitter |
|---|---|
| Plain text, articles, general documents | `RecursiveCharacterTextSplitter` |
| Text with one reliable separator | `CharacterTextSplitter` |
| Python, JS, Java, and other code | `RecursiveCharacterTextSplitter.from_language(...)` |
| Markdown notes, READMEs, docs | `MarkdownHeaderTextSplitter`, then Recursive |
| Web pages (HTML) | `HTMLHeaderTextSplitter` or `HTMLSectionSplitter`, then Recursive |
| LaTeX papers | `RecursiveCharacterTextSplitter.from_language(Language.LATEX)` |
| JSON and API data | `RecursiveJsonSplitter` |
| You must obey a model's token limit | `from_tiktoken_encoder(...)` or `TokenTextSplitter` |

**When unsure:** start with `RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)`. It is a safe default.

### 💻 The Code

The function below turns the chart into code: give it a file type and it returns a ready-made splitter.

```python
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    MarkdownHeaderTextSplitter,
    HTMLHeaderTextSplitter,
    RecursiveJsonSplitter,
    Language,
)

def choose_splitter(file_type: str):
    """Return a sensible default splitter for a given file type."""
    file_type = file_type.lower()

    if file_type in ("md", "markdown"):
        return MarkdownHeaderTextSplitter(
            headers_to_split_on=[("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")],
            strip_headers=False,
        )
    if file_type in ("html", "htm"):
        return HTMLHeaderTextSplitter(
            headers_to_split_on=[("h1", "Header 1"), ("h2", "Header 2"), ("h3", "Header 3")]
        )
    if file_type == "json":
        return RecursiveJsonSplitter(max_chunk_size=500)
    if file_type in ("py", "python"):
        return RecursiveCharacterTextSplitter.from_language(
            language=Language.PYTHON, chunk_size=800, chunk_overlap=0)
    if file_type in ("js", "javascript"):
        return RecursiveCharacterTextSplitter.from_language(
            language=Language.JS, chunk_size=800, chunk_overlap=0)
    if file_type in ("tex", "latex"):
        return RecursiveCharacterTextSplitter.from_language(
            language=Language.LATEX, chunk_size=800, chunk_overlap=0)

    # Safe default for everything else (plain text, articles, ...)
    return RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)

for kind in ["txt", "md", "html", "json", "py"]:
    print(kind, "->", type(choose_splitter(kind)).__name__)

# Output:
# txt -> RecursiveCharacterTextSplitter
# md -> MarkdownHeaderTextSplitter
# html -> HTMLHeaderTextSplitter
# json -> RecursiveJsonSplitter
# py -> RecursiveCharacterTextSplitter
```

## Common Mistakes and Troubleshooting

### 📖 The Story

Pip the baker kept a **"Oops Notebook"**. Every time something went wrong in the kitchen, he wrote down what happened, why, and how to fix it. His next pizzas were perfect. Every programmer should keep a notebook like that, so here is a ready-made one for text splitting.

### 💡 The Explanation

| Problem | Cause | Fix |
|---|---|---|
| `ValueError: Got a larger chunk overlap than chunk size` | `chunk_overlap >= chunk_size` | Make overlap smaller (about 10 to 20 percent of chunk size) |
| Warning: `Created a chunk of size X, which is longer than the specified Y` | `CharacterTextSplitter` found a piece bigger than `chunk_size` and has no other separator | Use `RecursiveCharacterTextSplitter` |
| `NameError: name 'Language' is not defined` | Forgot the import | `from langchain_text_splitters import Language` |
| `NameError: name 'headers_to_split_on' is not defined` | The list was never created | Define it before creating the splitter |
| Words are cut in half | Used `separator=""` | Use the recursive splitter with its default separators |
| LaTeX shows strange characters where `\begin` should be | In a normal Python string, `\b` means *backspace* | Use a **raw string**: `r"""\begin{document} ..."""` |
| Header chunks are huge | Header splitters do not limit size | Add the second stage with `RecursiveCharacterTextSplitter` |
| Metadata disappears after splitting | Used `split_text` on plain strings | Use `create_documents(..., metadatas=...)` or `split_documents(...)` |
| `HTMLSectionSplitter` import or parse error | `lxml` is not installed | `pip install lxml` |
| Chunk counts differ from a friend's | Different library versions or text encoding | Pin versions and read files with `encoding="utf-8"` |

### 💻 The Code

The block below reproduces three classic mistakes on purpose, together with their fixes.

```python
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    Language,
)

# ---------- Mistake 1: overlap bigger than chunk size ----------
try:
    CharacterTextSplitter(chunk_size=20, chunk_overlap=50)
except ValueError as error:
    print("Mistake 1:", error)
# Output: Mistake 1: Got a larger chunk overlap (50) than chunk size (20), should be smaller.
# Fix: use chunk_overlap=2 (about 10 percent).

# ---------- Mistake 2: forgetting the raw string for LaTeX ----------
broken = "\begin{document}"        # "\b" becomes a backspace character
fixed = r"\begin{document}"        # raw string keeps the backslash
print("Broken length:", len(broken), "| Fixed length:", len(fixed))
# Output: Broken length: 15 | Fixed length: 16
# The broken string is one character shorter because \b was swallowed.

# ---------- Mistake 3: metadata lost with split_text ----------
splitter = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=0)
lost = splitter.split_text("Alpha beta gamma delta epsilon zeta eta theta")
print(type(lost[0]).__name__)      # Output: str   (no metadata possible!)

kept = splitter.create_documents(
    ["Alpha beta gamma delta epsilon zeta eta theta"],
    metadatas=[{"source": "greek"}],
)
print(kept[0].metadata)            # Output: {'source': 'greek'}
```

## Summary

### 📖 The Story

At the end of the party, Pip counted what he had learned: *cut with care, cut at natural lines, share a little cheese between slices, label every slice, and taste-test before the next party.* Everyone cheered, and every guest went home with exactly the slice they needed.

### 💡 The Explanation

- **Splitting** cuts long text into chunks the AI can handle. It is the "slicing the pizza" step of RAG.
- **`chunk_size`** is the maximum slice size. **`chunk_overlap`** is the shared edge. **`length_function`** is the ruler. **`separator(s)`** are the dotted lines.
- A **`Document`** has `page_content` (text) and `metadata` (labels).
- Use `split_text` for strings, `create_documents` to add metadata, and `split_documents` to split existing `Document`s.
- **`CharacterTextSplitter`** uses one separator. It is simple but not smart.
- **`RecursiveCharacterTextSplitter`** tries a list of separators. It is the **default recommendation**.
- **`from_language(...)`** makes the recursive splitter understand code and LaTeX.
- **Markdown and HTML header splitters** cut by document structure and store header paths in metadata.
- **`RecursiveJsonSplitter`** keeps every JSON chunk valid.
- Measure in **tokens** when a model's token limit matters.
- Use a **two-stage pipeline** (structure first, then size) for the best chunks.
- Test your settings with **real questions**. Good chunks lead to good retrieval, which leads to good answers.

### 💻 The Code

A compact "cheat sheet" you can keep. It is runnable and prints one line per splitter.

```python
from langchain_text_splitters import (
    CharacterTextSplitter, RecursiveCharacterTextSplitter,
    MarkdownHeaderTextSplitter, Language,
)

text = "Cats purr.\n\nDogs bark.\n\nBirds sing."

print(CharacterTextSplitter(separator="\n\n", chunk_size=15, chunk_overlap=0).split_text(text))
print(RecursiveCharacterTextSplitter(chunk_size=15, chunk_overlap=0).split_text(text))
print(RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=40, chunk_overlap=0
).split_text("def a():\n    return 1\n\ndef b():\n    return 2"))
print(MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "H1")]).split_text("# Zoo\nLions roar."))

# Output:
# ['Cats purr.', 'Dogs bark.', 'Birds sing.']
# ['Cats purr.', 'Dogs bark.', 'Birds sing.']
# ['def a():\n    return 1', 'def b():\n    return 2']
# [Document(page_content='Lions roar.', metadata={'H1': 'Zoo'})]
# (Exact printing of Document objects differs slightly between versions.)
```

## Exercises

### Exercise 1: The Scissors Story (Change the Separator)

📖 **Story:** Tom the tailor (from the character splitter section) has three pairs of scissors: one cuts at **new lines** (`"\n"`), one at **blank lines** (`"\n\n"`), and one cuts **anywhere** (`""`). He wants to cut the company policy handbook with each pair and compare the results.

**Your task:** use `CharacterTextSplitter` on `companypolicies` with `chunk_size=200` and `chunk_overlap=20`, once for each separator.

1. How many chunks do you get with each separator?
2. Print the first chunk of each.
3. Which separator cuts words in half? Which one produces warnings, and why?

### Exercise 2: The Scientist's Paper (Split LaTeX)

📖 **Story:** Dr. Amina wrote a research paper in LaTeX, a typesetting language that scientists love. She wants to split it into chunks for a RAG assistant, but she must not tear a section in half unless she has to.

**Your task:** split the LaTeX text below using `RecursiveCharacterTextSplitter.from_language(language=Language.LATEX, ...)` with `chunk_size=150` and `chunk_overlap=0`. Print each chunk with its number. Then try `chunk_size=400` and compare.

> **Hint:** the original lab used a normal string. Use a **raw string** (`r"""..."""`) so that `\begin` is not read as a backspace.

```python
latex_text = r"""
\documentclass{article}

\begin{document}

\maketitle

\section{Introduction}
Large language models (LLMs) are a type of machine learning model that can be trained on vast amounts of text data to generate human-like language. In recent years, LLMs have made significant advances in a variety of natural language processing tasks, including language translation, text generation, and sentiment analysis.

\subsection{History of LLMs}
The earliest LLMs were developed in the 1980s and 1990s, but they were limited by the amount of data that could be processed and the computational power available at the time. In the past decade, however, advances in hardware and software have made it possible to train LLMs on massive datasets, leading to significant improvements in performance.

\subsection{Applications of LLMs}
LLMs have many applications in industry, including chatbots, content creation, and virtual assistants. They can also be used in academia for research in linguistics, psychology, and computational linguistics.

\end{document}
"""
```

### Exercise 3 (Capstone): The Helpful Librarian Robot

📖 **Story:** The school hires a robot librarian named **Robo-Lib**. Teachers ask it questions about the **Employee Handbook**, like "How many days of sick leave do I get?". Robo-Lib cannot read the whole handbook for every question, so you must **cut the handbook into good chunks** and teach Robo-Lib to **find the best chunk** for each question.

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

1. Split `handbook_md` in **two stages**: `MarkdownHeaderTextSplitter` (keep the headers in the text), then `RecursiveCharacterTextSplitter` with `chunk_size=200` and `chunk_overlap=30`.
2. Print each chunk's length, text, and metadata.
3. Write a function `retrieve(question, docs, k=2)` that returns the `k` chunks sharing the **most words** with the question. (Real RAG uses embeddings, but word overlap is enough to see the idea.)
4. Test it with: *"How many days of sick leave do I get?"* and *"How often must I change my password?"*
5. Reflect: what would happen with `chunk_size=1000`? And with `chunk_size=40`?

## Solutions

### Solution 1: The Scissors Story

**Explanation.** The separator decides *where cuts are allowed*; `chunk_size` decides *how much is merged back together*.

- `"\n"` cuts at line breaks, then **merges whole lines** until adding another line would pass 200 characters. Chunks end at line ends, so sentences stay whole. Overlap is only used when whole lines fit inside the overlap size, so you may see little or none.
- `"\n\n"` treats each **blank-line-separated block** as one unit. Several of our blocks are longer than 200 characters, so LangChain **warns** ("Created a chunk of size ..., which is longer than the specified 200") and keeps them whole, because this splitter has only one separator.
- `""` cuts **every 200 characters** regardless of meaning, so it is the one that **cuts words in half**.

```python
from langchain_text_splitters import CharacterTextSplitter

for sep in ["\n", "\n\n", ""]:
    splitter = CharacterTextSplitter(
        separator=sep,
        chunk_size=200,
        chunk_overlap=20,
        length_function=len,
    )
    docs = splitter.create_documents([companypolicies])
    print(f"separator={sep!r:6} -> {len(docs)} chunks, sizes={[len(d.page_content) for d in docs]}")
    print("   first chunk:", repr(docs[0].page_content[:60]), "...")

# Output (with the sample companypolicies from the Setup section):
# separator='\n'   -> 6 chunks, sizes=[134, 183, 139, 164, 170, 143]
# separator='\n\n' -> 5 chunks, sizes=[25, 193, 222, 238, 240]     (plus warnings: sizes above 200)
# separator=''     -> 6 chunks, sizes=[200, 199, 199, 199, 199, 26]
# Notice: "\n" gives tidy sizes under 200, "\n\n" breaks the limit, and "" is exact but blind.
```

### Solution 2: The Scientist's Paper

**Explanation.** The LaTeX separators prefer cutting **before `\section` and `\subsection`**, then fall back to paragraphs, lines, and words. With `chunk_size=150`, the long paragraphs (about 300 characters) do not fit, so each section is broken into several pieces. With `chunk_size=400`, each section fits in one chunk.

```python
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

latex_text = r"""
\documentclass{article}

\begin{document}

\maketitle

\section{Introduction}
Large language models (LLMs) are a type of machine learning model that can be trained on vast amounts of text data to generate human-like language. In recent years, LLMs have made significant advances in a variety of natural language processing tasks, including language translation, text generation, and sentiment analysis.

\subsection{History of LLMs}
The earliest LLMs were developed in the 1980s and 1990s, but they were limited by the amount of data that could be processed and the computational power available at the time. In the past decade, however, advances in hardware and software have made it possible to train LLMs on massive datasets, leading to significant improvements in performance.

\subsection{Applications of LLMs}
LLMs have many applications in industry, including chatbots, content creation, and virtual assistants. They can also be used in academia for research in linguistics, psychology, and computational linguistics.

\end{document}
"""

for size in (150, 400):
    latex_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.LATEX, chunk_size=size, chunk_overlap=0
    )
    latex_docs = latex_splitter.create_documents([latex_text])
    print(f"===== chunk_size={size}: {len(latex_docs)} chunks =====")
    for i, doc in enumerate(latex_docs, start=1):
        first_line = doc.page_content.strip().splitlines()[0][:45]
        print(f"Chunk {i} ({len(doc.page_content)} chars): {first_line}")

# Output:
# ===== chunk_size=150: 9 chunks =====
# Chunk 1 (53 chars): \documentclass{article}
# Chunk 2 (149 chars): \section{Introduction}
# Chunk 3 (143 chars): human-like language. In recent years, LLMs ...
# Chunk 4 (53 chars): translation, text generation, and sentiment analysis.
# Chunk 5 (143 chars): \subsection{History of LLMs}
# Chunk 6 (148 chars): processed and the computational power ...
# Chunk 7 (83 chars): train LLMs on massive datasets, ...
# Chunk 8 (145 chars): \subsection{Applications of LLMs}
# Chunk 9 (112 chars): also be used in academia for research ...
# ===== chunk_size=400: 4 chunks =====
# Chunk 1 (53 chars): \documentclass{article}
# Chunk 2 (347 chars): \section{Introduction}
# Chunk 3 (376 chars): \subsection{History of LLMs}
# Chunk 4 (258 chars): \subsection{Applications of LLMs}
# With 400, every section starts a new chunk and stays in one piece.
# (The first-line previews above are shortened for display; your exact text may differ slightly.)
```

### Solution 3 (Capstone): The Helpful Librarian Robot

**Explanation.** Stage 1 cuts the handbook into one chunk per section and attaches header metadata. Stage 2 only cuts a chunk if it is longer than 200 characters, and it copies the metadata to the new pieces. The retriever then scores each chunk by shared words.

Two practical details to notice in the output:

- The first chunk is just the headers `# Employee Handbook` and `## Remote Work`, because the handbook has no text between those two headers. A tiny header-only chunk like this is normal with `strip_headers=False`.
- The **Remote Work** section is longer than 200 characters, so Stage 2 splits it into two chunks (chunks 2 and 3). **Both** carry the same header metadata.
- Plain word matching misses "change" versus "changed". A tiny fix, comparing only the **first five letters** of each word (a crude "stemmer"), solves it. This is a small taste of why real systems use embeddings.

```python
import re
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

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

stage1 = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False,            # keep the header text inside page_content
).split_text(handbook_md)

stage2 = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
docs = stage2.split_documents(stage1)

# ---------- Task 2: inspect the chunks ----------
for i, d in enumerate(docs, start=1):
    print(f"Chunk {i} | {len(d.page_content)} chars | {d.metadata}")
    print("   ", repr(d.page_content[:60]))

# ---------- Task 3: a tiny retriever ----------
STOPWORDS = {"the", "a", "an", "of", "do", "i", "how", "many", "must", "is", "to", "get", "my", "often"}

def tokenize(text):
    words = re.findall(r"[a-z0-9']+", text.lower())
    return {w[:5] for w in words if w not in STOPWORDS}     # first 5 letters = crude stemming

def retrieve(question, docs, k=2):
    q_words = tokenize(question)
    scored = [(len(q_words & tokenize(d.page_content)), d) for d in docs]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored[:k]

# ---------- Task 4: test ----------
for q in ["How many days of sick leave do I get?",
          "How often must I change my password?"]:
    print("\nQUESTION:", q)
    for score, d in retrieve(q, docs, k=2):
        print(f"  score={score} | {d.metadata.get('Header 3') or d.metadata.get('Header 2')}")

# Output (Task 2):
# Chunk 1 | 36 chars  | {'Header 1': 'Employee Handbook', 'Header 2': 'Remote Work'}
#     '# Employee Handbook  \n## Remote Work'
# Chunk 2 | 193 chars | {'Header 1': 'Employee Handbook', 'Header 2': 'Remote Work'}
#     'Employees may work remotely up to three days per week with m'
# Chunk 3 | 33 chars  | {'Header 1': 'Employee Handbook', 'Header 2': 'Remote Work'}
#     'must be kept secure at all times.'
# Chunk 4 | 167 chars | {... 'Header 2': 'Leave Policy', 'Header 3': 'Annual Leave'}
#     '## Leave Policy  \n### Annual Leave\nFull-time employees recei'
# Chunk 5 | 96 chars  | {... 'Header 2': 'Leave Policy', 'Header 3': 'Sick Leave'}
#     '### Sick Leave\nSick leave is granted for up to 10 days per y'
# Chunk 6 | 168 chars | {'Header 1': 'Employee Handbook', 'Header 2': 'Information Security'}
#     '## Information Security\nPasswords must be at least 12 charac'
#
# Output (Task 4):
# QUESTION: How many days of sick leave do I get?
#   score=3 | Sick Leave
#   score=2 | Annual Leave
#
# QUESTION: How often must I change my password?
#   score=2 | Information Security
#   score=0 | Remote Work
```

**Task 5: Reflection**

| Setting | What happens | Why it matters |
|---|---|---|
| `chunk_size=1000` | Stage 2 does nothing, because every section already fits. Each chunk is a whole section, so retrieval is still good here. | On a *bigger* handbook, a 1000-character chunk could mix several rules, so a question might retrieve a large chunk of mostly irrelevant text. |
| `chunk_size=40` | Sentences are chopped into tiny fragments such as `"Passwords must be at least 12"` and `"characters long and changed"`. | Fragments lose meaning. A chunk like `"every 90 days."` does not say what happens every 90 days, so retrieval gets worse. |
| `chunk_size=200` (our choice) | About one or two sentences per chunk, still tagged with their section headers. | A good balance for short policy text: each chunk holds one clear idea. |

**Big idea:** *header metadata plus sensibly sized chunks* give the retriever **precise** pieces that still **make sense on their own**. This is exactly why we study text splitting before building a full RAG system.

### Bonus Challenges

1. Replace the word-overlap retriever with an **embedding-based** retriever (for example, `FAISS` or `Chroma` with an embeddings model) and compare the results.
2. Try `chunk_size` values of 100, 200, 400, and 800, and record how often the correct chunk ranks first for 10 questions you write yourself.
3. Convert `handbook_md` to HTML and repeat the exercise with `HTMLHeaderTextSplitter`.
