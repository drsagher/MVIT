# Lesson 02 Data Types and Variables
In JavaScript, data types and variables are fundamental concepts that enable developers to store, manipulate, and interact with data. Data types determine the type of value a variable can hold, such as numbers, strings, booleans, null, undefined, objects, arrays, functions, symbols, and bigInts. Variables, on the other hand, are containers that hold values of specific data types, allowing developers to access, modify, and reuse values throughout their code. JavaScript is dynamically-typed, meaning that variables can be reassigned to hold different data types, and type checking occurs at runtime rather than compile-time. Understanding data types and variables is crucial for writing effective JavaScript code, as it enables developers to declare, initialize, and manipulate variables, perform operations, and handle errors, ultimately building robust, scalable, and maintainable applications.


## Data Types
In JavaScript, data types are the building blocks of any program, determining the type of value a variable can hold and the operations that can be performed on it. JavaScript supports a range of primitive and complex data types, including Numbers, which can be integers or floating-point values; Strings, which are sequences of characters enclosed in quotes; Booleans, which represent true or false values; Null, which represents the absence of any object value; and Undefined, which represents an uninitialized or non-existent variable. Additionally, JavaScript also supports complex data types such as Objects, which are collections of key-value pairs; Arrays, which are ordered collections of values; and Functions, which are reusable blocks of code that can take arguments and return values. Furthermore, JavaScript also supports Symbol data type, which is a unique and immutable value that can be used as a property key in an object. Lastly, JavaScript also supports BigInt data type, which is a large integer with arbitrary precision, allowing developers to work with very large numbers. Understanding and working effectively with these data types is crucial for any JavaScript developer, as it enables them to write robust, efficient, and scalable code.

Here is a rundown of JavaScript's basic syntax and data types:

| Data Type | Description | Declaration | Code Example |
| --- | --- | --- | --- |
| Number | A numeric value | ```let num = 42;``` | ```console.log(num); // 42``` |
| String | A sequence of characters | ```let str = 'hello';``` | ```console.log(str); // 'hello'``` |
| Boolean | A true or false value | ```let isAdmin = true;``` | ```console.log(isAdmin); // true``` |
| Null | The absence of any object value | ```let nullValue = null;``` | ```console.log(nullValue); // null``` |
| Undefined | An uninitialized or non-existent variable | ```let undefinedValue;``` | ```console.log(undefinedValue); // undefined``` |
| Object | A collection of key-value pairs | ```let person = { name: 'John', age: 30 };``` | ```console.log(person.name); // 'John'``` |
| Array | An ordered collection of values | ```let colors = ['red', 'green', 'blue'];``` | ```console.log(colors[0]); // 'red'``` |
| Function | A block of code that can be executed | ```function greet(name) { console.log('Hello, ' + name); }``` | ```greet('Alice'); // 'Hello, Alice'``` |
| Symbol | A unique and immutable value | ```let symbol = Symbol('mySymbol');``` | ```console.log(symbol); // Symbol('mySymbol')``` |
| BigInt | A large integer value | ```let bigInt = 12345678901234567890n;``` | ```console.log(bigInt); // 12345678901234567890n``` |

Note: The n suffix is used to denote a BigInt value.
