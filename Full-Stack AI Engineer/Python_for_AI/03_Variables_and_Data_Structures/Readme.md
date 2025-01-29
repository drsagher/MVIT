# 03 Variables and Data Structures
In Python, variables are used to store and manipulate data. A variable is a name given to a value, and it can be reassigned to hold different values. Python has various data structures that allow you to store and organize data in different ways. The basic data structures in Python include lists, tuples, dictionaries, and sets. Lists are ordered collections of values that can be of any data type, including strings, integers, and other lists. Tuples are similar to lists but are immutable, meaning their values cannot be changed after creation. Dictionaries are unordered collections of key-value pairs, where each key is unique and maps to a specific value. Sets are unordered collections of unique values, often used for membership testing and mathematical operations. Understanding variables and data structures is essential in Python programming, as they form the foundation of data manipulation and analysis. By mastering these concepts, you can write efficient and effective Python code to solve real-world problems.

## Variables 
When a variable is declared and assigned a value, a series of steps occur to store the data in memory. Firstly, the compiler allocates a small amount of memory to store the variable name and its associated data type. Next, a block of memory is allocated to store the assigned value, with the size of the block depending on the data type. The value is then stored in the allocated memory block, and the memory address of the block is associated with the variable name. Finally, the compiler keeps track of the memory address, allowing it to access the stored value when the variable is used in the code. For example, when assigning the value 5 to the variable x, the compiler allocates a 4-byte memory block, stores the value 5, and associates the memory address with the variable name x, allowing it to retrieve the value when needed.

### Process Understandings

```
x = 5
```
Here's what happens in memory:
1. Variable Declaration: The compiler allocates a small amount of memory to store the variable name x and its associated data type int.
2. Memory Allocation: The compiler allocates a block of memory to store the value 5. Since x is an int, the memory block is 4 bytes (32 bits) in size.
3. Value Storage: The value 5 is stored in the allocated memory block. The memory address of the block is associated with the variable name x.
4. Memory Addressing: The compiler keeps track of the memory address associated with x. When x is used in the code, the compiler uses the memory address to access the stored value 5.

Here's a simplified illustration of the memory layout:

| Memory Address | Value |
| --- | --- |
| 1000 (x) | 5 |

In this example, the memory address 1000 is associated with the variable x, and the value 5 is stored at that address.

### Declaring Variables in Python
A variable is a name given to a value. Variables are used to store and manipulate data in a program. In Python, you don't need to declare variables before using them. You can assign a value to a variable using the assignment operator (=).

Example: Assigning a Value to a Variable
```
x = 5
y = "Hello"
```

### Memory size of various data structures in Python

Here is a table showing the memory size of various data structures in Python:

| Data Structure | Memory Size (bytes) |
| --- | --- |
| Integer (int) | 8 (28 bytes for small integers) |
| Float (float) | 8 |
| Complex (complex) | 16 |
| String (str) | 50-100 (depending on length) |
| Boolean (bool) | 1 |
| List (list) | 56 + 8 * len(list) |
| Tuple (tuple) | 40 + 8 * len(tuple) |
| Dictionary (dict) | 140 + 8 * len(dict) |
| Set (set) | 112 + 8 * len(set) |
| Bytes (bytes) | len(bytes) |
| Bytearray (bytearray) | len(bytearray) + 1 |

Note:

- The memory sizes listed are approximate and may vary depending on the Python implementation and the system architecture.
- The memory size of a list, tuple, dictionary, or set includes the overhead of the container itself, as well as the memory required to store each element.
- The memory size of a string includes the overhead of the string object itself, as well as the memory required to store the string data.
- The memory size of an integer can vary depending on its value. Small integers (in the range -5 to 256) are stored in a single byte, while larger integers are stored in multiple bytes.

NOTE: You can use the sys.getsizeof() function to get the exact memory size of an object in Python.

