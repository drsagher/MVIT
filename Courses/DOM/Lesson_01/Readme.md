# Lesson 01 JavaScript Fundamentals
This lesson is designed to review the fundamental concepts of JavaScript, providing a solid foundation for further learning and practical application.

## Objectives:
- Review the basic syntax and data types of JavaScript
- Understand variables, operators, control structures, functions, and object-oriented programming concepts
- Learn about JavaScript's built-in data structures, including arrays and objects
- Understand the concept of scope, closures, and the "this" keyword
- Review JavaScript's built-in methods and functions

## Unlocking JavaScript's Power
Unlock the full potential of JavaScript and transform your web development skills with a deep dive into its powerful features. As the backbone of modern web development, JavaScript enables you to create dynamic, interactive, and responsive web applications that engage and captivate users. By mastering JavaScript, you'll be able to manipulate the Document Object Model (DOM), handle events, and create complex animations and effects. You'll also explore advanced concepts such as asynchronous programming, closures, and object-oriented programming, allowing you to build scalable, maintainable, and efficient code. With JavaScript, the possibilities are endless, and unlocking its power will take your web development skills to the next level.

## Introduction to JavaScript
Welcome to the world of JavaScript, the versatile and powerful programming language that drives the web. As the backbone of modern web development, JavaScript enables you to create dynamic, interactive, and responsive web applications that engage and captivate users. With JavaScript, you can add functionality to your websites, create mobile and desktop applications, and even develop server-side applications. Whether you're a beginner or an experienced developer, JavaScript offers a wide range of possibilities, from simple scripting to complex enterprise-level applications. In this introduction to JavaScript, you'll learn the basics of the language, including syntax, data types, variables, and control structures, providing a solid foundation for further learning and exploration.

## History of JavaScript
JavaScript, born out of the need for dynamic web pages, has come a long way since its inception in 1995 by Brendan Eich at Netscape. Initially called 'Mocha', it was later renamed to JavaScript, and its popularity soared with the rise of the web. Over the years, JavaScript has evolved through various versions, with ECMAScript (ES) being the standardized specification. Meanwhile, JavaScript engines, such as SpiderMonkey (Firefox), V8 (Google Chrome), and JavaScriptCore (Safari), have been developed to interpret and execute JavaScript code. These engines have become increasingly sophisticated, enabling faster execution, better memory management, and improved security. As a result, modern web browsers have become capable of running complex JavaScript applications, with many browsers now supporting advanced features like Just-In-Time (JIT) compilation, caching, and concurrency. With the browser's JavaScript engine at its core, the web has transformed into a dynamic, interactive, and immersive platform, revolutionizing the way we experience and interact with online content.

## Varibales and Variable Declaration

| Variable Type | Declaration | Syntax | Code Example |
| --- | --- | --- | --- |
| Var | Function scope | ```var name = 'John';``` | ```var name = 'John'; console.log(name); // 'John'``` |
| Let | Block scope | ```let name = 'John';``` | ```let name = 'John'; console.log(name); // 'John'``` |
| Const | Block scope | ```const name = 'John';``` | ```const name = 'John'; console.log(name); // 'John'``` |
| Global Variable | Outside any function | ```name = 'John';``` | ```name = 'John'; console.log(window.name); // 'John'``` |
| Local Variable | Inside a function | ```function greet() { let name = 'John'; }``` | ```function greet() { let name = 'John'; console.log(name); } greet(); // 'John'``` |
| Parameter Variable | As a function parameter | ```function greet(name) { console.log(name); }``` | ```function greet(name) { console.log(name); } greet('John'); // 'John'``` |

Note:

- Var is function scoped, which means it can be accessed throughout the function.
- Let and Const are block scoped, which means they can only be accessed within the block they are declared in.
- Global variables are declared outside any function and can be accessed from anywhere in the code.
- Local variables are declared inside a function and can only be accessed within that function.
- Parameter variables are declared as function parameters and can only be accessed within that function.


## Basic Syntax and Data Types
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

## Operators in JavaScript
Operators are symbols used to perform operations on variables and values.

