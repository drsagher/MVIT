# Lesson 3 Building Blocks of Code
The building blocks of code refer to the fundamental elements that form the foundation of programming. These essential components include conditions and branching, which enable decision-making in code; loops, which facilitate repetitive tasks; functions, which promote code reusability and modularity; exception handling, which ensures robust error management; and objects and classes, which introduce object-oriented programming principles. Mastering these building blocks allows developers to craft efficient, scalable, and maintainable software solutions. By understanding how to effectively utilize these elements, programmers can tackle complex problems, create innovative applications, and bring their ideas to life. Whether you're a beginner or an experienced developer, grasping the building blocks of code is crucial for success in the world of programming.

## Learning Objectives
- Classify conditions and branching by identifying structured scenarios with outputs.
- Work with objects and classes.
- Explain objects and classes by identifying data types and creating a class.
- Use exception handling in Python.
- Explain what functions do.
- Build a function using inputs and outputs.
- Explain how for loops and while loops work.
- Work with condition statements in Python, including operators and branching.
- Create and use loop statements in Python.


## Agenda
This lesson discusses Python fundamentals and begins with the concepts of conditions and branching. Continue through the lesson and learn how to implement loops to iterate over sequences, create functions to perform a specific task, perform exception handling to catch errors, and how classes are needed to create objects:

1. Conditions and Branching
2. Loops
3. Functions
4. Exception Handling
5. Objects and Classes


### 1. Conditions and Branching
Conditions and branching are essential for decision-making in Python programs. They allow you to execute specific blocks of code based on whether certain conditions are met, using statements like if, elif, and else. This guide provides a comprehensive overview with examples, formatted for clarity and suitable for a GitHub README.md.

#### 1. Introduction to Conditional Statements
Conditional statements evaluate expressions that result in a boolean value (True or False) and control the program’s flow by executing different code blocks based on those evaluations. The primary components are:

- ```if```: Executes a block of code if a condition is True.
- ```elif```: Checks additional conditions if previous ones are False.
- ```else```: Executes a block of code if all preceding conditions are False.

**Syntax**

```
if condition:
    # Code block executed if condition is True
elif another_condition:
    # Code block executed if another_condition is True
else:
    # Code block executed if all conditions are False

````
**Note:** Python uses indentation (typically 4 spaces) to define code block scope.

#### 2. Comparison Operators
Comparison operators are used to compare values in Python, returning a boolean result (`True` or `False`). They are commonly used in conditional statements to control program flow.

| Operator | Description                  | Example          |
|----------|------------------------------|------------------|
| `==`     | Equal to                     | `x == y`         |
| `!=`     | Not equal to                 | `x != y`         |
| `>`      | Greater than                 | `x > y`          |
| `<`      | Less than                    | `x < y`          |
| `>=`     | Greater than or equal to     | `x >= y`         |
| `<=`     | Less than or equal to        | `x <= y`         |


#### 3. Logical Operators
Logical operators are used to combine multiple conditions in Python, producing a boolean result (`True` or `False`). They are essential for building complex conditional statements.

| Operator | Description                          | Example                 |
|----------|--------------------------------------|-------------------------|
| `and`    | True if both conditions are True     | `x > 0 and y > 0`      |
| `or`     | True if at least one condition is True | `x > 0 or y > 0`      |
| `not`    | Inverts the boolean value            | `not (x > 0)`          |


#### 4. The if Statement
The if statement evaluates a condition and executes its code block if the condition is True.

**Example: Checking Voting Eligibility**

```
age = 20
if age >= 18:
    print("You are eligible to vote.")
```

**Output:**
You are eligible to vote.

#### 5. The else Statement
The else statement provides a fallback block that runs when the if condition is False.

**Example: Pass or Fail**
```
score = 65
if score >= 60:
    print("You passed the exam!")
else:
    print("You failed the exam.")
```
**Output:**
You passed the exam!

#### 6. The elif Statement
The elif (else if) statement allows checking multiple conditions sequentially.

**Example: Grading System**

```
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**Output:**
Grade: B