### Use the sys.getsizeof()
```
import sys

# Integer
x = 10
print(f"Memory size of integer {x}: {sys.getsizeof(x)} bytes")

# Float
y = 3.14
print(f"Memory size of float {y}: {sys.getsizeof(y)} bytes")

# String
name = "John Doe"
print(f"Memory size of string '{name}': {sys.getsizeof(name)} bytes")

# List
fruits = ["apple", "banana", "cherry"]
print(f"Memory size of list {fruits}: {sys.getsizeof(fruits)} bytes")

# Tuple
colors = ("red", "green", "blue")
print(f"Memory size of tuple {colors}: {sys.getsizeof(colors)} bytes")

# Dictionary
person = {"name": "John", "age": 30}
print(f"Memory size of dictionary {person}: {sys.getsizeof(person)} bytes")

# Set
numbers = {1, 2, 3, 4, 5}
print(f"Memory size of set {numbers}: {sys.getsizeof(numbers)} bytes")

# Bytes
byte_data = b"Hello, World!"
print(f"Memory size of bytes {byte_data}: {sys.getsizeof(byte_data)} bytes")

# Bytearray
byte_array = bytearray(b"Hello, World!")
print(f"Memory size of bytearray {byte_array}: {sys.getsizeof(byte_array)} bytes")

# Array
import array
arr = array.array('i', [1, 2, 3, 4, 5])
print(f"Memory size of array {arr}: {sys.getsizeof(arr)} bytes")

# None
none_value = None
print(f"Memory size of None: {sys.getsizeof(none_value)} bytes")

# Boolean
bool_value = True
print(f"Memory size of boolean {bool_value}: {sys.getsizeof(bool_value)} bytes")

# Complex number
complex_value = 3 + 4j
print(f"Memory size of complex number {complex_value}: {sys.getsizeof(complex_value)} bytes")
```

### Data Types of Variables

Python variables can hold different data types, including:

- Integers (int): whole numbers, e.g., 1, 2, 3, etc.
- Floats (float): decimal numbers, e.g., 3.14, -0.5, etc.
- Strings (str): sequences of characters, e.g., "hello", 'hello', etc. Strings can be enclosed in single quotes or double quotes.
- Boolean (bool): true or false values
- List (list): ordered collections of values, e.g., [1, 2, 3], ["a", "b", "c"], etc.
- Tuple (tuple): ordered, immutable collections of values, e.g., (1, 2, 3), ("a", "b", "c"), etc.

Example: Variables with Different Data Types
```
x = 5  # integer variable
y = 3.14  # float variable
name = "John"  # string variable
isAdmin = True  # boolean variable
numbers = [1, 2, 3, 4, 5]  # list variable
colors = ("red", "green", "blue")  # tuple variable
```
### Reassigning Variables
Reassigning variables is a fundamental concept in programming that allows developers to update the value of a variable after it has been declared. This technique is essential for simplifying code, improving readability, and reducing memory usage. By reassigning variables, developers can adapt to changing requirements, support dynamic typing, and write more efficient and effective code. Whether it's swapping values, simplifying calculations, or updating variables in a loop, reassigning variables is a crucial skill for any programmer to master.

In Python, you can reassign a variable to hold a different value.

Example: Reassigning a Variable
```
x = 5
x = 10
print(x)
```

## Examples of Code for each variable and data structure

Here are examples of code for each variable and data structure:

### Integer
```
x = 5
print(x)  # Output: 5
print(type(x))  # Output: <class 'int'>
```

### Float
```
x = 3.14
print(x)  # Output: 3.14
print(type(x))  # Output: <class 'float'>
```

### Complex
```
x = 3 + 4j
print(x)  # Output: (3+4j)
print(type(x))  # Output: <class 'complex'>
```

### String
```
x = "Hello, World!"
print(x)  # Output: Hello, World!
print(type(x))  # Output: <class 'str'>
```

### Boolean
```
x = True
print(x)  # Output: True
print(type(x))  # Output: <class 'bool'>
```

