# Lesson 2: Apply Text Splitting Techniques to Enhance Model Responsiveness

## 1. Why Do We Split Text? 

Imagine you have a **giant pizza**. 🍕

You cannot put the whole pizza in your mouth at once. So you cut it into **slices**. Each slice is small enough to hold and eat, and each slice still tastes like pizza.

Text is the same:

| Pizza world | Text world |
|---|---|
| Whole pizza | A long document (a 200-page policy file, a book, a website) |
| A slice | A **chunk** of text |
| Size of a slice | `chunk_size` |
| A bit of cheese shared between two slices | `chunk_overlap` |
| The knife | The **text splitter** |

AI models (like ChatGPT or Claude) have a **limited "mouth"**. This is called the **context window**. They can only read a certain amount of text at one time. If your document is bigger than that, we must slice it up first.

### A bad cut vs. a good cut

Look at this sentence:

> "The cat sat on the mat. It was a sunny day."

- **Bad cut** (in the middle of a word): `"The cat sat on the m"` | `"at. It was a sunny day."`
- **Good cut** (between sentences): `"The cat sat on the mat."` | `"It was a sunny day."`

A good splitter tries to **cut at natural places**: paragraphs first, then sentences, then words. That way every slice still **makes sense on its own**.



## 2. Where Splitting Fits in RAG

**RAG** stands for **Retrieval-Augmented Generation**. In baby words:

> The AI does not know your private documents. So before it answers, we **look up** the best pieces from your documents and **hand them to the AI** like a cheat sheet. Then the AI writes the answer using that cheat sheet.

Here is the whole journey:

```
 ┌──────────────┐   ┌───────────────┐   ┌──────────────┐   ┌──────────────┐
 │ 1. LOAD      │──▶│ 2. SPLIT      │──▶│ 3. EMBED     │──▶│ 4. STORE     │
 │ your files   │   │ into chunks   │   │ chunks into  │   │ in a vector  │
 │ (PDF, HTML)  │   │ (THIS LESSON) │   │ numbers      │   │ database     │
 └──────────────┘   └───────────────┘   └──────────────┘   └──────┬───────┘
                                                                  │
 ┌──────────────┐   ┌───────────────┐   ┌──────────────┐          │
 │ 7. ANSWER    │◀──│ 6. GENERATE   │◀──│ 5. RETRIEVE  │◀─────────┘
 │ to the user  │   │ LLM reads the │   │ best chunks  │   user asks a
 │              │   │ chunks        │   │ for question │   question
 └──────────────┘   └───────────────┘   └──────────────┘
```

### Why splitting matters so much

| If chunks are... | What goes wrong |
|---|---|
| **Too big** | Each chunk mixes many topics, so the search gets "blurry". The model also wastes space on irrelevant text. |
| **Too small** | Each chunk loses its meaning ("It was approved by them." Who? What?). |
| **Cut in the wrong place** | An answer is split in half, and retrieval finds only half of it. |
| **Just right** | Each chunk is one clear idea. Search is sharp and answers are accurate. |

**Golden rule:** *Good chunks = good retrieval = good answers.*



## 3. Objectives

After completing this lesson you will be able to:

- Explain **why** text splitting is needed and how it affects RAG quality.
- Use the key parameters: `separator`, `chunk_size`, `chunk_overlap`, `length_function`.
- Create and read LangChain `Document` objects, including metadata.
- Use `CharacterTextSplitter`, `RecursiveCharacterTextSplitter`, code splitters, `MarkdownHeaderTextSplitter`, `HTMLHeaderTextSplitter`, `HTMLSectionSplitter`, `RecursiveJsonSplitter`, and token-based splitters.
- Combine a structure-aware splitter with a size-based splitter.
- Choose sensible chunk sizes and pick the right splitter for each file type.



## 4. Setup and Installation

For this lesson you will use:

