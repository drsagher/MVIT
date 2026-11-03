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