#### 7. Nested Conditional Statements
You can nest if statements within other if statements for complex decision-making.

**Example: Movie Theater Discounts**

```
age = 65
is_student = False

if age >= 60:
    if is_student:
        print("You get a senior student discount!")
    else:
        print("You get a senior discount!")
else:
    if is_student:
        print("You get a student discount!")
    else:
        print("No discount available.")
```

**Output:**
You get a senior discount!

#### 8. Ternary Operator
The ternary operator provides a concise way to write simple if-else statements.

**Syntax**
value_if_true if condition else value_if_false

**Example: Assigning a Status**

```
age = 16
status = "Minor" if age < 18 else "Adult"
print(status)
```

**Output:**
Minor

#### 9. Membership Operators
Membership operators are used to check if a value exists within a sequence (e.g., list, string, tuple) in Python, returning a boolean result (`True` or `False`). They are commonly used in conditional statements.

| Operator   | Description                          | Example                 |
|------------|--------------------------------------|-------------------------|
| `in`       | True if value is in sequence         | `x in list`             |
| `not in`   | True if value is not in sequence     | `x not in list`         |


**Example: Checking Allowed Items**

```
allowed_items = ["pen", "pencil", "notebook"]
item = "pen"

if item in allowed_items:
    print(f"{item} is allowed in the exam.")
else:
    print(f"{item} is not allowed.")
```

**Output:**
pen is allowed in the exam.

#### 10. Practical Example: ATM Simulator
This example simulates an ATM system, demonstrating conditions and branching with user input.

```
balance = 1000
pin = 1234
user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    print("1. Check Balance")
    print("2. Withdraw Money")
    choice = int(input("Select an option (1 or 2): "))
    
    if choice == 1:
        print(f"Your balance is ${balance}")
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: ${balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid option.")
else:
    print("Incorrect PIN.")
```

**Sample Run (Input: PIN = 1234, choice = 1):**

Enter your PIN: 1234
1. Check Balance
2. Withdraw Money
Select an option (1 or 2): 1
Your balance is $1000

#### 11. Common Pitfalls and Best Practices
- **Indentation Errors:** Use consistent indentation (4 spaces recommended) to avoid IndentationError.
- **Overusing elif:** For many mutually exclusive conditions, consider dictionaries or the match statement for cleaner code.
- **Redundant Conditions:** Simplify conditions, e.g., use if x instead of if x == True.
- **Readable Conditions:** Write clear and logical conditions to improve maintainability.

**Example: Simplified Conditions**

```
# Less readable
is_active = True
if is_active == True:
    print("System is active.")

# More readable
if is_active:
    print("System is active.")
```

#### 12. Advanced Example: Traffic Light Controller
This example simulates a traffic light system using conditions to determine actions.

```
light = input("Enter traffic light color (red, yellow, green): ").lower()

if light == "green":
    print("Go!")
elif light == "yellow":
    print("Slow down!")
elif light == "red":
    print("Stop!")
else:
    print("Invalid color. Please enter red, yellow, or green.")
```

**Sample Run (Input: green):**
Enter traffic light color (red, yellow, green): green
Go!

#### 13. The match Statement (Python 3.10+)
The match statement, introduced in Python 3.10, provides a cleaner alternative to multiple elif statements for pattern matching.

**Example: HTTP Status Code Handler**

```
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")
```

**Output:**
Not Found


### 2. Loops
Loops in Python allow you to execute a block of code repeatedly based on a condition or over a sequence of items. They are essential for automating repetitive tasks and processing collections of data. This guide provides a step-by-step learning process for all types of loops in Python, including `for`, `while`, nested loops, and loop control statements, with practical examples and best practices.

#### 1. Introduction to Loops

Loops allow you to repeat a block of code multiple times, either for a fixed number of iterations or until a condition is met. Python supports two primary loop types:

- **`for` Loop**: Iterates over a sequence (e.g., list, tuple, string, or range).
- **`while` Loop**: Repeats as long as a condition is `True`.