- [`langchain`, `langchain-text-splitters`](https://www.langchain.com/): the splitters themselves.
- [`lxml`](https://pypi.org/project/lxml/): needed for splitting HTML.
- `tiktoken` (optional): needed only for token-based splitting in Section 14.

```python
%%capture
!pip install "langchain==0.2.7"
!pip install "langchain-core==0.2.20"
!pip install "langchain-text-splitters==0.2.2"
!pip install "lxml==5.2.2"
!pip install tiktoken        # optional, only for Section 14
```

> **Note:** `%%capture` and `!pip` work in Jupyter or Colab notebooks. In a normal terminal, run `pip install ...` without the `!`.

### Our sample document: `companypolicies`

The original lab loads a file called `companypolicies.txt`, but never shows how it was created. To make every example below **runnable on its own**, we define a small sample text. You can replace it with your own file later.

```python
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

print(len(companypolicies), "characters")
```

**Loading from a real file instead** (use this when you have `companypolicies.txt`):

```python
with open("companypolicies.txt", "r", encoding="utf-8") as f:
    companypolicies = f.read()
```



## 5. Key Parameters Explained

When you create a splitter, you control it with these knobs:

| Parameter | What it does | Baby explanation |
|---|---|---|
| `separator` / `separators` | The character(s) where the splitter prefers to cut | *"Where is the dotted line on the paper?"* |
| `chunk_size` | The **maximum** size of one chunk | *"How big can one slice be?"* |
| `chunk_overlap` | How much of the end of chunk A is repeated at the start of chunk B | *"A little shared cheese between slices so nothing is lost at the edge."* |
| `length_function` | How size is measured (`len` = characters; a token counter = tokens) | *"Do we measure the slice with a ruler (characters) or by weighing it (tokens)?"* |

### Why overlap helps: a picture

Without overlap, an important sentence can be cut in half:

```
Chunk 1: "... Passwords must be at least 12 char"
Chunk 2: "acters long and changed every 90 days ..."
```

With overlap, both chunks share the middle part:

```
Chunk 1: "... Passwords must be at least 12 characters long"
Chunk 2: "at least 12 characters long and changed every 90 days ..."
```

Now whichever chunk is retrieved, the idea survives.

### Important facts beginners often miss

1. `chunk_size` is a **maximum**, not an exact size. Real chunks are often shorter.
2. Overlap must be **smaller** than chunk size. If `chunk_overlap >= chunk_size`, LangChain raises an error.
3. Splitters work by **splitting first on the separator, then merging small pieces back together** until the chunk size limit is reached.
4. A single piece that is already bigger than `chunk_size` (and cannot be split further by that separator) is **kept whole**, and you get a warning. Section 8 shows this.



## 6. The Document Object

Before we meet the splitters, we need to meet what they produce. In LangChain, a text chunk is wrapped in a **`Document`** object. Think of it as a **labelled box**:

- `page_content` (a `str`): the actual text inside the box.
- `metadata` (a `dict`): the sticky label on the box. It can hold a file name, page number, source, section title, date, and so on.

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

print(doc.page_content)
print(doc.metadata)
print(doc.metadata["my_document_source"])
```

### Why metadata matters in RAG

Imagine the AI answers: *"Employees get 20 days of leave."* A good RAG system can also say: *"Source: Company Policies, section 3."* That is possible only because the chunk carried its **metadata** with it.



## 7. Three Ways to Call a Splitter

Every LangChain splitter has similar methods. Knowing which to use saves confusion:

| Method | Input | Output | Use it when |
|---|---|---|---|
| `split_text(text)` | one string | list of **strings** | You just want raw text pieces |
| `create_documents([text1, text2], metadatas=[...])` | list of strings | list of **Document** objects | You have raw strings and want metadata attached |
| `split_documents(docs)` | list of **Document** objects | list of **Document** objects | You already loaded `Document`s (for example from a loader) and want to split them while **keeping** their metadata |

Quick demo:

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=60, chunk_overlap=10)

# 1) Strings in, strings out
strings = splitter.split_text(companypolicies)
print(type(strings[0]))        # <class 'str'>

# 2) Strings in, Documents out (add metadata yourself)
docs = splitter.create_documents(
    [companypolicies],
    metadatas=[{"source": "Company Policies"}],
)
print(type(docs[0]))           # Document
print(docs[0].metadata)        # {'source': 'Company Policies'}

# 3) Documents in, Documents out (metadata is copied to every chunk)
original = [Document(page_content=companypolicies, metadata={"source": "Company Policies"})]
chunked = splitter.split_documents(original)
print(len(chunked), chunked[0].metadata)
```



## 8. Split by Character

This is the **simplest** splitter.

- **How the text is split:** on one separator you choose (default `"\n\n"`, a blank line).
- **How chunk size is measured:** by number of characters.

### Step 1: Meet the splitter with `separator=""`

When `separator=""`, **any character** may be a cutting point. The splitter simply cuts every `chunk_size` characters. It is the "blind knife".

```python
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="",        # cut anywhere
    chunk_size=200,      # max 200 characters per chunk
    chunk_overlap=20,    # share 20 characters between neighbours
    length_function=len, # measure length in characters
)

texts = text_splitter.split_text(companypolicies)
print("Number of chunks:", len(texts))
print(texts[0])
```

You can also create `Document` objects with metadata:

```python
docs = text_splitter.create_documents(
    [companypolicies],
    metadatas=[{"document": "Company Policies"}],
)
print(docs[0])
```

### Step 2: A tiny example you can verify by eye

```python
story = "The cat sat on the mat. It was a sunny day. The cat was very happy. Then a dog came. The dog barked loudly. The cat ran away."

splitter = CharacterTextSplitter(separator="", chunk_size=40, chunk_overlap=0)
for chunk in splitter.split_text(story):
    print(repr(chunk))
```

**Output:**

```
'The cat sat on the mat. It was a sunny d'
'ay. The cat was very happy. Then a dog c'
'ame. The dog barked loudly. The cat ran'
'away.'
```

Notice how the splitter cut the word *"day"* into `d` and `ay`, and *"came"* into `c` and `ame`. That is the downside of a blind knife.

### Step 3: Now add overlap

```python
splitter = CharacterTextSplitter(separator="", chunk_size=40, chunk_overlap=10)
for chunk in splitter.split_text(story):
    print(repr(chunk))
```

**Output:**

```
'The cat sat on the mat. It was a sunny d'
'a sunny day. The cat was very happy. Th'
'happy. Then a dog came. The dog barked'
'og barked loudly. The cat ran away.'
```

Each chunk now **starts with a little bit of the previous chunk** (for example `a sunny d` appears at the end of chunk 1 and the start of chunk 2). The word "day" now appears whole in chunk 2.

### Step 4: Using a real separator (`"\n\n"` and `"\n"`)

Usually you want the knife to cut at **natural places**, such as paragraph breaks. Let's use a tiny text with three paragraphs:

```python
para = (
    "Paragraph one is about cats.\nCats are small.\n\n"
    "Paragraph two is about dogs.\nDogs are loud.\n\n"
    "Paragraph three is about birds.\nBirds can fly."
)
```

**Cut on blank lines (`"\n\n"`) with a big enough chunk size:**

```python
splitter = CharacterTextSplitter(separator="\n\n", chunk_size=50, chunk_overlap=0)
for chunk in splitter.split_text(para):
    print(repr(chunk))
```

```
'Paragraph one is about cats.\nCats are small.'
'Paragraph two is about dogs.\nDogs are loud.'
'Paragraph three is about birds.\nBirds can fly.'
```

One paragraph per chunk. 🎉

**Cut on single new lines (`"\n"`) with a small chunk size:**

```python
splitter = CharacterTextSplitter(separator="\n", chunk_size=30, chunk_overlap=0)
for chunk in splitter.split_text(para):
    print(repr(chunk))
```

Every line becomes its own chunk (6 chunks), because two lines together would be longer than 30 characters.

**What happens when a paragraph is too big for the chunk size?**

```python
splitter = CharacterTextSplitter(separator="\n\n", chunk_size=30, chunk_overlap=0)
chunks = splitter.split_text(para)
print([len(c) for c in chunks])
```

You will see a warning like `Created a chunk of size 44, which is longer than the specified 30`, and the chunks stay as big paragraphs. **`CharacterTextSplitter` only uses ONE separator.** If a piece is too large, it does not know what else to try. This is the exact problem the *recursive* splitter solves.

> **Takeaway:** `CharacterTextSplitter` is simple and predictable, but it is not smart. Use it when your text has a reliable single separator.



## 9. Recursively Split by Character

This is the splitter **recommended for generic text**.

### The idea (baby version)

Imagine you must cut a long cake into pieces no bigger than your palm. You try the **biggest natural cut first**:

1. First try cutting between **paragraphs** (`"\n\n"`).
2. A piece still too big? Cut between **lines** (`"\n"`).
3. Still too big? Cut between **words** (`" "`).
4. Still too big? Cut between **letters** (`""`), the last resort.

That is **recursion**: "try the next separator on any piece that is still too big". The default separator list is `["\n\n", "\n", " ", ""]`.

- **How the text is split:** by a list of separators, in order.
- **How chunk size is measured:** by number of characters (or whatever `length_function` says).

### Basic usage

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)

texts = text_splitter.create_documents([companypolicies])
print("Number of chunks:", len(texts))
for t in texts[:3]:
    print(repr(t.page_content))
```

### See the "stay together" behaviour

Using the sentence-level story with `chunk_size=60` and `chunk_overlap=10`:

```python
splitter = RecursiveCharacterTextSplitter(chunk_size=60, chunk_overlap=10)
for chunk in splitter.split_text(story):
    print(repr(chunk))
```

**Output:**

```
'The cat sat on the mat. It was a sunny day. The cat was very'
'was very happy. Then a dog came. The dog barked loudly. The'
'The cat ran away.'
```

Compare with `CharacterTextSplitter(separator="")`: this time **no word is cut in half**. The recursive splitter fell back to cutting on spaces (words) rather than letters.

### Same paragraphs, small chunk size: no more warnings

```python
splitter = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=0)
for chunk in splitter.split_text(para):
    print(repr(chunk))
