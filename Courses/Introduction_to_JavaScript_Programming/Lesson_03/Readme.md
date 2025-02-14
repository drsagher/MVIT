# Lesson 03 A Comprehensive Study of Complex Data Structures
A comprehensive study of complex data structures in JavaScript is essential for any developer looking to take their skills to the next level. Complex data structures, such as graphs, trees, and hash tables, are crucial components of efficient and scalable algorithms, enabling developers to solve complex problems and optimize their code. By mastering complex data structures in JavaScript, developers can improve their ability to analyze and solve problems, write more efficient and effective code, and build more robust and scalable applications. Additionally, a deep understanding of complex data structures can also help developers to better understand and utilize popular JavaScript libraries and frameworks, such as React, Angular, and Node.js, which rely heavily on complex data structures to manage and manipulate data.

## Introduction
In JavaScript, data types are categorized into primitives and objects. Primitives (e.g., ```number```, ```string```, ```boolean```) are immutable and not objects. Objects, however, are mutable collections of key-value pairs used to represent complex data. This lesson explores JavaScript's built-in object types, their uses, and examples.


## 1. Plain Objects (Object)
The most fundamental object type.

Creation:

```
// Object literal (preferred)
const person = { name: "Alice", age: 30 };

// Constructor
const car = new Object();
car.make = "Toyota";

```

### Key Features:

- Store properties (key-value pairs).
- Inherit properties/methods from ```Object.prototype```.
- Methods: ```Object.keys(obj)```, ```Object.values(obj)```, ```Object.assign(target, source)```.

## 2. Arrays (Array)

Ordered, integer-indexed collections.

Creation:

```
const fruits = ["apple", "banana"];
const numbers = new Array(1, 2, 3);
```

### Key Features:

- Dynamic size and type-flexible.
- Methods: ```push()```, ```pop()```, ```map()```, ```filter()```.
- Array-specific properties: ```length```.


## 3. Functions (Function)

Functions are objects with executable code.

Creation:

```
function greet() { console.log("Hello!"); }
const add = new Function("a", "b", "return a + b");
```

### Key Features:

- Can have properties and methods.
- Special methods: ```apply()```, ```bind()```, ```call()```.
- ES6 arrow functions ```(() => {})``` lack their own this.