Additionally, Python provides loop control statements (`break`, `continue`, `pass`) to modify loop behavior and supports nested loops for complex iterations.

> **Note**: Python uses indentation (typically 4 spaces) to define the scope of loop code blocks.

#### 2. The `for` Loop

The `for` loop is used to iterate over a sequence (e.g., list, tuple, string, or `range()` object). It’s ideal for tasks where the number of iterations is known or based on a sequence.

**Syntax**

```python
for variable in sequence:
    # Code block to execute
```

**Step 1:** Iterating Over Sequences
You can loop over elements in a list, tuple, string, or other iterable objects.

**Example:** Iterating Over a List

```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")
```

**Output**:

```
I like apple
I like banana
I like orange
```

**Example:** Iterating Over a String

```
word = "Python"
for letter in word:
    print(letter)
```

**Output**:
```
P
y
t
h
o
n
```

**Step 2:** Using `range()`
The `range()` function generates a sequence of numbers, often used with `for` loops.

#### Syntax
```python
range(start, stop, step)
```
- `start`: Starting number (inclusive, optional, default is 0).
- `stop`: Ending number (exclusive).
- `step`: Increment (optional, default is 1).

#### Example: Using `range()`
```python
for i in range(1, 5):  # Iterates from 1 to 4
    print(f"Number: {i}")
```
**Output**:
```
Number: 1
Number: 2
Number: 3
Number: 4
```

**Example: Using `range()` with Step**
```python
for i in range(0, 10, 2):  # Even numbers from 0 to 8
    print(f"Even: {i}")
```
**Output**:
```
Even: 0
Even: 2
Even: 4
Even: 6
Even: 8
```

#### 3. The `while` Loop

The `while` loop continues executing a block of code as long as a condition is `True`. It’s useful when the number of iterations is unknown.

**Syntax**
```python
while condition:
    # Code block to execute
```

**Step 3:** Condition-Based Looping
Use a `while` loop when you need to repeat an action until a specific condition changes.

**Example: Counting Down**
```python
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
```
**Output**:
```
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
```

**Example: User Input Validation**

```
password = ""
while password != "secret":
    password = input("Enter the password: ")
    if password == "secret":
        print("Access granted!")
    else:
        print("Access denied. Try again.")
```
**Sample Run** (Input: `wrong`, `secret`):
```
Enter the password: wrong
Access denied. Try again.
Enter the password: secret
Access granted!
```

#### 4. Loop Control Statements

Python provides three control statements to modify loop behavior:

| Statement | Description                                      |
|-----------|--------------------------------------------------|
| `break`   | Exits the loop immediately                      |
| `continue`| Skips the rest of the current iteration         |
| `pass`    | Does nothing, used as a placeholder             |

**Step 4: Using `break`**
The `break` statement terminates the loop prematurely when a condition is met.

**Example: Stop at a Specific Value**
```python
for i in range(1, 10):
    if i == 5:
        break
    print(f"Number: {i}")
```
**Output**:
```
Number: 1
Number: 2
Number: 3
Number: 4
```

**Step 5: Using `continue`**
The `continue` statement skips the current iteration and proceeds to the next one.

**Example: Skip Odd Numbers**

```python
for i in range(1, 6):
    if i % 2 != 0:  # Skip odd numbers
        continue
    print(f"Even number: {i}")
```
**Output**:
```
Even number: 2
Even number: 4
```

**Step 6: Using `pass`**
The `pass` statement is a placeholder that does nothing, often used when a loop or block requires no action yet.

**Example: Placeholder for Future Code**

```python
for i in range(1, 4):
    if i == 2:
        pass  # TODO: Add logic later
    else:
        print(f"Number: {i}")
```
**Output**:
```
Number: 1
Number: 3
```

#### 5. Nested Loops
Nested loops are loops within loops, useful for working with multi-dimensional data (e.g., matrices) or generating combinations.

**Syntax**

```
for outer_variable in outer_sequence:
    for inner_variable in inner_sequence:
        # Code block
```