### List
```
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(type(fruits))  # Output: <class 'list'>
```

### Tuple
```
fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')
print(type(fruits))  # Output: <class 'tuple'>
```

### Dictionary
```
person = {"name": "John", "age": 30, "city": "New York"}
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(person))  # Output: <class 'dict'>
```

### Set
```
colors = {"red", "green", "blue"}
print(colors)  # Output: {'red', 'green', 'blue'}
print(type(colors))  # Output: <class 'set'>
```

### Bytes
```
x = b"Hello, World!"
print(x)  # Output: b'Hello, World!'
print(type(x))  # Output: <class 'bytes'>
```

### Bytearray
```
x = bytearray(b"Hello, World!")
print(x)  # Output: bytearray(b'Hello, World!')
print(type(x))  # Output: <class 'bytearray'>
```
## Bytes and Bytearray in Python

In Python, the `bytes` and `bytearray` classes are used to handle sequences of bytes. They are particularly useful for working with binary data, such as files, network protocols, or low-level data manipulation. Below is an explanation of their purpose and differences.

## 1. `bytes` Class

- **Purpose**: The `bytes` class represents an **immutable** sequence of bytes. Once created, the data cannot be changed.
- **Use Cases**:
  - Storing binary data (e.g., reading from a binary file).
  - Representing data in a format compatible with network protocols or hardware interfaces.
  - Encoding and decoding text (e.g., using UTF-8, ASCII).
