# Lesson 1 How to Load Your Document from Different Sources 

What you will learn
- Describe how LangChain uses document loaders to simplify data integration
- Explain how to load different types of files
- Discuss how to load content directly from websites and handle unstructured files

## LangChain Document Loaders
- LangChain uses document loaders to gather information and prepare it for further use
- Document loaders act as connectors, pulling in data and converting it into a LangChain friendly format
- Collecting necessary information is step one to create a RAG application 
- Collected data is processed to find relevant answers
- Application can access and use a wide range of information

## Load Documents Using LangChain for Different Sources 

Imagine you are working as a data scientist at a consulting firm, and you've been tasked with analyzing documents from multiple clients. Each client provides their data in different formats: some in PDFs, others in Word documents, CSV files, or even HTML webpages. Manually loading and parsing each document type is not only time-consuming but also prone to errors. Your goal is to streamline this process, making it efficient and error-free.

To achieve this, you'll use LangChain’s powerful document loaders. These loaders allow you to read and convert various file formats into a unified document structure that can be easily processed. For example, you'll load client policy documents from text files, financial reports from PDFs, marketing strategies from Word documents, and product reviews from JSON files. By the end of this lab, you will have a robust pipeline that can handle any new file formats clients might send, saving you valuable time and effort.

In this Lesson, you will explore how to use various loaders provided by LangChain to load and process data from different file formats. These loaders simplify the task of reading and converting files into a document format that can be processed downstream. By the end of this lesson, you will be able to efficiently load text, PDF, Markdown, JSON, CSV, DOCX, and other file formats into a unified format, allowing for seamless data analysis and manipulation for LLM applications.

## Objectives

After completing this lab you will be able to:

 - Understand how to use `TextLoader` to load text files.
 - Learn how to load PDFs using `PyPDFLoader` and `PyMuPDFLoader`.
 - Use `UnstructuredMarkdownLoader` to load Markdown files.
 - Load JSON files with `JSONLoader` using jq schemas.
 - Process CSV files with `CSVLoader` and `UnstructuredCSVLoader`.
 - Load Webpage content using `WebBaseLoader`.
 - Load Word documents using `Docx2txtLoader`.
 - Utilize `UnstructuredFileLoader` for various file types.

### Load from TXT files
- The `TextLoader` is a tool designed to load textual data from various sources.
- It is the simplest loader, reading a file as text and placing all the content into a single document.

```
loader = TextLoader("MyPolicies.txt")
loader
data = loader.load()
data
pprint(data[0].page_content[:1000])

```

### Load from PDF files

Sometimes, we may have files in PDF format that we want to load for processing.
LangChain provides several classes for loading PDFs. Here, we introduce two classes: `PyPDFLoader` and `PyMuPDFLoader`.

#### PyPDFLoader
Load the PDF using `PyPDFLoader` into an array of documents, where each document contains the page content and metadata with the page number.

```
pdf_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Q81D33CdRLK6LswuQrANQQ/instructlab.pdf"
loader = PyPDFLoader(pdf_url)
pages = loader.load_and_split()
print(pages[0])
# Display the first three pages of the PDF.
for p,page in enumerate(pages[0:3]):
    print(f"page number {p+1}")
    print(page)

```

#### PyMuPDFLoader
`PyMuPDFLoader` is the fastest of the PDF parsing options. It provides detailed metadata about the PDF and its pages, and returns one document per page.

```
loader = PyMuPDFLoader(pdf_url)
loader
data = loader.load()
print(data[0])
```

The `metadata` attribute reveals that `PyMuPDFLoader` provides more detailed metadata information than `PyPDFLoader`.

### Load from Markdown files

Sometimes, our file source might be in Markdown format. LangChain provides the `UnstructuredMarkdownLoader` to load content from Markdown files.

