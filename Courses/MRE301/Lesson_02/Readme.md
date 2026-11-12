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

The `CodeTextSplitter` allows you to split your code, supporting multiple programming languages. It is based on the `RecursiveCharacterTextSplitter` strategy. Simply import enum `Language` and specify the language.

```
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)
texts = text_splitter.create_documents([companypolicies])
texts
len(texts)
```

#### Python
The following demonstrates how to split Python code using the `RecursiveCharacterTextSplitter` class.

The main difference between splitting code and using the original `RecursiveCharacterTextSplitter` is that you need to call `.from_language` after the `RecursiveCharacterTextSplitter` and specify the `language`. The other parameter settings remain the same as before.

```
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
python_docs
```

#### Javascript
Let's see the separators for JSON language.

The following code is used to separate the JSON language code.

```
RecursiveCharacterTextSplitter.get_separators_for_language(Language.JS)
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
js_docs
```
For more information about applying to other languages, you can refer [here](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/code_splitter/).

### Markdown Header Text Splitter

As mentioned, chunking often aims to keep text with a common context together. With this in mind, you might want to specifically honor the structure of the document itself. For example, a Markdown file is organized by headers. Creating chunks within specific header groups is an intuitive approach.

To address this challenge, you can use `MarkdownHeaderTextSplitter`. This splitter will divide a Markdown file based on a specified set of headers.

```
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=False)
md_header_splits = markdown_splitter.split_text(md)
md_header_splits
```
From the split results, you can see that the Markdown file is divided into several chunks formatted as document objects. The `page_content` contains the text under the headings, and the `metadata` contains the header information corresponding to the `page_content`.
If you want the headers appears in the page_content as well, you can specify `strip_headers=False` when you call the `MarkdownHeaderTextSplitter`.

### Split by HTML
#### Split by HTML header
Similar in concept to the `MarkdownHeaderTextSplitter`, the HTMLHeaderTextSplitter is a "structure-aware" chunker that splits text at the element level and adds metadata for each header "relevant" to any given chunk. It can return chunks element by element or combine elements with the same metadata, with the objectives of (a) keeping related text grouped (more or less) semantically and (b) preserving context-rich information encoded in document structures. It can be used with other text splitters as part of a chunking pipeline.

Split the HTML string using `HTMLHeaderTextSplitter`.

```
from langchain_text_splitters import HTMLHeaderTextSplitter
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
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
html_header_splits = html_splitter.split_text(html_string)
html_header_splits
```
From the split results, you can see that the context under the headings is extracted and put in the `page_content` parameter. The `metatdata` contains the header information.

#### Split by HTML section
Similar to the `HTMLHeaderTextSplitter`, the `HTMLSectionSplitter` is also a "structure-aware" chunker that splits text section by section based on headings.
The following code is used to implement it.

```
from langchain_text_splitters import HTMLSectionSplitter

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

headers_to_split_on = [("h1", "Header 1"), ("h2", "Header 2"), ("h3", "Header 3")]

html_splitter = HTMLSectionSplitter(headers_to_split_on=headers_to_split_on)
html_header_splits = html_splitter.split_text(html_string)
html_header_splits
```

**Exercise 1**
- Changing separator for CharacterTextSplitter Try to change to use another separator, for example `"\n"` to see how it affect the split and chunks.
  ```
  from langchain_text_splitters import CharacterTextSplitter

# Configure the splitter using "\n" as the separator
newline_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=20,
    length_function=len,
)

# Split the document
newline_texts = newline_splitter.create_documents([companypolicies])

print(f"Total chunks generated: {len(newline_texts)}")
print("\nFirst chunk sample:")
print(newline_texts[0])
```

### Exercise 2 - Splitting Latex code Here is an example of Latex code. Try to split it.

```
latex_text = """
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

**Solution**


```
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

latex_text = """
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
    print(f"Chunk {i+1}:")
    print(doc.page_content)
    print("-" * 50)

 ```



