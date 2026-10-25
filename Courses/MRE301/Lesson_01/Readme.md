# Lesson 1 How to Load Your Documents from Different Sources

**Learning Outcomes**

After completing this lesson you will be able to:

- Describe how LangChain uses **document loaders** to simplify data integration.
- Explain how to load different types of files into one unified format.
- Load content directly from **websites** and handle **unstructured** files.
- Use these loaders:

| Format | Loader(s) covered |
|---|---|
| Text | `TextLoader` |
| PDF | `PyPDFLoader`, `PyMuPDFLoader` |
| Markdown | `UnstructuredMarkdownLoader` |
| JSON | `JSONLoader` (with `jq` schemas) |
| CSV | `CSVLoader`, `UnstructuredCSVLoader` |
| Web pages | `WebBaseLoader` |
| Word | `Docx2txtLoader` |
| Excel | `UnstructuredExcelLoader`, `pandas` + `DataFrameLoader` |
| PowerPoint | `UnstructuredPowerPointLoader`, `python-pptx` |
| Anything else | `UnstructuredFileLoader` |

**Scenario**

Imagine you are a data scientist at a consulting firm. Each client sends data in a different format: PDFs, Word documents, CSV files, Excel workbooks, PowerPoint decks, or HTML webpages. Loading and parsing each type by hand is slow and error-prone.

Your goal is a **single, reliable pipeline** that converts every format into the same structure. In this lesson you will load:

- client policy documents from **text** files
- financial reports from **PDFs**
- marketing strategies from **Word** documents
- product reviews from **JSON** files
- budgets and sales figures from **Excel** workbooks
- pitch decks from **PowerPoint** files

By the end, you will have a pipeline that can absorb new formats with minimal effort.


**Background: What Is a Document Loader?**

- Document loaders are **connectors**: they pull in data and convert it into a LangChain-friendly format.
- Collecting data is **step one** of any RAG (Retrieval-Augmented Generation) application.
- The collected data is later split, embedded, and searched to find relevant answers.
- Loading from many sources lets your application use a wide range of information.

**The `Document` object**

Every loader returns a **list of `Document` objects**. Each one has two parts:

| Attribute | Description |
|---|---|
| `page_content` | The text content (a string) |
| `metadata` | A dictionary describing the source (file name, page number, row, etc.) |

```
Source file  ──►  Loader  ──►  [Document, Document, ...]  ──►  Splitter  ──►  Embeddings  ──►  Vector store
```

**Loader Cheat Sheet**

| File type | Loader | Documents returned |
|---|---|---|
| `.txt` | `TextLoader` | One for the whole file |
| `.pdf` | `PyPDFLoader` / `PyMuPDFLoader` | One per page |
| `.md` | `UnstructuredMarkdownLoader` | One for the whole file (default) |
| `.json` | `JSONLoader` | One per extracted item |
| `.csv` | `CSVLoader` | One per row |
| `.csv` | `UnstructuredCSVLoader` | One table element |
| URL | `WebBaseLoader` | One per URL |
| `.docx` | `Docx2txtLoader` | One for the whole file |
| `.xlsx` / `.xls` | `UnstructuredExcelLoader` | One per workbook (or per sheet in `elements` mode) |
| `.pptx` | `UnstructuredPowerPointLoader` | One per deck (or per element in `elements` mode) |
| Mixed | `UnstructuredFileLoader` | Depends on the file type |

**Setup Environment**

Install the required packages:

```bash
pip install langchain langchain-community
pip install pypdf pymupdf
pip install "unstructured[md,docx,pptx,xlsx]"
pip install jq docx2txt beautifulsoup4
pip install pandas openpyxl python-pptx
```

> **Note:** `jq` can be difficult to install on Windows. Use WSL, or use a pre-configured notebook environment.

Common imports used in this lesson:

```python
import json
from pathlib import Path
from pprint import pprint

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    PyMuPDFLoader,
    UnstructuredMarkdownLoader,
    JSONLoader,
    CSVLoader,
    UnstructuredCSVLoader,
    WebBaseLoader,
    Docx2txtLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader,
    UnstructuredFileLoader,
)
```


**Loading Files**

**6.1 Text (TXT)**

`TextLoader` is the simplest loader. It reads a file as text and places all the content into **a single document**.

```python
loader = TextLoader("MyPolicies.txt")
data = loader.load()
pprint(data[0].page_content[:1000])
```

**Tip:** if the file contains special characters, pass the encoding: `TextLoader("file.txt", encoding="utf-8")`.


**6.2 PDF**

LangChain provides several PDF loaders. Here are two.

**`PyPDFLoader`**

Loads the PDF into a list of documents. Each document holds the page content and metadata containing the **page number**.