```

Because the recursive splitter can fall back from `"\n\n"` to `"\n"` to `" "`, it **always respects chunk size** (except in extreme cases such as one giant word).

### Customising the separators

You can supply your own list. For example, to prefer splitting at sentence ends:

```python
sentence_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ". ", " ", ""],  # added ". " for sentences
    chunk_size=80,
    chunk_overlap=10,
)
for chunk in sentence_splitter.split_text(story):
    print(repr(chunk))
```

### Character vs. Recursive: side by side

| Feature | `CharacterTextSplitter` | `RecursiveCharacterTextSplitter` |
|---|---|---|
| Number of separators | One | A list, tried in order |
| Handles oversize pieces | No (warns, keeps them big) | Yes (tries the next separator) |
| Keeps paragraphs/sentences together | Only if the separator matches | Yes, as much as possible |
| Recommended for general text | Sometimes | **Yes, the default choice** |


## 10. Split Code

Code is not like normal text. A function should stay in one piece. The `RecursiveCharacterTextSplitter` can use **language-aware separators**, so it cuts at `class`, `def`, `function`, and similar keywords **before** falling back to blank lines and spaces.

> **Correction to the original lesson:** the original showed the *normal* recursive splitter here by mistake, and used `Language` without importing it. The correct imports are below.

### Which languages are supported?

```python
from langchain_text_splitters import Language

