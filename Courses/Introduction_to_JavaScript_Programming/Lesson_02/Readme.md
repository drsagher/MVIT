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


## Variables
In JavaScript, variables are used to store and manipulate data, and they come in several types. The three main types of variables in JavaScript are Var, Let, and Const. Var variables are function-scoped, meaning they are accessible throughout the function in which they are declared, and can be redeclared and updated. Let variables, introduced in ECMAScript 2015, are block-scoped, meaning they are only accessible within the block in which they are declared, and can be updated but not redeclared. Const variables are also block-scoped, but their values cannot be changed once they are declared. Additionally, JavaScript also supports other types of variables, such as Array variables, which store collections of values; Object variables, which store key-value pairs; and Function variables, which store reusable blocks of code. Understanding the different types of variables in JavaScript is essential for writing effective, efficient, and bug-free code.

### Varibales and Variable Declaration

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

### Variable Declaration Rules
1. Variable names must start with a letter, underscore (_), or dollar sign ($): Variable names cannot start with a number or any other special character.
2. Variable names can only contain letters, numbers, underscores (_), and dollar signs ($): Variable names cannot contain any other special characters.
3. Variable names are case-sensitive: JavaScript is case-sensitive, so "name" and "Name" are two different variable names.
4. Variable names cannot be reserved words: Reserved words, such as "var", "let", "const", "if", "else", etc., cannot be used as variable names.
5. Variable names should be descriptive and meaningful: Variable names should indicate the purpose or value of the variable.

## Data Memorization
In JavaScript, variables play a crucial role in data memorization, allowing developers to store and manipulate data in a program. When a variable is declared, a memory location is allocated to store the variable's value. The variable's name serves as a reference to this memory location, enabling developers to access and modify the stored value. JavaScript variables can hold various data types, including numbers, strings, booleans, objects, and arrays, each requiring a specific amount of memory to store. As variables are reassigned or go out of scope, the memory allocated to them is released, allowing for efficient memory management. Understanding how JavaScript variables interact with memory is essential for writing efficient, scalable, and bug-free code, particularly when working with large datasets or complex applications.