```python
pdf_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Q81D33CdRLK6LswuQrANQQ/instructlab.pdf"

loader = PyPDFLoader(pdf_url)
pages = loader.load_and_split()
print(pages[0])

# Display the first three pages
for p, page in enumerate(pages[0:3]):
    print(f"page number {p + 1}")
    print(page)
```

**`PyMuPDFLoader`**

The **fastest** PDF parsing option. It returns one document per page and provides **more detailed metadata** than `PyPDFLoader`.

```python
loader = PyMuPDFLoader(pdf_url)
data = loader.load()
print(data[0])
```

| | `PyPDFLoader` | `PyMuPDFLoader` |
|---|---|---|
| Speed | Good | Fastest |
| Metadata | Basic (source, page) | Detailed (author, dates, producer, etc.) |
| Scanned PDFs (images) | No text without OCR | No text without OCR |

> **Scanned PDFs:** if a PDF contains only images, neither loader can extract text. Use an OCR-capable loader (for example `UnstructuredPDFLoader` with `strategy="ocr_only"`).


**6.3 Markdown**

Use `UnstructuredMarkdownLoader` for `.md` files.

```python
!wget 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/eMSP5vJjj9yOfAacLZRWsg/markdown-sample.md'

markdown_path = "markdown-sample.md"
loader = UnstructuredMarkdownLoader(markdown_path)
data = loader.load()
data
```

To keep each heading or list as its own element, use `mode="elements"`:

```python
loader = UnstructuredMarkdownLoader(markdown_path, mode="elements")
```


**6.4 JSON**

