# Lesson 2 Apply Text Splitting Techniques to Enhance Model Responsiveness

In many data processing tasks, especially those involving large documents, breaking down text into smaller, more manageable chunks is essential. Text splitters are tools specifically designed to accomplish this, ensuring that lengthy texts are divided into coherent segments. This division is crucial for maintaining the integrity and readability of the information, making it easier to handle and process. Effective text splitting helps prevent overwhelming systems with large, unwieldy blocks of text and ensures that each segment remains meaningful and contextually relevant.

The significance of text splitters becomes even more apparent in the context of retrieval-augmented generation (RAG). RAG involves fetching relevant pieces of information from a large dataset and using them to generate accurate and context-aware responses. Without properly split text, the retrieval process can become inefficient, potentially missing critical pieces of information or returning irrelevant data. By using text splitters to create well-defined chunks, the retrieval process can be streamlined, ensuring that the most relevant information is easily accessible. This not only enhances the efficiency of data retrieval but also improves the quality and relevance of the generated responses, making text splitters an important tool in the RAG workflow.

This lab will guide you about how to use some commonly used text splitters from LangChain to split your source document.

## Objectives

After completing this lab you will be able to:

 - Use commonly used text splitters from LangChain.
 - Split source documents into chunks for downstream use in RAG


For this lab, you will use the following libraries:

*   [`langchain`, `langchain-text-splitters`](https://www.langchain.com/) for using relevant features and text splitters from Langchain.
*   [`lxml`](https://pypi.org/project/lxml/) for libxml2 and libxslt libraries, which is used for splitting html text.

**Installing required libraries**
```
%%capture
!pip install "langchain==0.2.7"
!pip install "langchain-core==0.2.20"
!pip install "langchain-text-splitters==0.2.2"
!pip install "lxml==5.2.2"
```

## Text splitters

**Key parameters**

When using the splitter, you can customize several key parameters to fit your needs:
- **separator**: Define the characters that will be used for splitting the text.
- **chunk_size**: Specify the maximum size of your chunks to ensure they are as granular or broad as needed.
- **chunk_overlap**: Maintain context between chunks by setting the `chunk_overlap` parameter, which determines the number of characters that overlap between consecutive chunks. This helps ensure that information isn't lost at the chunk boundaries.
- **length_function**: Define how the length of chunks is calculated.


### Document object

Before introducing the splitters, let's take a look at the document object in LangChain, which is a data structure used to represent and manage text data in RAG process.

A Document object in LangChain contains information about some data. It has two attributes:

- `page_content: str`: The content of this document. Currently is only a string.
- `metadata: dict`: Arbitrary metadata associated with this document. Can track the document id, file name, etc.

```
from langchain_core.documents import Document
Document(page_content="""Python is an interpreted high-level general-purpose programming language. 
                        Python's design philosophy emphasizes code readability with its notable use of significant indentation.""",
         metadata={
             'my_document_id' : 234234,
             'my_document_source' : "About Python",
             'my_document_create_time' : 1680013019
         })
```

### Split by Character

This is the simplest method, which splits the text based on characters (by default `"\n\n"`) and measures chunk length by the number of characters.
- **How the text is split**: By single character.
- **How the chunk size is measured**: By number of characters.


Let's see how to implement this method using code.

In the following code, you will use `CharacterTextSplitter` to split the document by character. 
- Separator: Set to `''`, meaning that any character can act as a separator once the chunk size reaches the set limit.
- Chunk size: Set to `200`, meaning that once a chunk reaches 200 characters, it will be split.
- Chunk overlap: Set to `20`, meaning there will be `20` characters overlapping between chunks.
- Length function: Set to `len`.


```
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="",
    chunk_size=200,
    chunk_overlap=20,
    length_function=len,
)

texts = text_splitter.split_text(companypolicies)
texts
len(texts)

texts = text_splitter.create_documents([companypolicies], metadatas=[{"document":"Company Policies"}])  # pass the metadata as well

texts[0]
```

You will use `split_text` function to operate the split.

You can also use the following code to add metadata to the text, forming it into a `document` object using LangChain.

### Recursively Split by Character

This text splitter is the recommended one for generic text. It is parameterized by a list of characters, and it tries to split on them in order until the chunks are small enough. The default list is `["\n\n", "\n", " ", ""]`.

It processes the large text by attempting to split it by the first character, `\n\n`. If the first split by \n\n results in chunks that are still too large, it moves to the next character, `\n`, and attempts to split by it. This process continues through the list of characters until the chunks are less than the specified chunk size.

This method aims to keep all paragraphs (then sentences, then words) together as much as possible, as these are generally the most semantically related pieces of text.

- **How the text is split**: by list of characters.
- **How the chunk size is measured**: by number of characters.

The following code is showing how to implement it.

The `RecursiveCharacterTextSplitter` class from LangChain is used to implement it.
- You use the default separator list, which is `["\n\n", "\n", " ", ""]`.
- Chunk size is set to `100`.
- Chunk overlap is set to `20`.
- And the length function is `len`.

Here, you are using the same document "companypolicies.txt" from earlier as an example to show the performance of `RecursiveCharacterTextSplitter`.

```
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)
texts = text_splitter.create_documents([companypolicies])
texts
len(texts)
```

### Split Code