print([lang.value for lang in Language])
```

Typical output includes: `cpp, go, java, kotlin, js, ts, php, proto, python, r, rst, ruby, rust, scala, swift, markdown, latex, html, sol, csharp, cobol, c, lua, perl, haskell, elixir, powershell` (the exact list depends on your version).

### Python

The main difference from the plain recursive splitter is that you call **`.from_language(...)`** and choose a `language`. Everything else stays the same.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
python_docs = python_splitter.create_documents([PYTHON_CODE])
for d in python_docs:
    print(repr(d.page_content))
```

**Output:**

```
'def hello_world():\n    print("Hello, World!")'
'# Call the function\nhello_world()'
```

The function definition stays in **one** chunk, and the call stays in another.

### Peek at the separators used for Python

```python
RecursiveCharacterTextSplitter.get_separators_for_language(Language.PYTHON)
```

```
['\nclass ', '\ndef ', '\n\tdef ', '\n\n', '\n', ' ', '']
```

Read it like this: *"First try to cut before a `class`. If pieces are still too big, cut before a `def`. Then before an indented `def` (a method). Then blank lines, lines, words, letters."*

### JavaScript

> **Correction:** the original text said "separators for JSON language", but the code is for **JavaScript** (`Language.JS`).

```python
print(RecursiveCharacterTextSplitter.get_separators_for_language(Language.JS))

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
js_docs = js_splitter.create_documents([JS_CODE])
for d in js_docs:
    print(repr(d.page_content))
```

The JS separator list begins with `['\nfunction ', '\nconst ', '\nlet ', '\nvar ', '\nclass ', ...]`, so functions and declarations are cut at their starts.

### Other languages

The same recipe works for Java, Go, Rust, C++, PHP, Ruby, Markdown, LaTeX, HTML, and more. Change only `Language.XXX`:

```python
java_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JAVA, chunk_size=200, chunk_overlap=20
)
```

More details: [LangChain code splitter docs](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/code_splitter/).


## 11. Markdown Header Text Splitter

### The idea (baby version)

A book has **chapters**. If you tear pages randomly, a page about "Cats" could be glued to a page about "Dogs". It is much better to tear the book **at chapter boundaries**.

Markdown files have chapters too: they are the **headers** (`#`, `##`, `###`). `MarkdownHeaderTextSplitter` cuts the file at those headers and stores the header names in **metadata**.

> **Correction:** the original lesson used `headers_to_split_on` and `md` without ever defining them. Here is the complete, runnable version.

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

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_header_splits = markdown_splitter.split_text(md)
for d in md_header_splits:
    print(d)
```

**Output:**

```
page_content='Intro to pets.' metadata={'Header 1': 'Pets'}
page_content='Cats purr.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats'}
page_content='Kittens are tiny.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats', 'Header 3': 'Kittens'}
page_content='Dogs bark.' metadata={'Header 1': 'Pets', 'Header 2': 'Dogs'}
```

Look closely at the metadata of "Kittens are tiny.": it remembers the **whole path** `Pets > Cats > Kittens`. This is like a mailing address for the chunk. 📮

### Keeping the headers inside the text with `strip_headers=False`

By default the header lines are **removed** from `page_content` (they live in the metadata). If you want them to stay in the text too, set `strip_headers=False`:

```python
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False,
)
for d in markdown_splitter.split_text(md):
    print(d)
```

**Output:**

```
page_content='# Pets\nIntro to pets.' metadata={'Header 1': 'Pets'}
page_content='## Cats\nCats purr.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats'}
page_content='### Kittens\nKittens are tiny.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats', 'Header 3': 'Kittens'}
page_content='## Dogs\nDogs bark.' metadata={'Header 1': 'Pets', 'Header 2': 'Dogs'}
```

### Why keep the header in the text?

When you later **embed** the chunk (turn it into numbers), the embedding only sees `page_content`, not `metadata`. If the header text is missing, the chunk "Cats purr." has less meaning. Keeping the header often improves search quality.


## 12. Split by HTML

Web pages are built from tags such as `<h1>`, `<h2>`, and `<p>`. HTML splitters are **structure-aware**: they use these tags as natural cutting lines, just like Markdown headers.

> **Requires:** `lxml` (installed in Section 4).

Here is the sample HTML used by both splitters below:

```python
html_string = """
<!DOCTYPE html>
<html>
<body>
    <div>
        <h1>Foo</h1>
        <p>Some intro text about Foo.</p>
        <div>
            <h2>Bar main section</h2>
            <p>Some intro text about Bar.</p>
            <h3>Bar subsection 1</h3>
            <p>Some text about the first subtopic of Bar.</p>
            <h3>Bar subsection 2</h3>
            <p>Some text about the second subtopic of Bar.</p>
        </div>
        <div>
            <h2>Baz</h2>
            <p>Some text about Baz</p>
        </div>
        <br>
        <p>Some concluding text about Foo</p>
    </div>
</body>
</html>
"""

headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
]
```

### 12.1 Split by HTML header: `HTMLHeaderTextSplitter`

It works like `MarkdownHeaderTextSplitter`, but for HTML. It splits at the element level and adds metadata for each relevant header. The goals are to (a) keep related text together and (b) keep the context that the document structure carries.

```python
from langchain_text_splitters import HTMLHeaderTextSplitter

html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
html_header_splits = html_splitter.split_text(html_string)
for d in html_header_splits:
    print(d)
```

On a smaller page (`<h1>Foo</h1><p>Intro Foo.</p><div><h2>Bar</h2><p>Intro Bar.</p><h3>Sub 1</h3><p>Text 1.</p></div>...`) the output looks like this:

```
page_content='Foo' metadata={'Header 1': 'Foo'}
page_content='Intro Foo.' metadata={'Header 1': 'Foo'}
page_content='Bar' metadata={'Header 1': 'Foo', 'Header 2': 'Bar'}
page_content='Intro Bar.' metadata={'Header 1': 'Foo', 'Header 2': 'Bar'}
page_content='Sub 1' metadata={'Header 1': 'Foo', 'Header 2': 'Bar', 'Header 3': 'Sub 1'}
page_content='Text 1.' metadata={'Header 1': 'Foo', 'Header 2': 'Bar', 'Header 3': 'Sub 1'}
```

Notice that each paragraph carries the **full header path** in its metadata.

### 12.2 Split by HTML section: `HTMLSectionSplitter`

This one is also structure-aware, but it groups **the header text and its content together** in one chunk, one section at a time.

```python
from langchain_text_splitters import HTMLSectionSplitter

html_splitter = HTMLSectionSplitter(headers_to_split_on=headers_to_split_on)
html_section_splits = html_splitter.split_text(html_string)
for d in html_section_splits:
    print(d)
```

On the same small page, the output looks like this:

```
page_content='Foo \n Intro Foo.' metadata={'Header 1': 'Foo'}
page_content='Bar \n Intro Bar.' metadata={'Header 2': 'Bar'}
page_content='Sub 1 \n Text 1.' metadata={'Header 3': 'Sub 1'}
page_content='Baz \n Text Baz' metadata={'Header 2': 'Baz'}
```

### Header splitter vs. Section splitter

| | `HTMLHeaderTextSplitter` | `HTMLSectionSplitter` |
|---|---|---|
| Header text appears in `page_content` | No (only in metadata) | **Yes** |
| Metadata path | Full path (H1 > H2 > H3) | Only the section's own header |
| Chunk granularity | Element by element | Section by section |
| Good for | Rich metadata and filtering | Self-contained section chunks |

### Splitting a live web page

You can also pass a URL (needs internet):

```python
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
docs = html_splitter.split_text_from_url("https://example.com")
```

## 13. Split JSON

Sometimes your data is **JSON** (API results, config files). `RecursiveJsonSplitter` splits it while keeping the JSON **valid**: it never cuts in the middle of a key or value.

```python
from langchain_text_splitters import RecursiveJsonSplitter

data = {
    "a": {"b": "x" * 30, "c": "y" * 30},
    "d": [1, 2, 3],
}

json_splitter = RecursiveJsonSplitter(max_chunk_size=60)
for chunk in json_splitter.split_text(data):
    print(chunk)
```

**Output:**

```
{"a": {"b": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "c": "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"}}
{"d": [1, 2, 3]}
```

Each chunk is a **complete, valid JSON object**. Note that `RecursiveJsonSplitter` takes `max_chunk_size` (no overlap option) and the size limit is soft: a single value that is too large will not be broken apart.


## 14. Split by Tokens

### Characters vs. tokens (baby version)

AI models do not read letters. They read **tokens**, which are small word-pieces. For example, `"unbelievable"` might be 3 tokens: `un`, `believ`, `able`. A rough rule of thumb for English is **1 token is about 4 characters, or about 0.75 of a word**.

Models limit how many **tokens** they accept, not how many characters. So if you care about staying under a model's limit, **measure in tokens**.

### Option A: `TokenTextSplitter`

```python
from langchain_text_splitters import TokenTextSplitter

token_splitter = TokenTextSplitter(
    encoding_name="cl100k_base",  # tokenizer used by many OpenAI models
    chunk_size=50,                # 50 TOKENS (not characters)
    chunk_overlap=5,
)
token_chunks = token_splitter.split_text(companypolicies)
print(len(token_chunks))
```

### Option B (often nicer): recursive splitting measured in tokens

This keeps the **smart separators** (paragraph, line, word) and only changes the **ruler** to tokens:

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

token_recursive = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    chunk_size=50,
    chunk_overlap=5,
)
chunks = token_recursive.split_text(companypolicies)
print(len(chunks))
```