| Operator | Description | Code | Example |
| --- | --- | --- | --- |
| Arithmetic Operators |  |  |  |
| + | Addition | let sum = 2 + 3; | sum = 5 |
| - | Subtraction | let diff = 5 - 2; | diff = 3 |
| * | Multiplication | let product = 4 * 5; | product = 20 |
| / | Division | let quotient = 10 / 2; | quotient = 5 |
| % | Modulus (remainder) | let remainder = 17 % 5; | remainder = 2 |
| ++ | Increment | let count = 0; count++; | count = 1 |
| -- | Decrement | let count = 1; count--; | count = 0 |
| Comparison Operators |  |  |  |
| == | Equal to | let isEqual = 2 == 2; | isEqual = true |
| != | Not equal to | let isNotEqual = 2 != 3; | isNotEqual = true |
| === | Strictly equal to | let isStrictlyEqual = 2 === '2'; | isStrictlyEqual = false |
| !== | Strictly not equal to | let isStrictlyNotEqual = 2 !== '2'; | isStrictlyNotEqual = true |
| > | Greater than | let isGreaterThan = 3 > 2; | isGreaterThan = true |
| < | Less than | let isLessThan = 2 < 3; | isLessThan = true |
| >= | Greater than or equal to | let isGreaterThanOrEqualTo = 3 >= 3; | isGreaterThanOrEqualTo = true |
| <= | Less than or equal to | let isLessThanOrEqualTo = 2 <= 3; | isLessThanOrEqualTo = true |
| Logical Operators |  |  |  |
| && | Logical and | ```let isValid = true && true;``` | ```isValid = true``` |
| || | Logical or | ``` let isValid = true || false; ``` | ```isValid = true``` |
| ! | Logical not | ```let isNotValid = !true;``` | ```isNotValid = false``` |
| Assignment Operators |  |  |  |
| = | Assign | let name = 'John'; | name = 'John' |
| += | Add and assign | let count = 0; count += 2; | count = 2 |
| -= | Subtract and assign | let count = 2; count -= 1; | count = 1 |
| *= | Multiply and assign | let product = 2; product *= 3; | product = 6 |
| /= | Divide and assign | let quotient = 6; quotient /= 2; | quotient = 3 |
| %= | Modulus and assign | let remainder = 17; remainder %= 5; | remainder = 2 |


### 2. Control Structures and Functions
In JavaScript, control structures and functions are essential components that enable developers to write efficient, modular, and reusable code. Control structures, such as conditional statements (if/else, switch), loops (for, while, do-while), and jump statements (break, continue, return), allow developers to control the flow of their program's execution. Functions, on the other hand, are reusable blocks of code that take arguments, perform a specific task, and return a value. Functions can be defined using the function keyword or as arrow functions, and they can be invoked using the function name followed by parentheses. By combining control structures and functions, developers can write robust, maintainable, and scalable JavaScript code that can handle complex logic and tasks.

#### Conditional statements (if/else, switch)
| Conditional Statement | Description | Code Example |
| --- | --- | --- |
| If Statement | Used to execute a block of code if a condition is true | ```if (x > 5) { console.log('x is greater than 5'); }``` |
| If-Else Statement | Used to execute a block of code if a condition is true, and another block of code if the condition is false | ```if (x > 5) { console.log('x is greater than 5'); } else { console.log('x is less than or equal to 5'); }``` |
| If-Else-If Statement | Used to check multiple conditions and execute different blocks of code | ```if (x > 5) { console.log('x is greater than 5'); } else if (x == 5) { console.log('x is equal to 5'); } else { console.log('x is less than 5'); }``` |
| Switch Statement | Used to execute different blocks of code based on the value of a variable | ```switch (x) { case 1: console.log('x is 1'); break; case 2: console.log('x is 2'); break; default: console.log('x is not 1 or 2'); }``` |
| Ternary Operator | Used to execute a block of code if a condition is true, and another block of code if the condition is false | ```let result = x > 5 ? 'x is greater than 5' : 'x is less than or equal to 5';``` |

Example Use Cases
- Login System: Use an if-else statement to check if a user's credentials are correct, and if so, grant access to the system.
- Game Development: Use a switch statement to handle different game states, such as "game over", "game won", or "game paused".
- Form Validation: Use an if-else statement to check if a form field has been filled in correctly, and if not, display an error message.

Best Practices
- Keep it simple: Avoid nesting too many if-else statements, as it can make the code hard to read.
- Use meaningful variable names: Use variable names that clearly indicate what the variable represents.
- Test your code: Test your code thoroughly to ensure that it works as expected.

#### Loops (for, while, do-while, for in, for of)
Loops are a fundamental concept in JavaScript that allow developers to execute a block of code repeatedly for a specified number of iterations. JavaScript supports several types of loops, including the for loop, while loop, do-while loop, for-in loop, and for-of loop. The for loop is used to iterate over a block of code for a specified number of iterations, while the while loop continues to execute a block of code as long as a specified condition is true. The do-while loop is similar to the while loop, but it executes the block of code at least once before checking the condition. The for-in loop is used to iterate over the properties of an object, while the for-of loop is used to iterate over the values of an iterable object, such as an array or a string. By using loops, developers can write efficient and concise code that can perform repetitive tasks with ease.