**Step 7: Loops Within Loops**
Nested loops allow you to iterate over multiple sequences simultaneously.

**Example: Printing a Grid**

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row}, {col})", end=" ")
    print()  # New line after each row
```
**Output**:
```
(1, 1) (1, 2) (1, 3) 
(2, 1) (2, 2) (2, 3) 
(3, 1) (3, 2) (3, 3)
```

#### 6. Practical Example: Number Guessing Game

This example combines `while`, `break`, and user input to create a number guessing game.

```
import random

secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("Guess the number between 1 and 10. You have 3 attempts.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempt(s).")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    
    if attempts == max_attempts:
        print(f"Game over! The number was {secret_number}.")
```
**Sample Run** (Input: `2`, `8`, `5` with secret number `5`):
```
Guess the number between 1 and 10. You have 3 attempts.
Enter your guess: 2
Too low!
Enter your guess: 8
Too high!
Enter your guess: 5
Congratulations! You guessed it in 3 attempt(s).
```

#### 7. Common Pitfalls and Best Practices

- **Infinite Loops**: Ensure `while` loop conditions will eventually become `False` to avoid infinite loops. For example, always update the loop variable.
  ```python
  # Bad: Infinite loop
  while True:
      print("This will run forever!")
  ```
  ```python
  # Good: Controlled loop
  count = 0
  while count < 3:
      print("Controlled loop")
      count += 1
  ```

- **Overusing Loops**: For simple iterations over sequences, consider list comprehensions or built-in functions like `sum()` or `map()` to improve readability.
  ```python
  # Verbose
  total = 0
  for num in [1, 2, 3]:
      total += num
  ```
  ```python
  # Concise
  total = sum([1, 2, 3])
  ```

- **Indentation Errors**: Use consistent indentation (4 spaces) to avoid `IndentationError`.
- **Clear Loop Logic**: Use descriptive variable names (e.g., `item` instead of `i` for lists) to improve code readability.

#### 8. Advanced Example: Multiplication Table Generator

This example uses nested `for` loops to generate a multiplication table.

```python
print("Multiplication Table (1 to 5)")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")
    print()  # New line after each row
```
**Output**:
```
Multiplication Table (1 to 5)
 1  2  3  4  5 
 2  4  6  8 10 
 3  6  9 12 15 
 4  8 12 16 20 
 5 10 15 20 25
```

#### 9. Conclusion
Loops are a fundamental part of Python programming, enabling you to handle repetitive tasks efficiently. By mastering `for` and `while` loops, loop control statements, and nested loops, you can tackle a wide range of problems, from simple iterations to complex data processing. Practice with real-world scenarios like games or data generation to solidify your understanding.


### 3. Functions

Functions in Python are reusable blocks of code that perform specific tasks, promoting modularity and code reusability. They allow you to organize code, reduce repetition, and make programs easier to maintain. This guide provides a step-by-step learning process for all types of functions in Python, including defining functions, handling parameters, returning values, and advanced function concepts, with practical examples and best practices.

#### 1. Introduction to Functions

A function is a block of code that performs a specific task and can be called multiple times from different parts of a program. Functions improve code organization, readability, and reusability. Python supports various function types, including:

- **Regular Functions**: Defined with the `def` keyword.
- **Lambda Functions**: Anonymous, single-expression functions.
- **Recursive Functions**: Functions that call themselves.
- **Nested Functions**: Functions defined inside other functions.

Functions can accept inputs (parameters), process them, and return outputs.

#### 2. Defining a Function

Functions are defined using the `def` keyword, followed by the function name, parentheses for parameters, and a colon. The function body is indented.

**Syntax**

```python
def function_name(parameters):
    # Code block
    return value  # Optional
```

**Step 1: Basic Function Definition**
Create a simple function without parameters that performs a task.

**Example: Greeting Function**
```python
def say_hello():
    print("Hello, World!")
    