### Option C: your own `length_function`

This is where `length_function` shines. Any function that takes a string and returns a number works:

```python
def word_count(text: str) -> int:
    return len(text.split())

word_splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,          # 20 WORDS
    chunk_overlap=3,
    length_function=word_count,
)
chunks = word_splitter.split_text(companypolicies)
print(len(chunks))
print(chunks[0])
```

> **Note:** `tiktoken` may need internet access the first time it runs, to download its vocabulary files.


## 15. Combining Splitters: A Two-Stage Pipeline

Real-world RAG almost always uses **two stages**:

1. **Stage 1: structure-aware** (Markdown/HTML header splitter): cut at chapters so each chunk is about one topic and gets header metadata.
2. **Stage 2: size-aware** (recursive splitter): if a chapter is still too big, cut it down.

Why? Header splitters do **not** limit chunk size. A chapter could be 5,000 characters long. Stage 2 fixes that **and keeps the header metadata** on every smaller piece.

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

# Stage 1: cut by chapters
stage1 = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on).split_text(md)

# Stage 2: make sure no chunk is bigger than chunk_size
stage2 = RecursiveCharacterTextSplitter(chunk_size=12, chunk_overlap=0)
final_docs = stage2.split_documents(stage1)

for d in final_docs:
    print(d)
