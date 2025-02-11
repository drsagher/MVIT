# Lesson 02 DOM Fundamentals
The Document Object Model (DOM) is a programming interface for HTML documents. It represents the structure of a document as a tree of nodes, where each node corresponds to an element, attribute, or piece of text. The DOM allows developers to interact with and manipulate the document's content, layout, and behavior. It provides a way to access and modify elements, attributes, and text nodes, as well as to respond to events such as clicks, keyboard input, and page loads. 

Understanding the DOM is essential for building dynamic web applications, as it allows developers to create, modify, and control the behavior of web pages. The DOM is composed of several key components, including elements, attributes, text nodes, and events, which work together to provide a powerful and flexible way to interact with web documents.

## DOM Tree Structure
The DOM tree structure is a hierarchical representation of an HTML document. It consists of a root node, which is the document object, and various child nodes, which represent the different elements, attributes, and text content of the HTML document.

The DOM tree structure is composed of the following components:
- Root Node: The document object, which is the top most node of the DOM tree.
- Element Nodes: Represent HTML elements, such as ```div```, ```p```, ```img```, etc.
- Attribute Nodes: Represent the attributes of HTML elements, such as ```id```, ```class```, ```src```, etc.
- Text Nodes: Represent the text content of HTML elements.
- Comment Nodes: Represent HTML comments.

## Node Types
The DOM defines several node types, each representing a specific type of node in the DOM tree. The following are the most common node types:

### 1. ```Node.ELEMENT_NODE```: Represents an HTML element.

```
#### HTML

<!DOCTYPE html>
<html>
<head>
	<title>Node.ELEMENT_NODE Example</title>
</head>
<body>
	<div id="myDiv">Hello World!</div>

	<script src="script.js"></script>
</body>
</html>

```

#### JavaScript ```script.js```
```
// Get the div element
var div = document.getElementById("myDiv");

// Check if the div is an element node
if (div.nodeType === Node.ELEMENT_NODE) {
	console.log("The div is an element node.");
} else {
	console.log("The div is not an element node.");
}

// Get the node name of the div
console.log("Node name:", div.nodeName);

// Get the node type of the div
console.log("Node type:", div.nodeType);

// Check if the div has child nodes
if (div.hasChildNodes()) {
	console.log("The div has child nodes.");
} else {
	console.log("The div does not have child nodes.");
}

// Get the child nodes of the div
var childNodes = div.childNodes;
console.log("Child nodes:", childNodes);
```

Output

The div is an element node.
Node name: DIV
Node type: 1
The div has child nodes.
Child nodes: [text]

In this example, we use the ```Node.ELEMENT_NODE``` constant to check if the ```div``` element is an element node. We also use other node properties and methods, such as ```nodeName```, ```nodeType```, ```hasChildNodes()```, and ```childNodes```, to get more information about the ```div``` element and its child nodes.

### 2. ```Node.TEXT_NODE```: Represents a text node.

#### HTML
```
<!DOCTYPE html>
<html>
<head>
	<title>Node.TEXT_NODE Example</title>
</head>
<body>
	<div id="myDiv">Hello <span>World!</span></div>

	<script src="script.js"></script>
</body>
</html>
```

#### JavaScript ```script.js```
```
// Get the div element
var div = document.getElementById("myDiv");

// Get the child nodes of the div
var childNodes = div.childNodes;

// Loop through the child nodes
for (var i = 0; i < childNodes.length; i++) {
	var node = childNodes[i];

	// Check if the node is a text node
	if (node.nodeType === Node.TEXT_NODE) {
		console.log("Text node:", node.nodeValue);
	} else {
		console.log("Non-text node:", node.nodeName);
	}
}
```

Output
Text node: Hello 
Non-text node: SPAN
Text node: World!

In this example, we use the Node.TEXT_NODE constant to check if a node is a text node. We then use the nodeValue property to get the text content of the text node.

Here's what's happening in the code:
1. We get the ```div``` element using ```document.getElementById```.
2. We get the child nodes of the ```div``` element using ```childNodes```.
3. We loop through the child nodes using a for loop.
4. For each node, we check if it's a text node using ```node.nodeType === Node.TEXT_NODE```.
5. If it's a text node, we log its text content using ```node.nodeValue```.
6. If it's not a text node, we log its node name using ```node.nodeName```.

