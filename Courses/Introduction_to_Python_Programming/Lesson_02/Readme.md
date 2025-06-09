# Lesson 2 Start Thinking in Python

In this lesson, we'll cover the fundamentals of Python, starting with an exploration of various data types, including integers, real numbers, and strings. As you progress through the lesson, you'll discover how to use expressions in mathematical operations, store values in variables, and explore multiple techniques for manipulating strings.

## Learning Objectives:
- Demonstrate an understanding of types in Python by converting or casting data types such as strings, floats, and integers.
- Interpret variables and solve expressions by applying mathematical operations.
- Describe how to manipulate strings by using a variety of methods and operations.
- Build a program in JupyterLab to demonstrate your knowledge of types, expressions, and variables.
- Work with, manipulate, and perform operations on strings in Python.

## Agenda
1. Getting Started with Jupyter
2. Python Data Types
3. Expressions and Variables
4. String Operations

### 1. Getting Started with Jupyter

In this section, you will learn Step-by-Step Installation of Anaconda and Open Jupyter Notebook


#### Step 1: Download the Anaconda Installer

- Open your web browser (e.g., Chrome, Edge, or Firefox).
- Go to the official Anaconda download page: https://www.anaconda.com/products/distribution.
- Scroll to the Anaconda Installers section.
- Under Windows, select the 64-bit Graphical Installer (recommended for beginners) for the latest Python version (e.g., Python 3.9 or higher).
- If you have a 32-bit system (rare), choose the 32-bit installer.
- The installer file (e.g., Anaconda3-2023.09-0-Windows-x86_64.exe) will begin downloading. File size is approximately 400–600 MB, so it may take a few minutes depending on your internet speed.

#### Step 2: Install Anaconda
- Locate the downloaded installer in your Downloads folder (or wherever you saved it).
- Double-click the installer file to launch it.
- If prompted by Windows User Account Control (UAC), click Yes to allow the installer to make changes.

#### In the Anaconda installer:
- Welcome Screen: Click Next.
- License Agreement: Read the agreement, select I Agree, and click Next.
- Installation Type: Choose Just Me (recommended for most users) or All Users (requires admin privileges), then click Next.
- Destination Folder: Keep the default location (e.g., C:\Users\<YourUsername>\Anaconda3) or choose a custom folder with sufficient space, then click Next.

#### Advanced Options:
- Check Add Anaconda3 to my PATH environment variable (optional, but useful for command-line access).
- Check Register Anaconda3 as my default Python 3.x (recommended unless you have another Python installation you prefer).
- Click Next.
- Click Install to begin the installation. This may take 5–15 minutes depending on your system.
- Once installation is complete, click Next.
- (Optional) Select Install Microsoft VSCode if you want to install VSCode alongside Anaconda, then click Next.
- Click Finish to close the installer.

#### Step 3: Verify Anaconda Installation
- Open the Start Menu and search for Anaconda Prompt.
- Click Anaconda Prompt to open it.
- In the prompt, type the following command and press Enter:conda --version
-  You should see output like conda 23.7.4 (version numbers may vary). This confirms Anaconda is installed.
- Update Anaconda to the latest version by running:conda update --all --yes
- This ensures all packages, including Jupyter Notebook, are up to date.

#### Step 4: Install Jupyter Notebook (if not already included)
- Anaconda typically includes Jupyter Notebook by default, but you can verify or install it manually.
- In the Anaconda Prompt, type:conda install jupyter
- If prompted, confirm by typing y and press Enter.
- Wait for the installation to complete (this step is usually unnecessary if using a recent Anaconda installer).

#### Step 5: Open Jupyter Notebook
There are multiple ways to launch Jupyter Notebook. Below are the two most common methods for beginners:
**Method 1**: Using Anaconda Navigator (Graphical Interface)
- Open the Start Menu and search for Anaconda Navigator.
- Click Anaconda Navigator to launch it.
- It may take a moment to load, especially the first time.
- In the Anaconda Navigator window, find the Jupyter Notebook tile.
- Click the Launch button under the Jupyter Notebook tile.
- A browser window (e.g., Chrome, Edge) will open, displaying the Jupyter Notebook dashboard.
- The dashboard shows files in your home directory (e.g., C:\Users\<YourUsername>).
- To create a new notebook, click New > Python 3 in the dashboard.
- A new notebook will open where you can start coding.