```

**Output** (`chunk_size=12` is deliberately tiny, just to show the effect):

```
page_content='Intro to' metadata={'Header 1': 'Pets'}
page_content='pets.' metadata={'Header 1': 'Pets'}
page_content='Cats purr.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats'}
page_content='Kittens are' metadata={'Header 1': 'Pets', 'Header 2': 'Cats', 'Header 3': 'Kittens'}
page_content='tiny.' metadata={'Header 1': 'Pets', 'Header 2': 'Cats', 'Header 3': 'Kittens'}
page_content='Dogs bark.' metadata={'Header 1': 'Pets', 'Header 2': 'Dogs'}
```

Two things to notice:

- `"Intro to pets."` was too long for 12 characters, so it was split into two pieces.
- **Both pieces still carry** `{'Header 1': 'Pets'}`. The label was not lost.

The same two-stage idea works for HTML: `HTMLHeaderTextSplitter` first, then `RecursiveCharacterTextSplitter.split_documents(...)`.


## 16. How to Choose `chunk_size` and `chunk_overlap`

There is no single perfect number. Use these starting points and then **test with real questions**.

| Content type | Suggested `chunk_size` (characters) | Suggested overlap |
|---|---|---|
| Short FAQs, chat messages | 200 to 400 | 0 to 40 |
| Policies, articles, documentation | 500 to 1000 | 50 to 150 (about 10 to 20%) |
| Long technical or legal text where context matters | 1000 to 2000 | 100 to 300 |
| Source code | 500 to 1500 (cut at functions/classes) | 0 to 100 |

### The balancing act

```
Small chunks  ◀─────────────────────────▶  Large chunks
+ precise search                           + more context per chunk
+ cheaper to embed                         + fewer chunks to manage
- may lose context                         - search gets "blurry"
- many more chunks                         - uses more of the model's window
```

### A simple testing recipe

1. Write 10 realistic questions your users might ask.
2. Split with `chunk_size=300`, then `600`, then `1000`.
3. For each setting, check: *does the retrieved chunk actually contain the answer?*
4. Keep the setting that finds the answer most often.

### Handy chunk statistics

```python
chunks = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20).split_text(companypolicies)
sizes = [len(c) for c in chunks]
print("chunks:", len(sizes))
print("smallest:", min(sizes), "| largest:", max(sizes), "| average:", sum(sizes) // len(sizes))
```


## 17. Which Splitter Should I Use?

| Your data | Best splitter |
|---|---|
| Plain text, articles, general documents | `RecursiveCharacterTextSplitter` |
| Text with one reliable separator (for example, one record per paragraph) | `CharacterTextSplitter` |
| Python, JS, Java, and other code | `RecursiveCharacterTextSplitter.from_language(...)` |
| Markdown notes, READMEs, docs | `MarkdownHeaderTextSplitter` (then Recursive) |
| Web pages / HTML | `HTMLHeaderTextSplitter` or `HTMLSectionSplitter` (then Recursive) |
| LaTeX papers | `RecursiveCharacterTextSplitter.from_language(Language.LATEX)` |
| JSON / API data | `RecursiveJsonSplitter` |
| You must obey a model's token limit | `from_tiktoken_encoder(...)` or `TokenTextSplitter` |

**When unsure:** start with `RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)`. It is a safe default.


## 18. Common Mistakes and Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| `ValueError: Got a larger chunk overlap than chunk size` | `chunk_overlap >= chunk_size` | Make overlap smaller (about 10 to 20% of chunk size) |
| Warning: `Created a chunk of size X, which is longer than the specified Y` | `CharacterTextSplitter` found a piece bigger than `chunk_size` with no other separator to try | Use `RecursiveCharacterTextSplitter` |
| `NameError: name 'Language' is not defined` | Forgot the import | `from langchain_text_splitters import Language` |
| `NameError: name 'headers_to_split_on' is not defined` | The list was never created | Define it before creating the splitter (see Section 11) |
| Words are cut in half | Used `separator=""` | Use the recursive splitter with the default separators |
| LaTeX text looks broken (strange characters where `\begin` should be) | In a normal Python string, `\b` means *backspace* | Use a **raw string**: `r"""\begin{document} ..."""` |
| Header chunks are huge | Header splitters do not limit size | Add Stage 2 with `RecursiveCharacterTextSplitter` (Section 15) |
| Metadata disappears after splitting | Used `split_text` on strings | Use `create_documents(..., metadatas=...)` or `split_documents(...)` |
| `HTMLSectionSplitter` import or parse error | `lxml` is not installed | `pip install lxml` |
| Chunk count looks different from a friend's | Different library versions or text encoding | Pin versions (Section 4) and read files with `encoding="utf-8"` |


## 19. Summary

- **Splitting** cuts long text into chunks the AI can handle. It is the "slicing the pizza" step of RAG.
- **`chunk_size`** is the maximum slice size. **`chunk_overlap`** is the shared edge between slices. **`length_function`** is the ruler. **`separator(s)`** are the dotted lines.
- A **`Document`** has `page_content` (text) and `metadata` (labels).
- Use `split_text` for strings, `create_documents` to add metadata, and `split_documents` to split existing `Document`s.
- **`CharacterTextSplitter`** uses one separator. It is simple but not smart.
- **`RecursiveCharacterTextSplitter`** tries a list of separators. It is the **default recommendation**.
- **`from_language(...)`** makes the recursive splitter understand code and LaTeX.
- **Markdown/HTML header splitters** cut by document structure and store header paths in metadata.
- Use a **two-stage pipeline** (structure first, then size) for the best chunks.
- Test your settings with **real questions**. Good chunks lead to good retrieval, which leads to good answers.


## 20. Exercises

### Exercise 1: Change the separator for `CharacterTextSplitter`

Use `CharacterTextSplitter` on `companypolicies` with `separator="\n"`, `chunk_size=200`, `chunk_overlap=20`.

1. How many chunks do you get?
2. Print the first chunk.
3. Repeat with `separator="\n\n"` and `separator=""`. How do the number of chunks and the chunk boundaries change? Which one cuts words in half?

### Exercise 2: Split LaTeX code

Split the LaTeX text below using `RecursiveCharacterTextSplitter.from_language(language=Language.LATEX, ...)` with `chunk_size=150` and `chunk_overlap=0`. Print each chunk with its number.

> **Hint:** the original lab used a normal string here. Use a **raw string** (`r"""..."""`) so that `\begin` is not read as a backspace.

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

### Exercise 3 (Capstone): Build a mini RAG "retrieval" step

Build the **Split → Retrieve** part of a RAG system for this Markdown employee handbook:

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

**Tasks:**

1. Split `handbook_md` in **two stages**: `MarkdownHeaderTextSplitter` (keep the headers in the text), then `RecursiveCharacterTextSplitter` with `chunk_size=200` and `chunk_overlap=30`.
2. Print each chunk's text and its metadata.
3. Write a function `retrieve(question, docs, k=2)` that returns the `k` chunks sharing the **most words** with the question. (Real RAG uses embeddings, but word overlap is enough to see the idea.)
4. Test it with: *"How many days of sick leave do I get?"* and *"How often must I change my password?"*
5. Reflect: what would happen if you had used `chunk_size=1000`? What if you had used `chunk_size=40`?

## 21. Solutions

### Solution 1: Changing the separator

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
    label = repr(sep)
    print(f"separator={label:6} -> {len(docs)} chunks")
    print("  first chunk:", repr(docs[0].page_content[:80]), "...")
    print()
```

**Interpretation:**

- With `separator="\n"`, the splitter cuts at line breaks, then **merges lines back together** until adding another line would exceed 200 characters. Chunks end at **whole lines**, so sentences are kept intact. Overlap is only applied when whole lines fit inside the overlap size, so it may be smaller than 20 characters or absent.
- With `separator="\n\n"`, the splitter treats each **blank-line-separated block** (one policy section) as a unit. In our sample, each numbered section is roughly 200 to 300 characters, so you will usually get about **one chunk per section**. If a section is larger than 200 characters, you may see the warning `Created a chunk of size ..., which is longer than the specified 200`. The splitter keeps it whole because it has only one separator.
- With `separator=""`, the text is cut **every 200 characters regardless of meaning**, so words can be cut in half. This is the least intelligent option.

**Lesson learned:** the separator decides *where cuts are allowed*; `chunk_size` decides *how much is merged back together*. The exact chunk counts depend on your document, so run the code and compare.