- **Immutability**: Like strings, `bytes` objects are immutable. You cannot modify the contents of a `bytes` object after creation.
- **Syntax**:
  ```python
  b = b"hello"  # Creates a bytes object
  print(b)      # Output: b'hello'

  ba = bytearray(b"hello")  # Creates a bytearray object
ba[0] = 72                # Modifies the first byte
print(ba)                 # Output: bytearray(b'Hello')

### bytes example
data = b"Python"  # Immutable bytes object
print(data[0])    # Output: 80 (ASCII value of 'P')

### bytearray example
mutable_data = bytearray(data)
mutable_data[0] = 74  # Change 'P' to 'J'
print(mutable_data)   # Output: bytearray(b'Jython')

## Key Differences Between bytes and bytearray 
The bytes and bytearray classes in Python both handle sequences of bytes but differ primarily in mutability and use cases. The bytes class is immutable, meaning once created, its contents cannot be changed, making it ideal for storing fixed binary data like file contents or encoded text. On the other hand, the bytearray class is mutable, allowing modifications such as changing individual bytes, appending, or removing elements, which is useful for dynamic binary data manipulation. In terms of performance, bytes is slightly faster and more memory-efficient due to its immutability, while bytearray incurs a small overhead because of its mutable nature. Use bytes for static data and bytearray when you need to modify or build byte sequences dynamically.

## Mutable and Immutable data structures

### Mutable Data Structures

A mutable data structure is a data structure that can be modified after it is created. Mutable data structures can be changed in-place, meaning that the original data structure is altered. This can be done by adding, removing, or modifying elements within the data structure.

#### Characteristics of Mutable Data Structures

- Can be modified after creation
- Changes are made in-place
- Original data structure is altered
- Examples: Lists, Dictionaries, Sets, Bytearrays

### Immutable Data Structures

An immutable data structure is a data structure that cannot be modified after it is created. Immutable data structures cannot be changed in-place; instead, a new copy of the data structure is created when modifications are made.

#### Characteristics of Immutable Data Structures

- Cannot be modified after creation
- Changes create a new copy of the data structure
- Original data structure remains unchanged
- Examples: Tuples, Strings, Integers, Floats, Complex numbers, Frozensets

In summary, mutable data structures can be modified in-place, while immutable data structures cannot be modified and require creating a new copy when changes are made.

### Key differences:

1. Modifiability: Mutable data structures can be modified, while immutable data structures cannot.
2. Memory allocation: When a mutable data structure is modified, the changes are made in-place, without allocating new memory. Immutable data structures, on the other hand, allocate new memory for each modification.
3. Thread safety: Immutable data structures are inherently thread-safe, as multiple threads cannot modify them simultaneously. Mutable data structures require synchronization mechanisms to ensure thread safety.
4. Hashability: Immutable data structures can be hashed, making them suitable for use as dictionary keys or set elements. Mutable data structures cannot be hashed.

### When to use each:

1. Use mutable data structures:
    - When frequent modifications are necessary.
    - When working with large datasets that need to be updated efficiently.
2. Use immutable data structures:
    - When data integrity is crucial, and modifications should be explicit.
    - When working with multi-threaded environments, where thread safety is essential.
    - When using data structures as dictionary keys or set elements.

## Naming Variables
Naming variables is a crucial part of writing clean, readable, and maintainable code. Here are some general rules and best practices for naming variables:
- When naming variables, it’s essential to use descriptive and meaningful names that clearly convey the purpose or content of the variable. This makes your code easier to read, understand, and maintain. Instead of using vague or generic names like x, data, or temp, opt for names that reflect the specific role of the variable in your program. For example, instead of naming a variable n, use user_count to indicate it stores the number of users. Similarly, instead of val, use discount_rate to describe a value representing a discount percentage. Descriptive names act as self-documenting code, reducing the need for additional comments and helping others (or your future self) quickly grasp the intent of the code. Always prioritize clarity over brevity, ensuring that the variable name provides enough context to understand its purpose at a glance.
- Following naming conventions is a critical practice in programming to ensure consistency and readability across your codebase. Different programming languages often have preferred styles for naming variables, such as snake_case (e.g., user_name) in Python, camelCase (e.g., userName) in JavaScript, or PascalCase (e.g., UserName) for class names in many languages. Adhering to these conventions helps maintain a uniform structure, making it easier for developers to understand and collaborate on the code. For instance, in Python, using snake_case for variables and functions, and PascalCase for classes, aligns with the language’s style guide (PEP 8). Consistently applying these conventions not only improves code readability but also avoids confusion, especially when working in teams or on large projects. Always follow the conventions specific to the language or framework you’re using to ensure your code is clean, professional, and easy to navigate.
- Avoiding reserved keywords is a fundamental rule when naming variables to prevent conflicts and errors in your code. Reserved keywords are special words that programming languages use for specific functionalities, such as if, else, class, return, or import. Using these keywords as variable names can lead to syntax errors or unexpected behavior, as the compiler or interpreter may misinterpret your intent. For example, naming a variable class in Python will cause an error because class is reserved for defining classes. Instead, choose meaningful and alternative names that do not clash with these keywords, such as course or student_class. Always familiarize yourself with the reserved keywords of the language you’re working in and ensure your variable names are distinct and unambiguous. This practice helps maintain smooth execution and avoids unnecessary debugging challenges.
- Using consistent naming throughout your codebase is essential for maintaining clarity, readability, and professionalism. Consistency means applying the same naming style and patterns across all variables, functions, classes, and other identifiers in your code. For example, if you choose snake_case for variable names (e.g., user_name), stick to it for all variables rather than mixing it with camelCase (e.g., userName) or other styles. Similarly, if you use prefixes like is_ for boolean variables (e.g., is_active), ensure all boolean variables follow the same convention. Inconsistent naming can confuse developers, make the code harder to navigate, and introduce errors during collaboration or maintenance. By adhering to a uniform naming style, you create a cohesive and predictable structure that enhances understanding and streamlines development, whether you’re working alone or as part of a team.
- Avoiding abbreviations and acronyms in variable names is a best practice that enhances code readability and reduces ambiguity. While abbreviations might save a few keystrokes, they can make your code harder to understand, especially for others (or even yourself) who may not be familiar with the shorthand. For example, a variable named cust_id might be unclear, whereas customer_id immediately conveys its purpose. Similarly, acronyms like usr_cnt for "user count" can be confusing without proper context. Unless the abbreviation is universally understood (e.g., id for "identifier"), it’s better to use full, descriptive words that clearly express the variable’s role. This approach ensures that your code is self-explanatory, reduces the need for additional comments, and makes it easier for anyone to quickly grasp the meaning and functionality of your variables.
- Using plural names for collections is a helpful convention that makes your code more intuitive and easier to understand. When a variable stores multiple items, such as a list, array, or set, giving it a plural name clearly indicates that it holds more than one value. For example, naming a list users instead of user immediately signals that the variable contains multiple user objects. Similarly, orders, products, or employee_names are more descriptive than singular names like order, product, or employee_name when referring to collections. This practice not only improves readability but also helps avoid confusion, especially when working with variables that represent single items versus groups of items. By consistently using plural names for collections, you create a clear and logical structure in your code, making it easier to navigate and maintain.
- Prefixing boolean variables with words like is, has, or can is a widely adopted practice that makes their purpose and meaning immediately clear. Since boolean variables represent true/false or yes/no states, these prefixes help indicate that the variable is answering a question or describing a condition. For example, is_active clearly conveys whether something is active, has_permission indicates whether permission is granted, and can_edit specifies whether editing is allowed. This naming convention not only improves readability but also reduces the need for additional comments to explain the variable’s intent. Without such prefixes, boolean names like active or permission can be ambiguous and harder to interpret. By consistently using is, has, or can, you create self-documenting code that is easier to understand and maintain, both for yourself and others.
- Avoiding numbers in variable names is a good practice to ensure clarity and maintainability in your code. While it might seem convenient to use numbers to differentiate similar variables (e.g., user1, user2), this approach often leads to confusion and lacks descriptive value. Numbers in names do not provide meaningful context about the purpose or role of the variable, making the code harder to understand. For example, instead of naming variables item1, item2, and item3, use names that reflect their specific roles, such as first_item, second_item, and third_item, or better yet, use a collection like items with an index. If numbers are necessary, consider whether a list, array, or other data structure might be a better fit. By avoiding numbers in names and opting for descriptive alternatives, you create code that is more intuitive, readable, and easier to maintain.
- Using constants for fixed values is a best practice that improves code readability, maintainability, and reduces the risk of errors. Constants are variables whose values do not change during the execution of a program, such as mathematical values (e.g., π), configuration settings (e.g., maximum file size), or application-specific limits (e.g., maximum users). By convention, constants are named in uppercase letters with underscores (e.g., MAX_USERS, PI, DEFAULT_TIMEOUT), making them easily distinguishable from regular variables. This approach not only makes the purpose of the value clear but also ensures that if the value needs to be updated, it only needs to be changed in one place. For example, instead of hardcoding the value 3.14159 throughout your code, defining it as PI = 3.14159 makes the code more readable and easier to maintain. Using constants helps avoid magic numbers, enhances clarity, and promotes a more organized and professional coding style.
- Avoiding special characters in variable names is a fundamental rule to ensure your code is clean, readable, and free from syntax errors. Special characters such as @, $, %, -, or spaces are often reserved for specific purposes in programming languages and can cause errors or unexpected behavior if used in variable names. For example, in Python, using a hyphen (-) in a variable name like user-name will result in a syntax error, and in JavaScript, using @ in a name like @email is invalid. Instead, stick to alphanumeric characters and underscores (_), which are universally accepted in most programming languages. For instance, use user_name or emailAddress instead of user-name or @email. By avoiding special characters, you ensure that your code is syntactically correct, easier to read, and compatible across different programming environments. This practice also helps maintain consistency and professionalism in your codebase.
- Using context-appropriate names for variables is essential to ensure your code is meaningful and easy to understand. Variable names should reflect their role within the specific context of the code, making it clear what they represent or how they are used. For example, in a function that calculates the area of a rectangle, naming the parameters width and height is more descriptive and contextually relevant than using generic names like a and b. Similarly, in a loop that processes a list of employees, naming the iterator variable employee or emp is more appropriate than using i or item. Context-appropriate names act as self-documenting code, reducing the need for additional comments and making it easier for others (or your future self) to understand the logic and purpose of the code. By choosing names that align with the context, you create code that is intuitive, maintainable, and less prone to errors.
- Avoiding overly long variable names is important to maintain a balance between descriptiveness and readability in your code. While it’s crucial to use meaningful and descriptive names, excessively long names can make your code cumbersome and harder to read. For example, a variable name like number_of_students_enrolled_in_the_math_course is unnecessarily verbose and could be simplified to math_students_count or enrolled_students without losing clarity. Long names can also lead to cluttered code, especially when used repeatedly in expressions or function calls. Instead, aim for concise yet descriptive names that convey the purpose of the variable without being overly wordy. Striking this balance ensures your code remains clean, professional, and easy to understand, while still providing enough context to make the variable’s role clear.

## The difference between a variable and a data structure
The difference between a variable and a data structure lies in their purpose, complexity, and how they store and organize data:
### Variable
- A variable is a basic storage unit that holds a single value or reference at a time.
- It is used to store simple data types like integers, floats, strings, booleans, or references to objects.
- Variables are typically straightforward and have a limited scope, such as storing a single piece of information like age = 25 or name = "Alice".
```
age = 25  # A variable storing a single integer value
name = "Alice"  # A variable storing a single string value
```
### Data Structure
- A data structure is a specialized format for organizing, storing, and managing collections of data.
- It can hold multiple values or even other data structures, enabling efficient access, modification, and manipulation of data.
- Examples of data structures include arrays, lists, dictionaries, sets, stacks, queues, trees, and graphs.
- Data structures are designed to handle complex data relationships and operations, making them ideal for tasks like sorting, searching, or grouping data.
- They are lightweight and easy to use but are not designed to handle complex or structured data.
```
# A list (data structure) storing multiple values
students = ["Alice", "Bob", "Charlie"]

