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

## 4. Dates (Date)
Represent dates and times.

Creation:
```
const now = new Date();
const birthday = new Date("2000-01-01");
```

### Key Features:
- Methods: ```getFullYear()```, ```setMonth()```, ```toISOString()```.
- Timestamps: ```Date.now()``` returns milliseconds since epoch.

## 5. Regular Expressions (RegExp)
Pattern matching for strings.

Creation:
```
const regex1 = /ab+c/i; // Literal syntax
const regex2 = new RegExp("ab+c", "i");
```

### Key Features:
- Methods: ```test("string")```, ```exec("string")```.
- Flags: ```g``` (global), ```i``` (case-insensitive).


## 6. Error Objects (Error, TypeError, etc.)
Represent runtime errors.
Creation:

```
throw new Error("Something went wrong!");
throw new TypeError("Invalid type!");
```

### Key Features:
- Built-in subtypes: SyntaxError, ReferenceError, RangeError.
- Custom errors: Extend Error class.

## 7. Keyed Collections

### Map
Stores key-value pairs with any key type.

```
const map = new Map();
map.set("name", "Alice");
map.get("name"); // "Alice"
```

### Set
Stores unique values.
```
const set = new Set([1, 2, 2, 3]); // {1, 2, 3}
```

### WeakMap/WeakSet
Hold "weak" references (keys are objects only).

## 9. Other Built-in Objects

### Math
Static methods for math operations.

```
Math.PI; // 3.14159...
Math.random(); // Random number between 0-1
```

### JSON
Serialize/deserialize JSON data.

```
JSON.stringify({ name: "Alice" }); // '{"name":"Alice"}'
JSON.parse('{"name":"Alice"}');
```

### Promise
Manage asynchronous operations.

```
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("Done!"), 1000);
});
```

### Proxy/Reflect
Customize object behavior.

```
const target = {};
const proxy = new Proxy(target, {
  get: (obj, prop) => Reflect.get(obj, prop) || "default"
});
```

### Internationalization (Intl)
Format dates, numbers, and strings.

```
new Intl.DateTimeFormat("en-US").format(new Date());
```

## 10. Wrapper Objects
Primitives can be wrapped in objects (rarely used directly):

```
const strObj = new String("hello"); // Avoid; use primitives instead.
```
JavaScript provides a rich set of built-in object types to handle diverse programming needs. From storing data ```(Object, Array)``` to handling ```errors (Error)```, asynchronous operations (```Promise```), and binary data (```TypedArray```), understanding these objects is crucial for effective development. Always prefer literal syntax ```({}, [], /\d+/)``` over constructors for simplicity.

