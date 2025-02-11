# Lesson 02 DOM Fundamentals
The Document Object Model (DOM) is a programming interface for HTML and XML documents. It represents the structure of a document as a tree of nodes, where each node corresponds to an element, attribute, or piece of text. The DOM allows developers to interact with and manipulate the document's content, layout, and behavior. It provides a way to access and modify elements, attributes, and text nodes, as well as to respond to events such as clicks, keyboard input, and page loads. Understanding the DOM is essential for building dynamic web applications, as it allows developers to create, modify, and control the behavior of web pages. The DOM is composed of several key components, including elements, attributes, text nodes, and events, which work together to provide a powerful and flexible way to interact with web documents.

## DOM Tree Structure
The DOM tree structure is a hierarchical representation of an HTML document. It consists of a root node, which is the document object, and various child nodes, which represent the different elements, attributes, and text content of the HTML document.

The DOM tree structure is composed of the following components:
- Root Node: The document object, which is the topmost node of the DOM tree.
- Element Nodes: Represent HTML elements, such as div, p, img, etc.
- Attribute Nodes: Represent the attributes of HTML elements, such as id, class, src, etc.
- Text Nodes: Represent the text content of HTML elements.
- Comment Nodes: Represent HTML comments.

## Node Types
The DOM defines several node types, each representing a specific type of node in the DOM tree. The following are the most common node types:

- Node.ELEMENT_NODE (1): Represents an HTML element.
- Node.TEXT_NODE (3): Represents a text node.
- Node.COMMENT_NODE (8): Represents an HTML comment.
- Node.DOCUMENT_NODE (9): Represents the document object.

## Document Object
The document object is the root node of the DOM tree. It provides access to the entire HTML document and allows you to manipulate its content, layout, and behavior.

The document object has several properties and methods that allow you to interact with the HTML document. Some of the most commonly used properties and methods include:
- *document.documentElement*: Returns the root element of the HTML document (i.e., the html element).
- *document.body*: Returns the body element of the HTML document.
- *document.getElementById()*: Returns an element with the specified ID.
- *document.getElementsByClassName()*: Returns a collection of elements with the specified class name.
- *document.getElementsByTagName()*: Returns a collection of elements with the specified tag name.
- *document.createElement()*: Creates a new element with the specified tag name.
- *document.createTextNode()*: Creates a new text node with the specified text content.

By understanding the DOM tree structure, node types, and document object, you can effectively manipulate and interact with HTML documents using JavaScript.