say_hello()
```
**Output**:
```
Hello, World!
```

#### 3. Functions with Parameters

Parameters allow functions to accept input values and process them.

**Step 2: Positional Parameters**
Positional parameters are passed in the order they are defined.

**Example: Adding Two Numbers**

```python
def add_numbers(a, b):
    result = a + b
    print(f"Sum of {a} and {b} is {result}")

add_numbers(5, 3)
```
**Output**:
```
Sum of 5 and 3 is 8
```

**Step 3: Default Parameters**
Default parameters have predefined values, used if no argument is provided.

**Example: Greeting with Default Name**
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Uses default value
greet("Alice")   # Uses provided value
```
**Output**:
```
Hello, Guest!
Hello, Alice!
```

**Step 4: Keyword Arguments**
Keyword arguments allow you to specify arguments by parameter name, ignoring order.

**Example: Order Details**
```python
def order_food(item, quantity=1):
    print(f"Ordered {quantity} {item}(s)")

order_food(quantity=2, item="pizza")
```
**Output**:
```
Ordered 2 pizza(s)
```

#### 4. Variable-Length Arguments

Python allows functions to accept a variable number of arguments using `*args` and `**kwargs`.

**Step 5: Using `*args` for Positional Arguments**
`*args` collects extra positional arguments into a tuple.

**Example: Summing Multiple Numbers**
```python
def sum_numbers(*args):
    total = sum(args)
    print(f"Sum: {total}")

sum_numbers(1, 2, 3, 4)
```
**Output**:
```
Sum: 10
```

**Step 6: Using `**kwargs` for Keyword Arguments**
`**kwargs` collects extra keyword arguments into a dictionary.

**Example: User Profile**

```
def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name="Bob", age=30, city="New York")
```
**Output**:
```
name: Bob
age: 30
city: New York
```

#### 5. Return Statements

The `return` statement sends a value back to the caller. If omitted, the function returns `None`.

**Step 7: Returning Values**
Use `return` to output results for further use.

**Example: Area of a Rectangle**
```
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)
print(f"Area: {area} square units")
```
**Output**:
```
Area: 15 square units
```

**Example: Multiple Return Values**

```python
def get_dimensions():
    return 10, 20  # Returns a tuple

length, width = get_dimensions()
print(f"Length: {length}, Width: {width}")
```
**Output**:
```
Length: 10, Width: 20
```

#### 6. Lambda Functions

Lambda functions are small, anonymous functions defined using the `lambda` keyword. They are limited to a single expression.

**Syntax**

```python
lambda arguments: expression
```

**Step 8: Anonymous Functions**

Use lambda functions for simple operations or as arguments to higher-order functions.

**Example: Square a Number**

```python
square = lambda x: x * x
print(square(5))
```
**Output**:
```
25
```

**Example: Sorting with Lambda**

```python
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)
```
**Output**:
```
[(1, 'one'), (3, 'three'), (2, 'two')]
```

#### 7. Recursive Functions

A recursive function calls itself to solve a problem by breaking it into smaller instances.

**Step 9: Functions Calling Themselves**

Ensure a base case to prevent infinite recursion.

**Example: Factorial**

```python
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))
```
**Output**:
```
120
```

#### 8. Nested Functions

Functions defined inside other functions are called nested functions, often used for encapsulation or helper functions.

**Step 10: Functions Within Functions**

Nested functions can access variables from their enclosing scope.

**Example: Outer and Inner Functions**

```python
def outer_function(msg):
    def inner_function():
        print(f"Message: {msg}")
    inner_function()

outer_function("Hello!")
```
**Output**:
```
Message: Hello!
```

#### 9. Practical Example: Shopping Cart Calculator

This example combines multiple function concepts to calculate the total cost in a shopping cart.

```
def calculate_total(items, discount_rate=0):
    total = sum(items.values())
    discount = total * discount_rate
    return total - discount

def print_receipt(customer, *items, **details):
    print(f"Receipt for {customer}:")
    for item, price in items:
        print(f"{item}: ${price}")
    total = calculate_total(details, discount_rate=details.get('discount', 0))
    print(f"Total: ${total:.2f}")

print_receipt("Alice", ("apple", 1), ("bread", 2), total=3, discount=0.1)
```
**Output**:
```
Receipt for Alice:
apple: $1
bread: $2
Total: $2.70
```