Remember that the ```nodeValue``` property only returns the text content of a text node, while the ```nodeName``` property returns the name of a non-text node (e.g. "SPAN").

### 3. ```Node.COMMENT_NODE```: Represents an HTML comment.

### HTML
```
<!DOCTYPE html>
<html>
<head>
	<title>Node.COMMENT_NODE Example</title>
</head>
<body>
	<!-- This is an HTML comment -->
	<div id="myDiv">Hello World!</div>

	<script src="script.js"></script>
</body>
</html>
```

### JavaScript ```script.js```
```
// Get the HTML document
var doc = document;

// Get the child nodes of the HTML document
var childNodes = doc.childNodes;

// Loop through the child nodes
for (var i = 0; i < childNodes.length; i++) {
	var node = childNodes[i];

	// Check if the node is a comment node
	if (node.nodeType === Node.COMMENT_NODE) {
		console.log("Comment node:", node.nodeValue);
	} else {
		console.log("Non-comment node:", node.nodeName);
	}
}
```
Output:
- Comment node:  This is an HTML comment
- Non-comment node: HTML

In this example, we use the ```Node.COMMENT_NODE``` constant to check if a node is a comment node. We then use the ```nodeValue``` property to get the text content of the comment node.

Here's what's happening in the code:
1. We get the HTML document using document.
2. We get the child nodes of the HTML document using ```childNodes```.
3. We loop through the child nodes using a for loop.
4. For each node, we check if it's a comment node using ```node.nodeType === Node.COMMENT_NODE```.
5. If it's a comment node, we log its text content using ```node.nodeValue```.
6. If it's not a comment node, we log its node name using ```node.nodeName```.

Note that the ```nodeValue``` property only returns the text content of a comment node, while the ```nodeName``` property returns the name of a non-comment node (e.g. "HTML").

### 4. ```Node.DOCUMENT_NODE```: Represents the document object..

#### HTML
```
<!DOCTYPE html>
<html>
<head>
	<title>Node.DOCUMENT_NODE Example</title>
</head>
<body>
	<div id="myDiv">Hello World!</div>

	<script src="script.js"></script>
</body>
</html>
```

#### JavaScript (script.js)
```
// Get the document object
var doc = document;

// Check if the document object is a document node
if (doc.nodeType === Node.DOCUMENT_NODE) {
	console.log("The document object is a document node.");
} else {
	console.log("The document object is not a document node.");
}

// Get the document element (the root element of the document)
var docElement = doc.documentElement;

// Check if the document element is an element node
if (docElement.nodeType === Node.ELEMENT_NODE) {
	console.log("The document element is an element node.");
} else {
	console.log("The document element is not an element node.");
}

// Get the child nodes of the document object
var childNodes = doc.childNodes;

// Loop through the child nodes
for (var i = 0; i < childNodes.length; i++) {
	var node = childNodes[i];

	// Check if the node is a document type node
	if (node.nodeType === Node.DOCUMENT_TYPE_NODE) {
		console.log("Document type node:", node.name);
	} else {
		console.log("Non-document type node:", node.nodeName);
	}
}
```

Output:
- The document object is a document node.
- The document element is an element node.
- Document type node: html
- Non-document type node: HTML

In this example, we use the Node.DOCUMENT_NODE constant to check if the document object is a document node. We then use other node properties and methods to get more information about the document object and its child nodes.

Here's what's happening in the code:
1. We get the document object using document.
2. We check if the document object is a document node using ```nodeType === Node.DOCUMENT_NODE```.
3. We get the document element (the root element of the document) using ```documentElement```.
4. We check if the document element is an element node using ```nodeType === Node.ELEMENT_NODE```.
5. We get the child nodes of the document object using ```childNodes```.
6. We loop through the child nodes using a for loop.
7. For each node, we check if it's a document type node using ```nodeType === Node.DOCUMENT_TYPE_NODE```.
8. If it's a document type node, we log its name using ```name```.
9. If it's not a document type node, we log its node name using ```nodeName```.

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

## Example-01 electing elements with ```getElementById```

## HTML
```
<!DOCTYPE html>
<html>
<head>
	<title>Selecting Elements with getElementById</title>
</head>
<body>
	<h1 id="header">Selecting Elements with getElementById</h1>
	<p id="paragraph">This is a paragraph of text.</p>
	<button id="button" onclick="changeText()">Click Me!</button>

	<script src="script.js"></script>
</body>
</html>
```

