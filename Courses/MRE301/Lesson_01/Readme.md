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