#### 10. Common Pitfalls and Best Practices

- **Missing Return**: If a function doesn’t explicitly return a value, it returns `None`. Always ensure intended returns.
  ```python
  # Bad: Missing return
  def add(a, b):
      a + b  # No return
  print(add(2, 3))  # Outputs: None
  ```
  ```python
  # Good: Explicit return
  def add(a, b):
      return a + b
  print(add(2, 3))  # Outputs: 5
  ```

- **Overusing Global Variables**: Avoid modifying global variables inside functions; use parameters and returns instead.
- **Descriptive Names**: Use meaningful function names (e.g., `calculate_area` instead of `func`) and parameter names.
- **Keep Functions Focused**: Each function should perform one task (Single Responsibility Principle).
- **Document Functions**: Use docstrings to explain the function’s purpose, parameters, and return values.
  ```python
  def divide(a, b):
      """Divides a by b and returns the quotient.
      
      Args:
          a (float): Numerator
          b (float): Denominator
          
      Returns:
          float: Result of division, or None if b is 0
      """
      if b == 0:
          return None
      return a / b
  ```

#### 11. Advanced Example: Temperature Converter

This example uses functions to convert temperatures between Celsius, Fahrenheit, and Kelvin.

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature(value, unit):
    """Converts temperature between Celsius, Fahrenheit, and Kelvin."""
    unit = unit.lower()
    if unit == "celsius":
        return {
            "fahrenheit": celsius_to_fahrenheit(value),
            "kelvin": value + 273.15
        }
    elif unit == "fahrenheit":
        celsius = fahrenheit_to_celsius(value)
        return {
            "celsius": celsius,
            "kelvin": celsius + 273.15
        }
    elif unit == "kelvin":
        celsius = value - 273.15
        return {
            "celsius": celsius,
            "fahrenheit": celsius_to_fahrenheit(celsius)
        }
    else:
        return None

result = convert_temperature(25, "celsius")
print(f"25°C = {result['fahrenheit']:.2f}°F, {result['kelvin']:.2f}K")
```
**Output**:
```
25°C = 77.00°F, 298.15K
```

#### 12. Conclusion

Functions are a cornerstone of Python programming, enabling modular, reusable, and maintainable code. By mastering function definitions, parameters, return statements, lambda functions, recursion, and nested functions, you can build robust applications. Practice with real-world scenarios like calculators or converters to deepen your understanding.


### 4. Exception Handling

Below is a comprehensive lesson on **Python Exception Handling**, formatted for a GitHub `README.md` file. It provides a step-by-step learning process covering all aspects of exception handling in Python, including try-except blocks, multiple exceptions, custom exceptions, the `else` and `finally` clauses, and raising exceptions. The guide includes detailed explanations, examples, tables, best practices, and practical scenarios to help learners understand exception handling effectively.



# Python Exception Handling: A Comprehensive Guide

Exception handling in Python allows you to manage errors gracefully, ensuring your program continues running or fails safely when unexpected situations occur. By handling exceptions, you can prevent crashes, provide meaningful feedback, and maintain robust applications. This guide provides a step-by-step learning process for all types of exception handling in Python, including try-except blocks, multiple exceptions, custom exceptions, and more, with practical examples and best practices.

## Table of Contents
- [1. Introduction to Exception Handling](#1-introduction-to-exception-handling)
- [2. The `try` and `except` Blocks](#2-the-try-and-except-blocks)
  - [Step 1: Basic Exception Handling](#step-1-basic-exception-handling)
- [3. Handling Multiple Exceptions](#3-handling-multiple-exceptions)
  - [Step 2: Catching Specific Exceptions](#step-2-catching-specific-exceptions)
  - [Step 3: Catching Multiple Exceptions](#step-3-catching-multiple-exceptions)
- [4. The `else` Clause](#4-the-else-clause)
  - [Step 4: Code to Run When No Exception Occurs](#step-4-code-to-run-when-no-exception-occurs)
- [5. The `finally` Clause](#5-the-finally-clause)
  - [Step 5: Code That Always Runs](#step-5-code-that-always-runs)
- [6. Raising Exceptions](#6-raising-exceptions)
  - [Step 6: Using the `raise` Statement](#step-6-using-the-raise-statement)
- [7. Custom Exceptions](#7-custom-exceptions)
  - [Step 7: Defining Your Own Exceptions](#step-7-defining-your-own-exceptions)
- [8. Practical Example: File Processing with Exception Handling](#8-practical-example-file-processing-with-exception-handling)
- [9. Common Exceptions in Python](#9-common-exceptions-in-python)
- [10. Common Pitfalls and Best Practices](#10-common-pitfalls-and-best-practices)
- [11. Advanced Example: User Input Validator](#11-advanced-example-user-input-validator)
- [12. Conclusion](#12-conclusion)

## 1. Introduction to Exception Handling

An **exception** is an error that occurs during program execution, disrupting the normal flow. Without handling, exceptions cause the program to crash. Python’s exception handling mechanism uses `try`, `except`, `else`, and `finally` blocks to catch and manage errors, and the `raise` statement to trigger exceptions intentionally. You can also define custom exceptions for specific needs.

## 2. The `try` and `except` Blocks

The `try` block contains code that might raise an exception, and the `except` block handles the exception if it occurs.

### Syntax
```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
```

### Step 1: Basic Exception Handling
Use a `try-except` block to catch any exception and prevent a crash.

#### Example: Division by Zero
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```
**Output**:
```
Error: Cannot divide by zero!
```

