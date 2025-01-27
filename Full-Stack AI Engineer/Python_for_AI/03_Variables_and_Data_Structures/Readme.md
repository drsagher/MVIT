# 03 Variables and Data Structures
In Python, variables are used to store and manipulate data. A variable is a name given to a value, and it can be reassigned to hold different values. Python has various data structures that allow you to store and organize data in different ways. The basic data structures in Python include lists, tuples, dictionaries, and sets. Lists are ordered collections of values that can be of any data type, including strings, integers, and other lists. Tuples are similar to lists but are immutable, meaning their values cannot be changed after creation. Dictionaries are unordered collections of key-value pairs, where each key is unique and maps to a specific value. Sets are unordered collections of unique values, often used for membership testing and mathematical operations. Understanding variables and data structures is essential in Python programming, as they form the foundation of data manipulation and analysis. By mastering these concepts, you can write efficient and effective Python code to solve real-world problems.

## Variables 
When a variable is declared and assigned a value, a series of steps occur to store the data in memory. Firstly, the compiler allocates a small amount of memory to store the variable name and its associated data type. Next, a block of memory is allocated to store the assigned value, with the size of the block depending on the data type. The value is then stored in the allocated memory block, and the memory address of the block is associated with the variable name. Finally, the compiler keeps track of the memory address, allowing it to access the stored value when the variable is used in the code. For example, when assigning the value 5 to the variable x, the compiler allocates a 4-byte memory block, stores the value 5, and associates the memory address with the variable name x, allowing it to retrieve the value when needed.

### Process Understandings
- Step 1: Variable Declaration: When a variable is declared, the compiler allocates a small amount of memory to store the variable's name and its associated data type.
- Step 2: Memory Allocation: When a value is assigned to the variable, the compiler allocates a block of memory to store the value. The size of the memory block depends on the data type of the variable.
- Step 3: Value Storage: The assigned value is stored in the allocated memory block. The memory address of the block is associated with the variable name.
- Step 4: Memory Addressing: The compiler keeps track of the memory address associated with each variable. When the variable is used in the code, the compiler uses the memory address to access the stored value.
- Example: Suppose we declare a variable x and assign it the value 5:
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


In Python, a variable is a name given to a value. Variables are used to store and manipulate data in a program.
### Declaring Variables in Python

In Python, you don't need to declare variables before using them. You can assign a value to a variable using the assignment operator (=).

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

### Data Types of Variables

Python variables can hold different data types, including:

- Integers (int): whole numbers, e.g., 1, 2, 3, etc.
- Floats (float): decimal numbers, e.g., 3.14, -0.5, etc.
- Strings (str): sequences of characters, e.g., "hello", 'hello', etc. Strings can be enclosed in single quotes or double quotes.
- Boolean (bool): true or false values
- List (list): ordered collections of values, e.g., [1, 2, 3], ["a", "b", "c"], etc.
- Tuple (tuple): ordered, immutable collections of values, e.g., (1, 2, 3), ("a", "b", "c"), etc.

Example: Variables with Different Data Types

x = 5  # integer variable
y = 3.14  # float variable
name = "John"  # string variable
isAdmin = True  # boolean variable
numbers = [1, 2, 3, 4, 5]  # list variable
colors = ("red", "green", "blue")  # tuple variable

### Reassigning Variables

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