`JSONLoader` uses a [`jq` schema](https://en.wikipedia.org/wiki/Jq_(programming_language)) to decide which part of the JSON to load. It relies on the `jq` Python package.

**Step 1. Look at the raw structure:**

```python
!wget 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/hAmzVJeOUAMHzmhUHNdAUg/facebook-chat.json'

file_path = 'facebook-chat.json'
data = json.loads(Path(file_path).read_text())
pprint(data)
```

**Step 2. Choose the attribute with a `jq_schema`.** To load only the `content` of every message:

```python
loader = JSONLoader(
    file_path=file_path,
    jq_schema='.messages[].content',
    text_content=False,
)

data = loader.load()
pprint(data)
```

**Common `jq` patterns**

| Goal | `jq_schema` |
|---|---|
| All values of `content` inside `messages` | `.messages[].content` |
| Everything in the `messages` list | `.messages[]` |
| A single top-level key | `.title` |
| Nested key | `.data.items[].name` |

> Use `text_content=False` when the extracted values are not plain strings (for example objects or numbers).


**6.5 CSV**

CSV is a common format for tabular data.

**`CSVLoader`**

Creates **one `Document` per row**. Headers are used as labels for each value.

```python
!wget 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IygVG_j0M87BM4Z0zFsBMA/mlb-teams-2012.csv'

loader = CSVLoader(file_path='mlb-teams-2012.csv')
data = loader.load()
data
```

**`UnstructuredCSVLoader`**

Treats the **entire CSV as one table element**. This is useful when you want to analyse the data as a complete table rather than as separate entries.

```python
loader = UnstructuredCSVLoader(
    file_path="mlb-teams-2012.csv", mode="elements"
)
data = loader.load()

data[0].page_content
print(data[0].metadata["text_as_html"])
```

| | `CSVLoader` | `UnstructuredCSVLoader` |
|---|---|---|
| Granularity | One document per row | One document for the whole table |
| Best for | Row-level question answering | Table-level analysis |
| HTML table in metadata | No | Yes (`text_as_html`) |


**6.6 Websites (URL)**

`BeautifulSoup` can parse HTML, but it has a limitation: the output contains **many HTML tags and links** you usually do not need.

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.ibm.com/topics/langchain'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())
```

`WebBaseLoader` solves this by extracting the **text** of an HTML page and converting it into documents.

**Single web page**

```python
loader = WebBaseLoader("https://www.ibm.com/topics/langchain")
data = loader.load()
data
```

**Multiple web pages**

Pass a list of URLs. The documents come back **in the same order** as the URLs.

```python
loader = WebBaseLoader([
    "https://www.ibm.com/topics/langchain",
    "https://www.redhat.com/en/topics/ai/what-is-instructlab",
])
data = loader.load()
data
```

> **Good practice:** respect each site's terms of use and `robots.txt`, and avoid sending large numbers of rapid requests.


**6.7 Word (DOCX)**

`Docx2txtLoader` converts Word documents into the document format.

```python
!wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/94hiHUNLZdb0bLMkrCh79g/file-sample.docx"

loader = Docx2txtLoader("file-sample.docx")
data = loader.load()
data
```

> `Docx2txtLoader` extracts text only. Tables and images are not preserved as structure. For richer output, use `UnstructuredWordDocumentLoader`.


**6.8 Excel (XLSX / XLS)**

Excel workbooks often hold multiple sheets of tables. There are two good approaches.

**Method 1: `UnstructuredExcelLoader`**

```python
loader = UnstructuredExcelLoader("sales-report.xlsx", mode="elements")
data = loader.load()

print(data[0].page_content)
print(data[0].metadata["text_as_html"])   # table as HTML
print(data[0].metadata["page_name"])      # sheet name
```

| Mode | Result |
|---|---|
| `mode="single"` (default) | One document for the whole workbook |
| `mode="elements"` | One document per sheet, with an HTML version of the table in metadata |

**Method 2: `pandas` + `DataFrameLoader` (more control)**

Use this when you need to pick a specific sheet, skip header rows, clean data, or choose which column becomes the text.

```python
import pandas as pd
from langchain_community.document_loaders import DataFrameLoader

# Read one sheet (use sheet_name=None to read ALL sheets into a dict)
df = pd.read_excel("sales-report.xlsx", sheet_name="Q1", engine="openpyxl")

# Optional: build one text column from several columns
df["text"] = df.apply(
    lambda row: f"Region: {row['Region']}, Product: {row['Product']}, Sales: {row['Sales']}",
    axis=1,
)

loader = DataFrameLoader(df, page_content_column="text")
data = loader.load()
print(data[0])
```

**Reading all sheets**

```python
sheets = pd.read_excel("sales-report.xlsx", sheet_name=None, engine="openpyxl")

for sheet_name, df in sheets.items():
    print(f"Sheet: {sheet_name}, rows: {len(df)}")
```

**Which method should I use?**

| Need | Use |
|---|---|
| Quick load of a workbook | `UnstructuredExcelLoader` |
| Specific sheets, cleaning, custom text | `pandas` + `DataFrameLoader` |
| Legacy `.xls` files | `pandas` with `engine="xlrd"` (`pip install xlrd`) |


**6.9 PowerPoint (PPTX)**

**Method 1: `UnstructuredPowerPointLoader`**

```python
loader = UnstructuredPowerPointLoader("marketing-deck.pptx")
data = loader.load()
print(data[0].page_content[:500])
```

To keep slide structure, use `mode="elements"`. Each element (title, bullet, text block) becomes a document with a category and slide number in its metadata.

```python
loader = UnstructuredPowerPointLoader("marketing-deck.pptx", mode="elements")
data = loader.load()

for doc in data[:5]:
    print(doc.metadata.get("category"), "| slide", doc.metadata.get("page_number"))
    print(doc.page_content)
    print("---")
```

**Method 2: `python-pptx` (full control, including speaker notes)**

Use this when you need **speaker notes**, tables, or slide-by-slide output.

```python
from pptx import Presentation
from langchain_core.documents import Document

prs = Presentation("marketing-deck.pptx")
documents = []

for slide_number, slide in enumerate(prs.slides, start=1):
    texts = []

    for shape in slide.shapes:
        # Text boxes, titles, placeholders
        if shape.has_text_frame:
            for paragraph in shape.text_frame.paragraphs:
                line = "".join(run.text for run in paragraph.runs).strip()
                if line:
                    texts.append(line)

        # Tables
        if shape.has_table:
            for row in shape.table.rows:
                texts.append(" | ".join(cell.text for cell in row.cells))

    # Speaker notes
    notes = ""
    if slide.has_notes_slide:
        notes = slide.notes_slide.notes_text_frame.text

    documents.append(
        Document(
            page_content="\n".join(texts),
            metadata={
                "source": "marketing-deck.pptx",
                "slide": slide_number,
                "notes": notes,
            },
        )
    )

print(documents[0])
```

| Need | Use |
|---|---|
| Fast load of text from a deck | `UnstructuredPowerPointLoader` |
| Speaker notes, tables, custom metadata | `python-pptx` |
| Old `.ppt` files | Convert to `.pptx` first (for example with LibreOffice) |

> `python-pptx` reads `.pptx` only, not the older `.ppt` format. Text inside images is not extracted.

**6.10 Unstructured Files (Any Format)**

Sometimes you receive many formats and do not want to write a loader for each. `UnstructuredFileLoader` handles **multiple file types** with one class, including text, PowerPoint, HTML, PDF, images, and more. It also saves time when a new format appears.

**Load a `.txt` file**

```python
loader = UnstructuredFileLoader("new-Policies.txt")
data = loader.load()
data
```

**Load a `.md` file**

```python
loader = UnstructuredFileLoader("markdown-sample.md")
data = loader.load()
data
```

**Load multiple files with different formats**

```python
files = ["markdown-sample.md", "new-Policies.txt"]
loader = UnstructuredFileLoader(files)
data = loader.load()
data
```

**Inspecting a Loaded Document**

Always check what the loader returned before moving on.

```python
print(type(data))              # list
print(len(data))               # number of documents
print(data[0].page_content[:300])
print(data[0].metadata)
```

**Build a simple multi-format loader**

A small helper that routes files to the right loader by extension:

```python
from pathlib import Path

LOADERS = {
    ".txt":  TextLoader,
    ".pdf":  PyMuPDFLoader,
    ".md":   UnstructuredMarkdownLoader,
    ".csv":  CSVLoader,
    ".docx": Docx2txtLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".pptx": UnstructuredPowerPointLoader,
}

def load_any(path):
    ext = Path(path).suffix.lower()
    loader_cls = LOADERS.get(ext, UnstructuredFileLoader)   # fallback
    return loader_cls(str(path)).load()

docs = []
for file in Path("client_files").iterdir():
    docs.extend(load_any(file))

print(f"Loaded {len(docs)} documents")
```

**Choosing the Right Loader**

```
Is the file plain text?            -> TextLoader
Is it a PDF?                       -> PyMuPDFLoader (fast) or PyPDFLoader
Is it structured data?
    JSON                           -> JSONLoader + jq_schema
    CSV (row-based questions)      -> CSVLoader
    CSV (whole-table analysis)     -> UnstructuredCSVLoader
    Excel                          -> UnstructuredExcelLoader or pandas
Is it an Office document?
    Word                           -> Docx2txtLoader
    PowerPoint                     -> UnstructuredPowerPointLoader / python-pptx
Is it a web page?                  -> WebBaseLoader
Unknown or mixed formats?          -> UnstructuredFileLoader
```

**Common Errors and Fixes**

| Error | Likely cause | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'jq'` | `jq` not installed | `pip install jq` |
| `ImportError: ... unstructured` | Missing `unstructured` package | `pip install "unstructured[all-docs]"` |
| `ImportError: openpyxl` | Excel engine missing | `pip install openpyxl` |
| `ImportError: python-pptx` | PowerPoint dependency missing | `pip install python-pptx` |
| `UnicodeDecodeError` with `TextLoader` | Wrong encoding | `TextLoader(path, encoding="utf-8")` |
| Empty `page_content` from a PDF | Scanned PDF (images only) | Use an OCR-based loader |
| `JSONLoader` returns nothing | Wrong `jq_schema` | Print the raw JSON first and check the path |
| Old import path warnings | Loaders moved to `langchain_community` | Import from `langchain_community.document_loaders` |


**Practice Exercises**

1. **Compare PDF loaders.** Load the same PDF with `PyPDFLoader` and `PyMuPDFLoader`. Which metadata keys does each return?
2. **JSON extraction.** Change the `jq_schema` to extract a different field from `facebook-chat.json`.
3. **CSV granularity.** Load `mlb-teams-2012.csv` with both CSV loaders. How many documents does each return?
4. **Multiple URLs.** Load three web pages at once and print the first 200 characters of each.
5. **Excel challenge.** Create a workbook with two sheets. Load every sheet with `pandas` and print each sheet name with its row count.
6. **PowerPoint challenge.** Build a 3-slide deck with speaker notes. Use `python-pptx` to produce one `Document` per slide with the notes in metadata.
7. **Mini pipeline.** Put a `.txt`, `.pdf`, `.docx`, `.xlsx`, and `.pptx` file in one folder and load them all with the `load_any` helper.


**Summary**

- **Document loaders** connect your data to LangChain and return a list of `Document` objects.
- Each `Document` has `page_content` (text) and `metadata` (source details).
- Pick the loader that matches your file type: `TextLoader`, `PyPDFLoader`/`PyMuPDFLoader`, `UnstructuredMarkdownLoader`, `JSONLoader`, `CSVLoader`/`UnstructuredCSVLoader`, `WebBaseLoader`, `Docx2txtLoader`.
- For **Excel**, use `UnstructuredExcelLoader` for speed or `pandas` for control.
- For **PowerPoint**, use `UnstructuredPowerPointLoader` for speed or `python-pptx` when you need speaker notes and tables.
- Use `UnstructuredFileLoader` when formats are mixed or unknown.
- Loading is **step one** of RAG. Next you split, embed, and retrieve.


**Further Reading**

- [LangChain document loaders documentation](https://python.langchain.com/docs/integrations/document_loaders/)
- [Unstructured library documentation](https://docs.unstructured.io/)
- [pandas `read_excel` reference](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
- [python-pptx documentation](https://python-pptx.readthedocs.io/)
- [jq manual](https://jqlang.github.io/jq/manual/)