# A dictionary (data structure) storing key-value pairs
student_grades = {"Alice": 90, "Bob": 85, "Charlie": 95}
```

### Key Differences

| **Aspect**            | **Variable**                          | **Data Structure**                     |
|------------------------|---------------------------------------|----------------------------------------|
| **Purpose**            | Stores a single value or reference.   | Stores and organizes multiple values.  |
| **Complexity**         | Simple and lightweight.               | More complex and versatile.            |
| **Data Handling**      | Holds one piece of data at a time.    | Can hold collections of data.          |
| **Examples**           | `age = 25`, `name = "Alice"`          | `students = ["Alice", "Bob"]`, `student_grades = {"Alice": 90}` |
| **Use Case**           | Ideal for simple, single-value storage. | Ideal for managing grouped or related data. |

### Summary
- A variable is a basic container for a single value, while a data structure is a more advanced tool for organizing and managing collections of data.
- Variables are simple and straightforward, whereas data structures provide flexibility and efficiency for handling complex data.
- Choosing between a variable and a data structure depends on the nature of the data and the operations you need to perform. Use variables for single values and data structures for grouped or related data.

## Key Takeaways
1. Choose variable names that accurately describe the variable's purpose.
2. Be aware of the scope of your variables to avoid unexpected behavior.
3. Select the data structure that best fits your problem's requirements.
4. Indexing and slicing can be powerful tools, but use them carefully to avoid errors.
5. Understand the implications of modifying mutable data structures.
6. Adhere to the official Python style guide for coding conventions.
7. Include type hints to improve code readability and enable static type checking.
8. Thoroughly test your code to ensure it works as expected.
9. Utilize a linter to catch errors and improve code quality.
10. Use modules, packages, and functions to maintain a clean and organized codebase.