### Solution 2: Splitting LaTeX

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

# Configure the LaTeX text splitter
latex_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.LATEX, chunk_size=150, chunk_overlap=0
)

# Split the document
latex_docs = latex_splitter.create_documents([latex_text])
for i, doc in enumerate(latex_docs):
    print(f"Chunk {i + 1}:")
    print(doc.page_content)
    print("-" * 50)
```

**Interpretation:** the LaTeX separators prefer cutting **before `\section`, `\subsection`, and similar commands**, then fall back to paragraphs, lines, and words. Therefore each section starts a new chunk when possible. Because the paragraphs here are long (about 300 characters) and `chunk_size` is only 150, the splitter then cuts those paragraphs on spaces (words), so you will see each long section broken into several chunks. Try `chunk_size=400` and compare: sections now stay in one piece.

**A smaller verified example** (`chunk_size=100`, `chunk_overlap=0`) on a shorter LaTeX text:

```python
lt = r"""\documentclass{article}
\begin{document}
\section{Introduction}
Large language models are big. They learn from text. They are useful.
\subsection{History}
Early models were small. Newer ones are huge.
\end{document}"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.LATEX, chunk_size=100, chunk_overlap=0
)
for d in splitter.create_documents([lt]):
    print(repr(d.page_content))
```

```
'\\documentclass{article}\n\\begin{document}'
'\\section{Introduction}\nLarge language models are big. They learn from text. They are useful.'
'\\subsection{History}\nEarly models were small. Newer ones are huge.'
```

(`repr` shows each backslash doubled; the real text has a single backslash.) Each `\section` / `\subsection` starts its own chunk.

### Solution 3 (Capstone): Mini RAG split and retrieve

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
    strip_headers=False,          # keep the header text inside page_content
).split_text(handbook_md)

stage2 = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
docs = stage2.split_documents(stage1)

# ---------- Task 2: inspect chunks ----------
for i, d in enumerate(docs, start=1):
    print(f"Chunk {i} | {len(d.page_content)} chars")
    print("  text    :", repr(d.page_content))
    print("  metadata:", d.metadata)
    print()

# ---------- Task 3: a tiny keyword retriever ----------
STOPWORDS = {"the", "a", "an", "of", "do", "i", "how", "many", "must", "is", "to", "get", "my", "often"}

def tokenize(text):
    words = re.findall(r"[a-z0-9']+", text.lower())
    return {w for w in words if w not in STOPWORDS}

def retrieve(question, docs, k=2):
    q_words = tokenize(question)
    scored = []
    for d in docs:
        overlap = len(q_words & tokenize(d.page_content))
        scored.append((overlap, d))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored[:k]

# ---------- Task 4: test ----------
questions = [
    "How many days of sick leave do I get?",
    "How often must I change my password?",
]

for q in questions:
    print("QUESTION:", q)
    for score, d in retrieve(q, docs, k=2):
        print(f"  score={score} | {d.metadata}")
        print(f"  {d.page_content[:90]!r}...")
    print()
```

**What you should see (the important parts):**

- For the **sick leave** question, the top chunk has metadata `{'Header 1': 'Employee Handbook', 'Header 2': 'Leave Policy', 'Header 3': 'Sick Leave'}` and contains *"Sick leave is granted for up to 10 days per year..."*.
- For the **password** question, the top chunk comes from the `Information Security` section. Because that section is longer than 200 characters, the recursive splitter may cut it into two chunks. The password sentence appears in the first one, and **both pieces carry the same header metadata**.

The exact chunk boundaries can vary slightly with your library version, so print and check them yourself.

#### Task 5: Reflection answers

| Setting | What happens | Why it matters |
|---|---|---|
| `chunk_size=1000` | Stage 2 does almost nothing, since every section already fits. Each chunk is one whole section, so retrieval is still good here. | On a *bigger* handbook, a 1000-character chunk could mix several rules, so a question might retrieve a large chunk with mostly irrelevant text. |
| `chunk_size=40` | Sentences are chopped into tiny fragments such as `"Passwords must be at least 12"` / `"characters long and changed"`. | The fragments lose meaning. A fragment like `"every 90 days."` alone does not say what happens every 90 days. Retrieval gets worse. |
| `chunk_size=200` (our choice) | About one or two sentences per chunk, still tagged with their section headers. | A good balance for short policy text: each chunk holds one clear idea. |

**Big idea:** *header metadata + sensibly sized chunks* give the retriever **precise** pieces that still **make sense on their own**. This is exactly why we study text splitting before building a full RAG system.


### Bonus Challenge

1. Replace the word-overlap retriever with an **embedding-based** retriever (for example, using `FAISS` or `Chroma` and an embeddings model) and compare results.
2. Try `chunk_size` values of 100, 200, 400, and 800 and record how often the correct chunk ranks first for 10 questions you write yourself.
3. Convert `handbook_md` to HTML and repeat the exercise using `HTMLHeaderTextSplitter`.