```
!wget 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/eMSP5vJjj9yOfAacLZRWsg/markdown-sample.md'
markdown_path = "markdown-sample.md"
loader = UnstructuredMarkdownLoader(markdown_path)
loader
data = loader.load()
data
```
### Load from JSON files
The JSONLoader uses a specified [jq schema](https://en.wikipedia.org/wiki/Jq_(programming_language)) to parse the JSON files. It uses the jq python package, which we've installed before.
```
!wget 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/hAmzVJeOUAMHzmhUHNdAUg/facebook-chat.json'
file_path='facebook-chat.json'
data = json.loads(Path(file_path).read_text())
pprint(data)
```

We use `JSONLoader` to load data from the JSON file. However, JSON files can have various attribute-value pairs. If we want to load a specific attribute and its value, we need to set an appropriate `jq schema`.

So for example, if we want to load the `content` from the JSON file, we need to set `jq_schema='.messages[].content'`.

```
loader = JSONLoader(
    file_path=file_path,
    jq_schema='.messages[].content',
    text_content=False)

data = loader.load()
pprint(data)

```

### Load from CSV files

CSV files are a common format for storing tabular data. The `CSVLoader` provides a convenient way to read and process this data.

```
!wget 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IygVG_j0M87BM4Z0zFsBMA/mlb-teams-2012.csv'
loader = CSVLoader(file_path='mlb-teams-2012.csv')
data = loader.load()
data
```
When you load data from a CSV file, the loader typically creates a separate `Document` object for each row of data in the CSV.

#### UnstructuredCSVLoader

In contrast to `CSVLoader`, which treats each row as an individual document with headers defining the data, `UnstructuredCSVLoader` considers the entire CSV file as a single unstructured table element. This approach is beneficial when you want to analyze the data as a complete table rather than as separate entries.

```
loader = UnstructuredCSVLoader(
    file_path="mlb-teams-2012.csv", mode="elements"
)
data = loader.load()
data[0].page_content
print(data[0].metadata["text_as_html"])
```

### Load from URL/Website files

Usually we use `BeautifulSoup` package to load and parse a HTML or XML file. But it has some limitations.

The following code is using `BeautifulSoup` to parse a website. Let's see what limitation it has.

```
import requests
from bs4 import BeautifulSoup

url = 'https://www.ibm.com/topics/langchain'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())

```

From the print output, we can see that `BeautifulSoup` not only load the web content, but also a lot of HTML tags and external links, which are not necessary if we just want to load the text content of the web.
So LangChain's `WebBaseLoader` can effectively address this limitation. `WebBaseLoader` is designed to extract all text from HTML webpages and convert it into a document format suitable for further processing.

#### Load from single web page

```
loader = WebBaseLoader("https://www.ibm.com/topics/langchain")
data = loader.load()
data
```

#### Load from multiple web pages

You can load multiple webpages simultaneously by passing a list of URLs to the loader. This will return a list of documents corresponding to the order of the URLs provided.

```
loader = WebBaseLoader(["https://www.ibm.com/topics/langchain", "https://www.redhat.com/en/topics/ai/what-is-instructlab"])
data = loader.load()
data
```

### Load from WORD files

`Docx2txtLoader` is utilized to convert Word documents into a document format suitable for further processing.

```
!wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/94hiHUNLZdb0bLMkrCh79g/file-sample.docx"
loader = Docx2txtLoader("file-sample.docx")
data = loader.load()
data
```

### Load from Unstructured Files

Sometimes, we need to load content from various text sources and formats without writing a separate loader for each one. Additionally, when a new file format emerges, we want to save time by not having to write a new loader for it. `UnstructuredFileLoader` addresses this need by supporting the loading of multiple file types. Currently, `UnstructuredFileLoader` can handle text files, PowerPoints, HTML, PDFs, images, and more.

For example, we can load `.txt` file.

```
loader = UnstructuredFileLoader("new-Policies.txt")
data = loader.load()
data
```

We also can load `.md` file.

```
loader = UnstructuredFileLoader("markdown-sample.md")
data = loader.load()
data
```