| Loop Type | Description | Use Case | Code Example |
| --- | --- | --- | --- |
| For Loop | Iterates over a block of code for a specified number of iterations | Iterate over an array of numbers and print each number | ```for (let i = 0; i < 5; i++) { console.log(i); }``` |
| While Loop | Continues to execute a block of code as long as a specified condition is true | Read user input until a valid email address is entered | ```let email; while (!validateEmail(email)) { email = prompt('Enter your email address:'); }``` |
| Do-While Loop | Executes a block of code at least once before checking a specified condition | Print a message to the console until the user decides to stop | ```let response; do { console.log('Hello!'); response = prompt('Do you want to continue? (yes/no)'); } while (response.toLowerCase() === 'yes');``` |
| For-In Loop | Iterates over the properties of an object | Iterate over the properties of a person object and print each property | ```let person = { name: 'John', age: 30, occupation: 'Developer' }; for (let prop in person) { console.log(prop + ': ' + person[prop]); }``` |
| For-Of Loop | Iterates over the values of an iterable object, such as an array or a string | Iterate over the values of an array of numbers and print each number | ```let numbers = [1, 2, 3, 4, 5]; for (let num of numbers) { console.log(num); }``` |

Best Practices
- Use the correct loop type for the job: Choose the loop type that best fits the problem you're trying to solve.
- Keep your loops concise: Avoid unnecessary complexity in your loops.
- Use meaningful variable names: Use variable names that clearly indicate what the variable represents.


#### Functions ( declarations, expressions, and arrow functions)
In JavaScript, functions are reusable blocks of code that perform a specific task. They can be defined using function declarations, function expressions, or arrow functions. Function declarations use the function keyword followed by the function name and parameters, whereas function expressions define a function as a variable assignment. Arrow functions, introduced in ECMAScript 2015, provide a concise way to define small, single-purpose functions using the arrow syntax (=>). Regardless of the definition method, functions can take arguments, return values, and be invoked multiple times. Functions are essential in JavaScript programming, enabling developers to modularize code, reduce repetition, and create reusable functionality. By mastering functions, developers can write more efficient, readable, and maintainable code.

| Function Type | Description | Use | Code Example |
| --- | --- | --- | --- |
| Function Declaration | Defines a function using the function keyword | Declare a reusable block of code | ```function greet(name) { console.log('Hello, ' + name); }``` |
| Function Expression | Defines a function as a variable assignment | Create a function that can be used as an argument to another function | ```let greet = function(name) { console.log('Hello, ' + name); };``` |
| Arrow Function | Defines a function using the arrow syntax (=>) | Create a concise, single-purpose function | ```let greet = (name) => { console.log('Hello, ' + name); };``` |
| Immediately Invoked Function Expression (IIFE) | Defines a function that is executed immediately after definition | Create a self-contained block of code that runs only once | ```(function() { console.log('Hello, World!'); })();``` |
| Higher-Order Function | A function that takes another function as an argument or returns a function as a result | Create a function that can be composed with other functions | ```function twice(func) { return function() { func(); func(); }; }``` |

Best Practices
- Use meaningful function names: Choose function names that clearly indicate what the function does.
- Keep functions concise: Avoid unnecessary complexity in your functions.
- Use functions to modularize code: Break down large codebases into smaller, reusable functions.