## 3. Handling Multiple Exceptions

You can handle specific exceptions or multiple types of exceptions in a single `try` block.

### Step 2: Catching Specific Exceptions
Catch a specific exception type to handle it appropriately.

#### Example: Handling TypeError
```python
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
```
**Output**:
```
Error: Invalid input! Please enter a number.
```

### Step 3: Catching Multiple Exceptions
Use multiple `except` blocks or a tuple of exception types to handle different errors.

#### Example: Multiple Exceptions
```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Error: Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```
**Sample Run** (Input: `0`):
```
Enter a number: 0
Error: Cannot divide by zero!
```

#### Example: Catching Multiple Exceptions in One Block
```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")
```
**Sample Run** (Input: `abc`):
```
Enter a number: abc
Error occurred: invalid literal for int() with base 10: 'abc'
```

## 4. The `else` Clause

The `else` clause runs if no exception is raised in the `try` block.

### Step 4: Code to Run When No Exception Occurs
Use `else` to execute code only when the `try` block succeeds.

#### Example: Safe Division
```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Error: Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print(f"Result: {result}")
```
**Sample Run** (Input: `5`):
```
Enter a number: 5
Result: 20.0
```

## 5. The `finally` Clause

The `finally` clause runs regardless of whether an exception occurs, useful for cleanup tasks (e.g., closing files).

### Step 5: Code That Always Runs
Use `finally` to ensure code executes even if an exception is raised or not.

#### Example: Resource Cleanup
```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
else:
    print("File read successfully!")
finally:
    print("Closing file...")
    try:
        file.close()
    except NameError:
        pass  # File was never opened
```
**Output** (if `example.txt` doesn’t exist):
```
Error: File not found!
Closing file...
```

## 6. Raising Exceptions

The `raise` statement allows you to trigger exceptions intentionally.

### Step 6: Using the `raise` Statement
Raise an exception when a condition is met to enforce rules or signal errors.

#### Example: Age Validation
```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")
```
**Output**:
```
Error: Age cannot be negative!
```

## 7. Custom Exceptions

You can define custom exceptions by creating a class that inherits from the built-in `Exception` class.

### Step 7: Defining Your Own Exceptions
Create custom exceptions for specific error scenarios.

