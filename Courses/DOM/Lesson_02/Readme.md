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

## Selecting elements: getElementById, querySelector, querySelectorAll:
In JavaScript, selecting elements is a crucial step in manipulating and interacting with web pages. There are several methods to select elements, including getElementById(), querySelector(), and querySelectorAll(). The getElementById() method is used to select a single element by its unique ID, while the querySelector() method is used to select the first element that matches a specified CSS selector. The querySelectorAll() method, on the other hand, is used to select all elements that match a specified CSS selector, returning a NodeList that can be iterated over. These methods provide a powerful way to target specific elements on a web page, allowing developers to add event listeners, modify styles, and update content dynamically. By mastering these selection methods, developers can efficiently and effectively interact with web pages, creating dynamic and engaging user experiences.


| Method | Description | Code Example | Use Case |
| --- | --- | --- | --- |
| getElementById() | Returns an element with the specified ID. | ```let element = document.getElementById('myId');``` | Selecting a single element by its unique ID. |
| querySelector() | Returns the first element that matches the specified selector. | ```let element = document.querySelector('#myId');``` | Selecting a single element by its ID, class, tag name, or attribute. |
| querySelectorAll() | Returns a collection of elements that match the specified selector. | ```let elements = document.querySelectorAll('.myClass');``` | Selecting multiple elements by their class, tag name, or attribute. |

``` *getElementById() Examples* ```

- Selecting a single element by its ID:
```
let element = document.getElementById('myId');
console.log(element); // <div id="myId">Hello World!</div>
```
- Trying to select an element that doesn't exist:
```
let element = document.getElementById('nonExistentId');
console.log(element); // null
```

``` *querySelector() Examples* ```
- Selecting a single element by its ID:
```
let element = document.querySelector('#myId');
console.log(element); // <div id="myId">Hello World!</div>
```
- Selecting a single element by its class:
```
let element = document.querySelector('.myClass');
console.log(element); // <div class="myClass">Hello World!</div>
```
- Selecting a single element by its tag name:
```
let element = document.querySelector('div');
console.log(element); // <div>Hello World!</div>
```
- Trying to select an element that doesn't exist:
```
let element = document.querySelector('#nonExistentId');
console.log(element); // null
```

``` *querySelectorAll() Examples*```
- Selecting multiple elements by their class:
```
let elements = document.querySelectorAll('.myClass');
console.log(elements); // NodeList [ <div class="myClass">Hello World!</div>, <div class="myClass">Goodbye World!</div> ]
```
- Selecting multiple elements by their tag name:
```
let elements = document.querySelectorAll('div');
console.log(elements); // NodeList [ <div>Hello World!</div>, <div>Goodbye World!</div> ]
```
- Trying to select elements that don't exist:
```
let elements = document.querySelectorAll('#nonExistentId');
console.log(elements); // NodeList []
```
Note: The ```querySelectorAll()``` method returns a NodeList, which is an array-like object that can be iterated over using a for loop or the ```forEach()``` method.