### 3. Object-Oriented Programming
Object-Oriented Programming (OOP) is a fundamental concept in JavaScript that enables developers to write reusable, modular, and maintainable code. In JavaScript, OOP is based on prototypes, where objects can inherit properties and methods from other objects. JavaScript supports encapsulation, inheritance, and polymorphism through various mechanisms such as constructors, prototypes, and closures. Developers can define classes using the class keyword, introduced in ECMAScript 2015, or use function constructors and prototypes to create objects. JavaScript's OOP capabilities enable developers to create complex web applications, simulate real-world objects, and write efficient and scalable code. By applying OOP principles, JavaScript developers can build robust and maintainable applications that can handle complex tasks and interactions.
| Concept | Description | Explanation | Example |
| --- | --- | --- | --- |
| Class | Blueprint for creating objects | Defines properties and methods | class Person { constructor(name, age) { this.name = name; this.age = age; } sayHello() { console.log('Hello, my name is ' + this.name); } } |
| Object | Instance of a class | Has its own set of properties and methods | let person = new Person('John', 30); |
| Constructor | Special method called when an object is created | Initializes properties | constructor(name, age) { this.name = name; this.age = age; } |
| Inheritance | Creating a new class based on an existing class | Child class inherits properties and methods | class Employee extends Person { constructor(name, age, salary) { super(name, age); this.salary = salary; } } |
| Polymorphism | Objects taking on multiple forms | Method overriding or method overloading | class Rectangle { area() { return this.width * this.height; } } class Square extends Rectangle { area() { return this.side * this.side; } } |
| Encapsulation | Hiding internal implementation details | Using getters and setters | class BankAccount { constructor(balance) { this._balance = balance; } getBalance() { return this._balance; } setBalance(balance) { this._balance = balance; } } |
| Abstraction | Showing only necessary information | Hiding complex implementation details | class CoffeeMachine { constructor() { this._waterTemp = 0; } makeCoffee() { // complex implementation details } } |
| Prototype Chain | Series of objects linked together | Used for inheritance and method lookup | let person = new Person(); console.log(person.__proto__); // Person.prototype |
| This Keyword | Refers to the current object | Used to access properties and methods | class Person { constructor(name) { this.name = name; } sayHello() { console.log('Hello, my name is ' + this.name); } } |

Best Practices
- Use meaningful class and method names: Choose names that clearly indicate what the class or method does.
- Keep classes and methods concise: Avoid unnecessary complexity in your classes and methods.
- Use inheritance and polymorphism: Take advantage of these OOP principles to write reusable and flexible code.

#### Objects and properties
In JavaScript, an object is a collection of key-value pairs, where each key is a string and each value can be a string, number, boolean, array, or another object. Objects are used to store and manipulate data, and are a fundamental building block of JavaScript programming. Properties are the key-value pairs that make up an object. Each property has a name, which is a string, and a value, which can be any data type. Properties can be accessed and modified using dot notation or bracket notation. For example, given an object person with a property name, the value of name can be accessed using person.name or person['name']. Objects can also have methods, which are functions that are properties of the object. Methods can be used to perform actions on the object or its properties.

#### Constructors and prototypes
In JavaScript, constructors are special functions that are used to create new objects. When a constructor is called with the new keyword, it creates a new object and sets its internal prototype property to the constructor's prototype property. The prototype property is an object that contains properties and methods that are shared by all objects created by the constructor. This allows for inheritance and code reuse, as objects created by the same constructor can access the same properties and methods. For example, if we define a constructor Person with a prototype method sayHello, all objects created by the Person constructor will inherit the sayHello method. This is a powerful way to create objects that share common behavior and properties, and is a fundamental concept in JavaScript object-oriented programming.

#### Inheritance and polymorphism
In JavaScript, inheritance allows one object to inherit the properties and methods of another object, creating a parent-child relationship. This is achieved through the use of prototypes, where a child object's prototype is set to the parent object's prototype. Polymorphism takes this a step further, allowing objects of different classes to be treated as if they were of the same class. This is achieved through method overriding, where a child object provides a different implementation of a method that is already defined in its parent object. JavaScript also supports method overloading, where multiple methods with the same name can be defined, but with different parameter lists. By using inheritance and polymorphism, developers can create complex, hierarchical relationships between objects, and write code that is more flexible, reusable, and maintainable. For example, a Square object can inherit from a Rectangle object, and override the area method to provide a specific implementation for squares.


### 4. Data Structures
JavaScript provides several built-in data structures, including arrays, objects, sets, maps, and weak maps, which can be used to store and manipulate data efficiently. Arrays are ordered collections of values that can be accessed by index, while objects are unordered collections of key-value pairs that can be accessed by key. Sets are collections of unique values, while maps are collections of key-value pairs that can be accessed by key. Weak maps are similar to maps, but they allow the garbage collector to remove entries when the key is no longer referenced. Additionally, JavaScript also provides several data structure libraries and frameworks, such as Lodash and Immutable.js, which provide additional data structures and utilities for working with data. By using these data structures, developers can write more efficient, scalable, and maintainable code, and solve complex problems in a more elegant and efficient way.

### JavaScript Arrays Complete Reference

#### Array Creation

| Concept               | Description                          | Code Example                          | Use Case                              |
|-----------------------|--------------------------------------|---------------------------------------|---------------------------------------|
| Array Literal         | Create array using square brackets   | `let arr = [1, 2, 3];`                | Most common array creation method     |
| Array Constructor     | Create array with `new Array()`      | `let arr = new Array(1, 2, 3);`       | Less common, creates empty array if single number passed |
| Array.of()            | Creates array from arguments         | `let arr = Array.of(1, 2, 3);`        | Avoid constructor ambiguity with single numeric argument |
| Array.from()          | Creates array from array-like object | `let arr = Array.from('hello');`      | Convert NodeList, strings, or iterables to arrays |
| Split String          | Create array from split string       | `let arr = 'a,b,c'.split(',');`       | Parsing CSV data or splitting strings |

#### Array Indexing & Basic Operations

| Concept               | Description                          | Code Example                          | Use Case                              |
|-----------------------|--------------------------------------|---------------------------------------|---------------------------------------|
| Index Access          | Access elements with bracket notation | `arr[0]`                             | Accessing first element               |
| Negative Indexing      | Access from end using `length`       | `arr[arr.length - 1]`                | Get last element                      |
| Length Property        | Get/set array length                 | `arr.length = 5;`                     | Truncating or extending arrays        |
| Modification           | Change elements by index             | `arr[2] = 'new';`                     | Updating array elements               |
| Existence Check        | Check if index exists                | `2 in arr`                            | Verifying sparse arrays               |
| Iteration              | Loop through elements                | `for (let item of arr) { ... }`       | Processing each element in sequence   |
| Spread Operator        | Expand array elements                | `[...arr1, ...arr2]`                  | Merging arrays or function arguments  |

#### Array Methods

###### Mutator Methods (Modify Original Array)

| Method       | Description                          | Code Example                          | Use Case                              |
|--------------|--------------------------------------|---------------------------------------|---------------------------------------|
| push()       | Add elements to end                  | `arr.push(4);`                        | Building stacks                       |
| pop()        | Remove last element                  | `let last = arr.pop();`               | Stack implementations                 |
| shift()      | Remove first element                 | `let first = arr.shift();`            | Queue implementations                 |
| unshift()    | Add elements to beginning            | `arr.unshift(0);`                     | Adding priority items                 |
| splice()     | Add/remove elements                  | `arr.splice(2, 1, 'a', 'b');`         | Modifying array at specific position  |
| sort()       | Sort elements                        | `arr.sort((a, b) => a - b);`          | Ordering data                         |
| reverse()    | Reverse array order                  | `arr.reverse();`                      | Displaying data in reverse            |
| fill()       | Fill array with value                | `new Array(5).fill(0);`               | Initializing arrays with default values |
| copyWithin() | Copy array portion                   | `arr.copyWithin(0, 3, 5);`            | Optimized array manipulation          |

##### Accessor Methods (Return New Array)

| Method       | Description                          | Code Example                          | Use Case                              |
|--------------|--------------------------------------|---------------------------------------|---------------------------------------|
| concat()     | Merge arrays                         | `arr1.concat(arr2);`                  | Combining datasets                    |
| slice()      | Extract portion                      | `arr.slice(1, 3);`                    | Pagination or data chunks             |
| join()       | Create string from elements          | `arr.join('-');`                      | Generating CSV or URL slugs           |
| indexOf()    | Find element index                   | `arr.indexOf('apple');`               | Checking element existence            |
| lastIndexOf()| Find last occurrence index           | `arr.lastIndexOf('apple');`           | Finding recent matches                |
| includes()   | Check element existence              | `arr.includes('apple');`              | Modern existence check                |
| toString()   | Convert to string                    | `arr.toString();`                     | Simple array representation           |

##### Iteration Methods

| Method       | Description                          | Code Example                          | Use Case                              |
|--------------|--------------------------------------|---------------------------------------|---------------------------------------|
| forEach()    | Execute function for each element    | `arr.forEach(item => console.log(item));` | Side effect operations          |
| map()        | Create new transformed array         | `arr.map(x => x * 2);`                | Data transformation pipelines         |
| filter()     | Create filtered array                | `arr.filter(x => x > 10);`            | Search results filtering              |
| reduce()     | Accumulate values                    | `arr.reduce((sum, x) => sum + x, 0);` | Aggregations and calculations         |
| reduceRight()| Reduce from right-to-left            | `arr.reduceRight((acc, x) => ...);`   | Right-associative operations          |
| find()       | Find first matching element          | `arr.find(x => x.age > 18);`          | Database-like queries                 |
| findIndex()  | Find index of first match            | `arr.findIndex(x => x > 10);`         | Locating element positions            |
| some()       | Test if any element matches          | `arr.some(x => x < 0);`               | Validation checks                     |
| every()      | Test if all elements match           | `arr.every(x => x.valid);`            | Complete data validation              |
| entries()    | Get index/value pairs                | `for (let [i, v] of arr.entries())`   | Need both index and value             |
| keys()       | Get array indices                    | `for (let i of arr.keys())`           | Index-only iteration                  |
| values()     | Get array values                     | `for (let v of arr.values())`         | Value-only iteration                  |

##### Other Important Methods/Properties

| Method/Property | Description                          | Code Example                          | Use Case                              |
|-----------------|--------------------------------------|---------------------------------------|---------------------------------------|
| flat()          | Flatten nested arrays                | `arr.flat(2);`                        | Processing nested data structures     |
| flatMap()       | Map then flatten                     | `arr.flatMap(x => [x, x*2]);`         | Combined mapping/flattening           |
| Array.isArray() | Check if value is array              | `Array.isArray(arr);`                 | Type checking                         |
| at()            | Access elements with negative index  | `arr.at(-1);`                         | Modern last element access            |
| toLocaleString()| Localized string representation      | `arr.toLocaleString();`               | Internationalization                  |

#### Advanced Concepts

| Concept               | Description                          | Code Example                          | Use Case                              |
|-----------------------|--------------------------------------|---------------------------------------|---------------------------------------|
| Sparse Arrays         | Arrays with empty slots              | `let arr = [1,,3];`                   | Memory optimization                   |
| Array-like Objects    | Objects with numeric keys and length | `Array.from(arguments);`              | Working with DOM collections          |
| Typed Arrays          | Fixed-type numeric arrays            | `new Int32Array(10);`                 | Binary data processing                 |
| Destructuring         | Extract values into variables        | `let [first, second] = arr;`          | Clean value extraction                 |
| Array Buffer          | Raw binary data buffer               | `new ArrayBuffer(16);`                | Low-level binary operations            |


#### Objects (creation, properties, methods)
Object Concepts
| Concept | Description | Code Example | Use Case |
| --- | --- | --- | --- |
| Object Creation | Create a new object using the Object constructor or the literal syntax {}. | ```let obj = new Object(); or let obj = {};``` | Create an object to store a collection of key-value pairs. |
| Indexing | Access object properties using their key. | ```let obj = { name: 'John', age: 30 }; console.log(obj['name']); // 'John'``` | Access a specific property in an object. |
| Dot Notation | Access object properties using dot notation. | ```let obj = { name: 'John', age: 30 }; console.log(obj.name); // 'John'``` | Access a specific property in an object. |
| Bracket Notation | Access object properties using bracket notation. | ```let obj = { name: 'John', age: 30 }; console.log(obj['name']); // 'John'``` | Access a specific property in an object. |

Object Methods
| Method | Description | Code Example | Use Case |
| --- | --- | --- | --- |
| Object.keys() | Return an array of a given object's own enumerable property names. | let obj = { name: 'John', age: 30 }; console.log(Object.keys(obj)); // ['name', 'age'] | Get an array of an object's property names. |
| Object.values() | Return an array of a given object's own enumerable property values. | let obj = { name: 'John', age: 30 }; console.log(Object.values(obj)); // ['John', 30] | Get an array of an object's property values. |
| Object.entries() | Return an array of a given object's own enumerable string-keyed property [key, value] pairs. | let obj = { name: 'John', age: 30 }; console.log(Object.entries(obj)); // [['name', 'John'], ['age', 30]] | Get an array of an object's property key-value pairs. |
| Object.assign() | Copy the values of all enumerable own properties from one or more source objects to a target object. | let obj1 = { name: 'John' }; let obj2 = { age: 30 }; Object.assign(obj1, obj2); console.log(obj1); // { name: 'John', age: 30 } | Merge two or more objects into a single object. |
| Object.create() | Create a new object, using an existing object as the prototype of the newly created object. | let obj = { name: 'John' }; let newObj = Object.create(obj); console.log(newObj.name); // 'John' | Create a new object that inherits from an existing object. |
| Object.freeze() | Freeze an object: that is, prevent new properties from being added to it; prevent existing properties from being removed; and prevent existing properties, or their enumerability, configurability, or writability, from being changed. | let obj = { name: 'John' }; Object.freeze(obj); obj.name = 'Jane'; console.log(obj.name); // 'John' | Prevent an object from being modified. |
| Object.seal() | Seal an object, preventing new properties from being added and marking all existing properties as non-configurable. | let obj = { name: 'John' }; Object.seal(obj); obj.name = 'Jane'; console.log(obj.name); // 'Jane' | Prevent new properties from being added to an object. |
| Object.isFrozen() | Determine if an object is frozen. | let obj = { name: 'John' }; Object.freeze(obj); console.log(Object.isFrozen(obj)); // true | Check if an object is frozen. |
| Object.isSealed() | Determine if an object is sealed. | let obj = { name: 'John' }; Object.seal(obj); console.log(Object.isSealed(obj)); // true | Check if an object is sealed. |

Object Iteration
| Method | Description | Code Example | Use Case |
| --- | --- | --- | --- |
| for...in | Iterate over the enumerable properties of an object. | let obj = { name: 'John', age: 30 }; for (let key in obj) { console.log(key + ': ' + obj[key]); } | Iterate over an object's properties. |
| for...of | Iterate over the values of an object's properties. | let obj = { name: 'John', age: 30 }; for (let value of Object.values(obj)) { console.log(value); } | Iterate over an object's property


### 5. Scope, Closures, and the "this" Keyword

In JavaScript, scope refers to the region of the code where a variable is defined and accessible. Variables defined within a function have local scope and are only accessible within that function. Closures, on the other hand, occur when a function has access to its own scope as well as the scope of its outer functions, even when the outer functions have returned. This allows the inner function to "remember" the variables and functions of its outer scope. The "this" keyword is used to refer to the current execution context of a function, which can vary depending on how the function is called. In global scope, "this" refers to the global object (usually the window object in browsers). Within a function, "this" refers to the object that the function is a method of, unless the function is called with a different context using the call() or apply() methods. Understanding scope, closures, and the "this" keyword is crucial for writing effective and efficient JavaScript code.


#### Variable scope and hoisting
In JavaScript, variable scope refers to the region of the code where a variable is defined and accessible. Variables can have either global or local scope, depending on where they are declared. Global variables are declared outside of functions and are accessible from anywhere in the code, while local variables are declared within functions and are only accessible within that function. Hoisting is a phenomenon in JavaScript where variables and functions are moved to the top of their scope, regardless of where they are actually declared. This means that variables and functions can be used before they are declared, as long as they are declared somewhere in the code. However, it's worth noting that only the declaration is hoisted, not the assignment. This can lead to unexpected behavior if not understood properly. Understanding variable scope and hoisting is essential for writing predictable and maintainable JavaScript code.


#### Closures and the module pattern

In JavaScript, closures are functions that have access to their own scope as well as the scope of their outer functions, even when the outer functions have returned. This allows closures to "remember" the variables and functions of their outer scope, making them useful for creating private variables and functions. The module pattern is a design pattern that takes advantage of closures to create self-contained modules of code that can be easily reused and composed together. In the module pattern, a function is used to create a new scope, and the variables and functions defined within that scope are only accessible through the public API exposed by the function. This allows developers to encapsulate their code and hide implementation details, making it easier to write modular, maintainable, and scalable code. By using closures and the module pattern, developers can create robust and flexible code that is easy to understand and reuse.

| Concept | Description | Example | Context |
| --- | --- | --- | --- |
| Global Scope | Variables defined outside of functions | ```let x = 10;``` | Global object (window) |
| Local Scope | Variables defined within functions | ```function foo() { let x = 10; }``` | Function scope |
| Closure | Function that has access to its own scope and outer scope | ```function outer() { let x = 10; function inner() { console.log(x); } return inner; }``` | Outer scope |
| this (Global) | Refers to the global object (window) | ```console.log(this);``` // window | Global object (window) |
| this (Function) | Refers to the object that the function is a method of | ```let obj = { name: 'John', sayHello: function() { console.log(this.name); } }; obj.sayHello(); // John | Object that the function is a method of ```|
| this (Constructor) | Refers to the newly created object | ```function Person(name) { this.name = name; } let john = new Person('John'); console.log(john.name); // John ```| Newly created object |
| this (Arrow Function) | Bound to the context of the surrounding scope | ```let obj = { name: 'John' }; let sayHello = () => console.log(this.name); sayHello(); // undefined | Surrounding scope |
| Call() and Apply()``` | Change the context of the "this" keyword | ```let obj = { name: 'John' }; function sayHello() { console.log(this.name); } sayHello.call(obj); // John``` | Specified object |
| Bind() | Bind the "this" keyword to a specific object | ```let obj = { name: 'John' }; function sayHello() { console.log(this.name); } let boundSayHello = sayHello.bind(obj); boundSayHello(); // John``` | Specified object |


### 6. Built-in Methods and Functions
JavaScript provides a wide range of built-in methods and functions that can be used to perform various tasks, such as manipulating strings, numbers, and dates, as well as working with arrays and objects. For example, the String object has methods like toUpperCase(), toLowerCase(), and trim() that can be used to manipulate strings. The Array object has methods like push(), pop(), and splice() that can be used to add, remove, and manipulate array elements. The Math object has functions like sin(), cos(), and sqrt() that can be used to perform mathematical calculations. Additionally, JavaScript also provides built-in functions like setTimeout(), setInterval(), and parseInt() that can be used to perform tasks like delaying code execution, repeating code execution, and converting strings to numbers. These built-in methods and functions can be used to simplify code and make it more efficient, and are an essential part of JavaScript programming.

#### String methods (concat, substring, etc.)
String Methods in JavaScript
| Method | Description | Code Example | Concept |
| --- | --- | --- | --- |
| charAt() | Returns the character at the specified index. | let str = "Hello"; console.log(str.charAt(0)); // "H" | Indexing |
| charCodeAt() | Returns the Unicode value of the character at the specified index. | let str = "Hello"; console.log(str.charCodeAt(0)); // 72 | Unicode values |
| codePointAt() | Returns the Unicode code point of the character at the specified index. | let str = "Hello"; console.log(str.codePointAt(0)); // 72 | Unicode code points |
| concat() | Concatenates two or more strings. | let str1 = "Hello"; let str2 = "World"; console.log(str1.concat(str2)); // "HelloWorld" | String concatenation |
| endsWith() | Returns true if the string ends with the specified value. | let str = "Hello World"; console.log(str.endsWith("World")); // true | String matching |
| fromCharCode() | Returns a string created from the specified sequence of Unicode values. | console.log(String.fromCharCode(72, 101, 108, 108, 111)); // "Hello" | Unicode values |
| includes() | Returns true if the string contains the specified value. | let str = "Hello World"; console.log(str.includes("World")); // true | String matching |
| indexOf() | Returns the index of the first occurrence of the specified value. | let str = "Hello World"; console.log(str.indexOf("World")); // 6 | Indexing |
| lastIndexOf() | Returns the index of the last occurrence of the specified value. | let str = "Hello World"; console.log(str.lastIndexOf("World")); // 6 | Indexing |
| localeCompare() | Compares two strings in the current locale. | let str1 = "Hello"; let str2 = "hello"; console.log(str1.localeCompare(str2)); // 1 | String comparison |
| match() | Returns an array containing the matches of the specified regular expression. | let str = "Hello World"; console.log(str.match(/World/)); // ["World"] | Regular expressions |
| normalize() | Returns the Unicode Normalization Form of the string. | let str = "café"; console.log(str.normalize("NFC")); // "café" | Unicode normalization |
| padEnd() | Pads the string with the specified value to the end. | let str = "Hello"; console.log(str.padEnd(10, " World")); // "Hello World" | String padding |
| padStart() | Pads the string with the specified value to the start. | let str = "Hello"; console.log(str.padStart(10, " World")); // " WorldHello" | String padding |
| repeat() | Returns a string repeated the specified number of times. | let str = "Hello"; console.log(str.repeat(3)); // "HelloHelloHello" | String repetition |
| replace() | Replaces the specified value with the specified replacement. | let str = "Hello World"; console.log(str.replace("World", "Universe")); // "Hello Universe" | String replacement |
| search() | Returns the index of the first occurrence of the specified regular expression. | let str = "Hello World"; console.log(str.search(/World/)); // 6 | Regular expressions |
| slice() | Returns a subset of the string. | let str = "Hello World"; console.log(str.slice(6, 11)); // "World" | String slicing |
| split() | Splits the string into an array of substrings. | let str = "Hello World"; console.log(str.split(" ")); // ["Hello", "World"] | String splitting |
| startsWith() | Returns true if the string starts with the specified value. | let str = "Hello World"; console.log(str.startsWith("Hello")); // true | String matching |
| substring() | Returns a subset of the string. | let str = "Hello World"; console.log(str.substring(6, 11)); // "World" | String slicing |
| toLocaleLowerCase() | Returns the string in lowercase, according to the current locale. | let str = "Hello"; console.log(str.toLocaleLowerCase()); // "hello" | String case conversion |
| toLocaleUpperCase() | Returns the string in uppercase, according to the current locale. | let str = "hello"; console.log(str.toLocaleUpperCase()); // "HELLO" | String case conversion |
| toLowerCase() | Returns the string in lowercase


#### Array methods (push, pop, etc.)

| Method | Description | Code Example | Concept |
| --- | --- | --- | --- |
| concat() | Merges two or more arrays into a new array. | let arr1 = [1, 2, 3]; let arr2 = [4, 5, 6]; console.log(arr1.concat(arr2)); // [1, 2, 3, 4, 5, 6] | Array merging |
| copyWithin() | Copies a sequence of array elements within the array. | let arr = [1, 2, 3, 4, 5]; arr.copyWithin(0, 2); console.log(arr); // [3, 4, 5, 4, 5] | Array copying |
| entries() | Returns an iterator object that contains the key-value pairs of the array. | let arr = [1, 2, 3]; for (let [key, value] of arr.entries()) { console.log(key + ': ' + value); } | Array iteration |
| every() | Returns true if all elements in the array pass the test implemented by the provided function. | let arr = [1, 2, 3, 4, 5]; console.log(arr.every(x => x > 0)); // true | Array testing |
| fill() | Fills all the elements of an array from a start index to an end index with a static value. | let arr = [1, 2, 3, 4, 5]; arr.fill(0, 2, 4); console.log(arr); // [1, 2, 0, 0, 5] | Array filling |
| filter() | Creates a new array with all elements that pass the test implemented by the provided function. | let arr = [1, 2, 3, 4, 5]; console.log(arr.filter(x => x > 3)); // [4, 5] | Array filtering |
| find() | Returns the first element in the array that satisfies the provided testing function. | let arr = [1, 2, 3, 4, 5]; console.log(arr.find(x => x > 3)); // 4 | Array searching |
| findIndex() | Returns the index of the first element in the array that satisfies the provided testing function. | let arr = [1, 2, 3, 4, 5]; console.log(arr.findIndex(x => x > 3)); // 3 | Array searching |
| forEach() | Calls a function once for each element in an array. | let arr = [1, 2, 3, 4, 5]; arr.forEach(x => console.log(x)); | Array iteration |
| includes() | Determines whether an array includes a certain value among its entries. | let arr = [1, 2, 3, 4, 5]; console.log(arr.includes(3)); // true | Array searching |
| indexOf() | Returns the first index at which a given element can be found in the array, or -1 if it is not present. | let arr = [1, 2, 3, 4, 5]; console.log(arr.indexOf(3)); // 2 | Array searching |
| join() | Joins all elements of an array into a string. | let arr = [1, 2, 3, 4, 5]; console.log(arr.join(', ')); // "1, 2, 3, 4, 5" | Array joining |
| keys() | Returns a new Array Iterator object that contains the keys for each index in the array. | let arr = [1, 2, 3, 4, 5]; for (let key of arr.keys()) { console.log(key); } | Array iteration |
| lastIndexOf() | Returns the last index at which a given element can be found in the array, or -1 if it is not present. | let arr = [1, 2, 3, 4, 5]; console.log(arr.lastIndexOf(3)); // 2 | Array searching |
| map() | Creates a new array with the results of applying the provided function on every element in this array. | let arr = [1, 2, 3, 4, 5]; console.log(arr.map(x => x * 2)); // [2, 4, 6, 8, 10] | Array transformation |
| pop() | Removes the last element from an array and returns that element

#### Math functions (abs, pow, etc.)

#### Date and time functions


## Target Audience:
- Beginners who want to review JavaScript fundamentals
- Developers who need a refresher on JavaScript basics
- Anyone looking to improve their understanding of JavaScript concepts