#### Example: Custom Exception for Insufficient Balance
```python
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough funds to withdraw!")
    return balance - amount

try:
    balance = 100
    new_balance = withdraw(balance, 150)
except InsufficientBalanceError as e:
    print(f"Error: {e}")
else:
    print(f"New balance: {new_balance}")
```
**Output**:
```
Error: Not enough funds to withdraw!
```

## 8. Practical Example: File Processing with Exception Handling

This example demonstrates exception handling in a file-processing scenario.

```python
def read_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("File is empty!")
            return lines
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("File operation completed.")

result = read_file("data.txt")
if result:
    print("File contents:", result)
```
**Output** (if `data.txt` doesn’t exist):
```
Error: data.txt not found!
File operation completed.
```

## 9. Common Exceptions in Python

Below is a table of common built-in exceptions in Python:

| Exception            | Description                                      |
|----------------------|--------------------------------------------------|
| `ZeroDivisionError`  | Raised when dividing by zero                    |
| `ValueError`         | Raised when a function receives an invalid value |
| `TypeError`          | Raised when an operation is performed on an inappropriate type |
| `FileNotFoundError`  | Raised when a file cannot be found              |
| `IndexError`         | Raised when an index is out of range            |
| `KeyError`           | Raised when a dictionary key is not found       |
| `AttributeError`     | Raised when an attribute is not found           |
| `Exception`          | Base class for all exceptions; catches all if unspecified |

## 10. Common Pitfalls and Best Practices

- **Catching Specific Exceptions**: Avoid using a bare `except` clause as it catches all exceptions, including unexpected ones, making debugging harder.
  ```python
  # Bad: Too broad
  try:
      num = int("abc")
  except:
      print("An error occurred!")  # Hides the specific error
  ```
  ```python
  # Good: Specific
  try:
      num = int("abc")
  except ValueError:
      print("Invalid input! Please enter a number.")
  ```

- **Avoid Overusing Exceptions**: Don’t use exceptions for flow control (e.g., checking conditions that can be handled with `if` statements).
- **Use Meaningful Messages**: Provide clear error messages in `raise` statements and custom exceptions.
- **Clean Up Resources**: Use `finally` or context managers (`with` statement) to ensure resources like files or connections are closed.
- **Log Exceptions**: In production code, log exceptions for debugging using the `logging` module.
  ```python
  import logging
  logging.basicConfig(level=logging.ERROR)
  try:
      result = 10 / 0
  except ZeroDivisionError as e:
      logging.error(f"Error occurred: {e}")
  ```

## 11. Advanced Example: User Input Validator

This example validates user input for a registration system, combining multiple exception handling techniques.

```python
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format!")

def register_user(name, age, email):
    try:
        if not name:
            raise ValueError("Name cannot be empty!")
        age = int(age)
        if age < 18:
            raise ValueError("User must be at least 18!")
        validate_email(email)
    except ValueError as e:
        print(f"Validation error: {e}")
    except InvalidEmailError as e:
        print(f"Email error: {e}")
    else:
        print(f"User registered: {name}, Age: {age}, Email: {email}")
    finally:
        print("Registration attempt completed.")

register_user("Alice", "25", "alice@example.com")
register_user("", "20", "bob@example.com")
register_user("Bob", "15", "bob@example.com")
register_user("Charlie", "30", "invalid_email")
```
**Output**:
```
User registered: Alice, Age: 25, Email: alice@example.com
Registration attempt completed.
Validation error: Name cannot be empty!
Registration attempt completed.
Validation error: User must be at least 18!
Registration attempt completed.
Email error: Invalid email format!
Registration attempt completed.
```

## 12. Conclusion

Exception handling is crucial for building robust Python applications. By mastering `try-except`, `else`, `finally`, raising exceptions, and custom exceptions, you can handle errors gracefully and ensure your program remains stable. Practice with real-world scenarios like file processing or input validation to solidify your understanding.



This guide is formatted for GitHub’s `README.md`, with markdown headers, tables, code blocks, and a table of contents for easy navigation. You can copy this content into a `README.md` file in your GitHub repository. If you need additional examples, specific modifications, or further clarification, let me know!



### 5. Objects and Classes
