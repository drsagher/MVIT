# Lesson 03 Document Properties
The HTML document properties provide valuable information about the current HTML document being manipulated by JavaScript. These properties allow developers to access and modify various attributes of the document, such as its title, URL, referrer, and character set. For example, 
the ```document.title``` property returns the title of the current HTML document, while the ```document.URL``` property returns the URL of the current document. Additionally, properties like ```document.referrer``` and
```document.characterSet``` provide information about the document's referrer and character set, respectively. By utilizing these document properties, developers can create more dynamic and interactive web pages that respond to user input and adapt to different environments.

## Example 01 ```document.activeElement```

### HTML
```
<!DOCTYPE html>
<html>
<head>
	<title>Document Active Element Example</title>
	<style>
		input:focus {
			background-color: lightblue;
		}
	</style>
</head>
<body>
	<form>
		<input type="text" id="input1" placeholder="Input 1">
		<input type="text" id="input2" placeholder="Input 2">
		<button id="button1">Click Me!</button>
	</form>

	<script src="script.js"></script>
</body>
</html>
```

### JavaScript ```script.js```
```
// Get the input elements
var input1 = document.getElementById("input1");
var input2 = document.getElementById("input2");
var button1 = document.getElementById("button1");

// Add event listeners to the input elements
input1.addEventListener("focus", function() {
	console.log("Input 1 focused");
	console.log("Active element:", document.activeElement);
});

input2.addEventListener("focus", function() {
	console.log("Input 2 focused");
	console.log("Active element:", document.activeElement);
});

button1.addEventListener("focus", function() {
	console.log("Button 1 focused");
	console.log("Active element:", document.activeElement);
});

// Add an event listener to the document to track changes to the active element
document.addEventListener("focus", function(event) {
	console.log("Active element changed:", event.target);
	console.log("New active element:", document.activeElement);
}, true);
```

In this example, we use document.activeElement to get the currently focused element in the document. We also add event listeners to the input elements and the button to track when they gain focus. When an element gains focus, we log the active element to the console using document.activeElement.

Note that document.activeElement returns the currently focused element, or null if no element is focused. Also, the focus event is used to track changes to the active element, and the event.target property is used to get the element that triggered the event.