**Method 2**: Using Anaconda Prompt (Command Line)
- Open the Start Menu and search for Anaconda Prompt.
- Click Anaconda Prompt to open it.
- Type the following command and press Enter:jupyter notebook
- The Jupyter Notebook server will start, and a browser window will open with the dashboard.
- The terminal will display a URL (e.g., http://localhost:8888) that you can copy into a browser if it doesn’t open automatically.
- To create a new notebook, click New > Python 3 in the dashboard.

#### Step 6: Using Jupyter Notebook
- In the Jupyter dashboard, navigate to your desired folder or create a new one to store your notebooks.
- To create a new notebook, click New > Python 3.
- To open an existing notebook (.ipynb file), navigate to its location and click it.
- Save your work frequently using File > Save and Checkpoint or the save icon.
- To stop the Jupyter server, return to the Anaconda Prompt and press Ctrl+C, then type y and press Enter to confirm.

### 2. Python Data Types
This guide provides a structured approach to understanding Python's core data types. Follow each step, practice the examples in a Jupyter Notebook, and complete the exercises to build a solid foundation.

#### Step 1: Understand What Data Types Are

**Concept:** Data types define the kind of data a variable can hold (e.g., numbers, text, collections). Python is dynamically typed, meaning you don’t explicitly declare types, but they determine what operations are allowed.
**Action:**
- Open Jupyter Notebook (via Anaconda Navigator or Anaconda Prompt with jupyter notebook).
- Create a new Python 3 notebook.
- Learn to check a variable’s type using the ```type()``` function.
- 
```
Example:x = 42
print(type(x))  # Output: <class 'int'>
```

**Exercise:**
- Create variables with different values (e.g., a number, text, True).
- Use print(type(variable)) to check their types.
- Expected types: <class 'int'>, <class 'str'>, <class 'bool'>.

#### Step 2: Explore Numeric Types (Integers and Floats)

**Concept:**
- Integers (```int```): Whole numbers (e.g., 5, -10).
- Floats (```float```): Numbers with decimal points (e.g., 3.14, -0.001).
- Python supports arithmetic operations (+, -, *, /, //, %, **) on these types.

**Action:**
- In a Jupyter cell, create variables for integers and floats.
- Perform basic operations and check their types.

```
Example:a = 10       # Integer
b = 3.14     # Float
print(type(a), type(b))  # Output: <class 'int'> <class 'float'>
print(a + b)  # Output: 13.14 (result is float)
print(a // 3)  # Output: 3 (integer division)
print(a ** 2)  # Output: 100 (exponentiation)
```

**Exercise:**
- Create two integers and perform addition, subtraction, multiplication, and division.
- Create a float and an integer, then multiply them. Check the type of the result.
- Try ```10 / 3``` and ```10 // 3```. Explain the difference in a comment.

#### Step 3: Work with Strings

**Concept:**
- Strings (```str```): Sequences of characters (e.g., "hello", 'Python').
- Strings are enclosed in single (') or double (") quotes and support operations like concatenation (+), repetition (*), and slicing).


**Action:**
- Create strings and experiment with common methods (e.g., .upper(), .lower(), .strip()).
- Use indexing and slicing to extract parts of a string.

**Example:** ```text = "Hello, Python!"```

```
print(type(text))  # Output: <class 'str'>
print(text.upper())  # Output: HELLO, PYTHON!
print(text[0:5])  # Output: Hello
print(text + " Welcome")  # Output: Hello, Python! Welcome
```

**Exercise:**
- Create a string with your name and convert it to uppercase and lowercase.
- Extract the first 3 characters of a string using slicing.
- Concatenate two strings (e.g., "Data" and "Science") and print the result.

#### Step 4: Learn Booleans

**Concept:**
- Booleans (```bool```): Represent ```True``` or ```False```.
- Used in logical operations (```and```, ```or```, ```not```) and comparisons (```==```, ```!=```, ```<```, ```>```).


**Action:**
- Create boolean variables and test logical operations.
- Use comparisons to generate booleans.

**Example:** ```is_active = True```
```
is_zero = False
print(type(is_active))  # Output: <class 'bool'>
print(5 > 3)  # Output: True
print(is_active and is_zero)  # Output: False
print(not is_zero)  # Output: True
```

**Exercise:**
- Create two boolean variables and test and, or, and not operations.
- Write comparisons (e.g., 10 < 5, "apple" == "Apple") and print their boolean results.
- Combine comparisons with logical operators (e.g., (5 > 3) and (2 < 4)).

#### Step 5: Explore Lists

Concept:
Lists (list): Ordered, mutable collections (e.g., [1, 2, 3], ["apple", "banana"]).
Support indexing, slicing, and methods like .append(), .remove(), .pop().


Action:
Create a list and modify it using common methods.
Access elements using indices and slices.


Example:fruits = ["apple", "banana", "orange"]
print(type(fruits))  # Output: <class 'list'>
fruits.append("grape")  # Add item
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']
print(fruits[1])  # Output: banana
print(fruits[0:2])  # Output: ['apple', 'banana']


Exercise:
Create a list of 5 numbers and append a new number.
Remove an item from the list using .remove() or .pop().
Extract a slice of the list (e.g., items 2 to 4).



Step 6: Understand Tuples

Concept:
Tuples (tuple): Ordered, immutable collections (e.g., (1, 2, 3)).
Similar to lists but cannot be modified after creation.


Action:
Create a tuple and access its elements.
Attempt to modify it to understand immutability.


Example:coordinates = (10, 20)
print(type(coordinates))  # Output: <class 'tuple'>
print(coordinates[0])  # Output: 10
# coordinates[0] = 5  # This will raise a TypeError


Exercise:
Create a tuple with 3 items (e.g., colors or numbers).
Access the second item using indexing.
Try modifying the tuple and observe the error.



Step 7: Learn Dictionaries

Concept:
Dictionaries (dict): Key-value pairs (e.g., {"name": "Alice", "age": 25}).
Keys are unique and immutable; values can be of any type.
Use methods like .keys(), .values(), .items().


Action:
Create a dictionary and access/modify its values.
Iterate over keys and values.


Example:person = {"name": "Alice", "age": 25}
print(type(person))  # Output: <class 'dict'>
print(person["name"])  # Output: Alice
person["city"] = "New York"  # Add key-value pair
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}


Exercise:
Create a dictionary with 3 key-value pairs (e.g., book titles and authors).
Add a new key-value pair and update an existing value.
Print all keys using .keys() and all values using .values().



Step 8: Explore Sets

Concept:
Sets (set): Unordered collections of unique items (e.g., {1, 2, 3}).
Support operations like union (|), intersection (&), and difference (-).


Action:
Create a set and perform set operations.
Add and remove items using .add() and .remove().


Example:numbers = {1, 2, 3, 3}  # Duplicate 3 is ignored
print(type(numbers))  # Output: <class 'set'>
print(numbers)  # Output: {1, 2, 3}
numbers.add(4)
print(numbers)  # Output: {1, 2, 3, 4}
set2 = {3, 4, 5}
print(numbers & set2)  # Output: {3, 4} (intersection)


Exercise:
Create two sets with some overlapping items.
Perform union, intersection, and difference operations.
Add and remove an item from one set.



Step 9: Type Conversion

Concept:
Python allows converting between types using functions like int(), float(), str(), list(), tuple(), set().
Not all conversions are valid (e.g., int("abc") raises an error).


Action:
Experiment with type conversion in a Jupyter cell.
Handle potential errors using try-except.


Example:num_str = "123"
num_int = int(num_str)
print(type(num_int))  # Output: <class 'int'>
float_num = float("3.14")
print(type(float_num))  # Output: <class 'float'>
my_list = list("hello")
print(my_list)  # Output: ['h', 'e', 'l', 'l', 'o']


Exercise:
Convert a string "42" to an integer and add 10 to it.
Convert a float 5.7 to an integer and observe the result.
Convert a string "Python" to a list of characters.



Step 10: Practice and Apply

Concept: Combine data types in a small project to reinforce learning.
Action:
Create a Jupyter Notebook project that uses multiple data types.
Example project: Store student information (name as string, grades as list, pass/fail as boolean) and perform operations (e.g., calculate average grade, display info).


Example:student = {
    "name": "Alice",
    "grades": [85, 90, 88],
    "passed": True
}
average = sum(student["grades"]) / len(student["grades"])
print(f"{student['name']} has an average grade of {average} and passed: {student['passed']}")
# Output: Alice has an average grade of 87.66666666666667 and passed: True


Exercise:
Create a dictionary for a product (e.g., name, price, categories as a set).
Calculate a discounted price (e.g., 10% off) and store it in the dictionary.
Print a summary using string formatting.



Additional Tips

Practice Regularly: Create new Jupyter notebooks for each data type and experiment with different operations.
Use Help: In Jupyter, use help(type_name) (e.g., help(str)) or dir(variable) to explore methods.
Debug Errors: If you encounter errors (e.g., TypeError), read the error message and check the types involved.
Resources:
Official Python documentation: https://docs.python.org/3/.
Run conda install -c anaconda ipython in Anaconda Prompt for enhanced interactive features in Jupyter.


Save Your Work: Save notebooks frequently (File > Save and Checkpoint) and organize them in a dedicated folder.

Troubleshooting

Type Errors: Ensure operations match the data type (e.g., don’t add a string to an integer without conversion).
Jupyter Issues: If Jupyter doesn’t launch, verify installation (conda install jupyter) or restart the kernel.
Unexpected Output: Use print(type(variable)) to debug incorrect types.
Need Help: Ask specific questions about errors or concepts for tailored guidance.

By completing these steps, you’ll have a solid understanding of Python’s core data types and how to use them. Continue practicing by building small projects, and explore advanced types (e.g., NoneType, custom classes) as you progress!