### JavaScript ```script.js```
```
function changeText() {
	// Select the header element by its ID
	var header = document.getElementById("header");
	// Change the text content of the header element
	header.textContent = "New Header Text!";

	// Select the paragraph element by its ID
	var paragraph = document.getElementById("paragraph");
	// Change the text content of the paragraph element
	paragraph.textContent = "New paragraph text!";

	// Select the button element by its ID
	var button = document.getElementById("button");
	// Change the text content of the button element
	button.textContent = "Clicked!";
}
```

In this example, we have an HTML page with a header, paragraph, and button. Each of these elements has a unique ID attribute. We use the getElementById method in our JavaScript code to select these elements and change their text content when the button is clicked.

## Example-02 electing elements with ```querySelector```

### HTML
```
<!DOCTYPE html>
<html>
<head>
	<title>Selecting Elements with querySelector</title>
</head>
<body>
	<h1 class="header">Selecting Elements with querySelector</h1>
	<p class="paragraph">This is a paragraph of text.</p>
	<button class="button" onclick="changeText()">Click Me!</button>

	<div id="container">
		<p>This is a paragraph inside a container.</p>
	</div>

	<script src="script.js"></script>
</body>
</html>
```

### JavaScript ```script.js```

```
function changeText() {
	// Select the header element by its class
	var header = document.querySelector(".header");
	// Change the text content of the header element
	header.textContent = "New Header Text!";

	// Select the paragraph element by its class
	var paragraph = document.querySelector(".paragraph");
	// Change the text content of the paragraph element
	paragraph.textContent = "New paragraph text!";

	// Select the button element by its class
	var button = document.querySelector(".button");
	// Change the text content of the button element
	button.textContent = "Clicked!";

	// Select the container element by its ID
	var container = document.querySelector("#container");
	// Change the background color of the container element
	container.style.backgroundColor = "lightblue";

	// Select the paragraph element inside the container element
	var containerParagraph = document.querySelector("#container p");
	// Change the text content of the paragraph element inside the container element
	containerParagraph.textContent = "New paragraph text inside container!";
}
```
In this example, we use the querySelector method to select elements by their class, ID, and even by a combination of both (e.g., #container p). We then change the text content, background color, and other styles of the selected elements.

## Example-03 electing elements with ```querySelectorAll```

### HTML
```
<!DOCTYPE html>
<html>
<head>
	<title>Selecting Elements with querySelectorAll</title>
</head>
<body>
	<h1 class="header">Selecting Elements with querySelectorAll</h1>
	<p class="paragraph">This is a paragraph of text.</p>
	<p class="paragraph">This is another paragraph of text.</p>
	<button class="button" onclick="changeText()">Click Me!</button>

	<div id="container">
		<p class="container-paragraph">This is a paragraph inside a container.</p>
		<p class="container-paragraph">This is another paragraph inside a container.</p>
	</div>

	<script src="script.js"></script>
</body>
</html>
```

### JavaScript ```script.js```
```
function changeText() {
	// Select all paragraph elements by their class
	var paragraphs = document.querySelectorAll(".paragraph");
	// Change the text content of all paragraph elements
	paragraphs.forEach(function(paragraph) {
		paragraph.textContent = "New paragraph text!";
	});

	// Select all button elements by their class
	var buttons = document.querySelectorAll(".button");
	// Change the text content of all button elements
	buttons.forEach(function(button) {
		button.textContent = "Clicked!";
	});

	// Select all paragraph elements inside the container element
	var containerParagraphs = document.querySelectorAll("#container .container-paragraph");
	// Change the text content of all paragraph elements inside the container element
	containerParagraphs.forEach(function(paragraph) {
		paragraph.textContent = "New paragraph text inside container!";
	});

	// Select all header elements by their class
	var headers = document.querySelectorAll(".header");
	// Change the background color of all header elements
	headers.forEach(function(header) {
		header.style.backgroundColor = "lightblue";
	});
}
```

In this example, we use the querySelectorAll method to select multiple elements by their class, ID, and even by a combination of both (e.g., #container .container-paragraph). We then change the text content, background color, and other styles of the selected elements using the forEach method to iterate over the NodeList returned by querySelectorAll.


