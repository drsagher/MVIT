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

Below is a comprehensive lesson on **Python Loops**, formatted for a GitHub `README.md` file. It provides a step-by-step learning process covering all types of loops in Python (`for`, `while`, nested loops, and loop control statements like `break`, `continue`, and `pass`). The guide includes detailed explanations, examples, tables, best practices, and practical scenarios to help beginners and intermediate learners understand loops effectively.



# Python Loops: A Comprehensive Guide

Loops in Python allow you to execute a block of code repeatedly based on a condition or over a sequence of items. They are essential for automating repetitive tasks and processing collections of data. This guide provides a step-by-step learning process for all types of loops in Python, including `for`, `while`, nested loops, and loop control statements, with practical examples and best practices.

## Table of Contents
- [1. Introduction to Loops](#1-introduction-to-loops)
- [2. The `for` Loop](#2-the-for-loop)
  - [Step 1: Iterating Over Sequences](#step-1-iterating-over-sequences)
  - [Step 2: Using `range()`](#step-2-using-range)
- [3. The `while` Loop](#3-the-while-loop)
  - [Step 3: Condition-Based Looping](#step-3-condition-based-looping)
- [4. Loop Control Statements](#4-loop-control-statements)
  - [Step 4: Using `break`](#step-4-using-break)
  - [Step 5: Using `continue`](#step-5-using-continue)
  - [Step 6: Using `pass`](#step-6-using-pass)
- [5. Nested Loops](#5-nested-loops)
  - [Step 7: Loops Within Loops](#step-7-loops-within-loops)
- [6. Practical Example: Number Guessing Game](#6-practical-example-number-guessing-game)
- [7. Common Pitfalls and Best Practices](#7-common-pitfalls-and-best-practices)
- [8. Advanced Example: Multiplication Table Generator](#8-advanced-example-multiplication-table-generator)
- [9. Conclusion](#9-conclusion)

## 1. Introduction to Loops

Loops allow you to repeat a block of code multiple times, either for a fixed number of iterations or until a condition is met. Python supports two primary loop types:

- **`for` Loop**: Iterates over a sequence (e.g., list, tuple, string, or range).
- **`while` Loop**: Repeats as long as a condition is `True`.

Additionally, Python provides loop control statements (`break`, `continue`, `pass`) to modify loop behavior and supports nested loops for complex iterations.

> **Note**: Python uses indentation (typically 4 spaces) to define the scope of loop code blocks.

## 2. The `for` Loop

The `for` loop is used to iterate over a sequence (e.g., list, tuple, string, or `range()` object). It’s ideal for tasks where the number of iterations is known or based on a sequence.

### Syntax
```python
for variable in sequence:
    # Code block to execute
```

### Step 1: Iterating Over Sequences
You can loop over elements in a list, tuple, string, or other iterable objects.

#### Example: Iterating Over a List
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

#### Example: Iterating Over a String
```python
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

### Step 2: Using `range()`
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

#### Example: Using `range()` with Step
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

## 3. The `while` Loop

The `while` loop continues executing a block of code as long as a condition is `True`. It’s useful when the number of iterations is unknown.

### Syntax
```python
while condition:
    # Code block to execute
```

### Step 3: Condition-Based Looping
Use a `while` loop when you need to repeat an action until a specific condition changes.

#### Example: Counting Down
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

#### Example: User Input Validation
```python
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

## 4. Loop Control Statements

Python provides three control statements to modify loop behavior:

| Statement | Description                                      |
|-----------|--------------------------------------------------|
| `break`   | Exits the loop immediately                      |
| `continue`| Skips the rest of the current iteration         |
| `pass`    | Does nothing, used as a placeholder             |

### Step 4: Using `break`
The `break` statement terminates the loop prematurely when a condition is met.

#### Example: Stop at a Specific Value
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

### Step 5: Using `continue`
The `continue` statement skips the current iteration and proceeds to the next one.

#### Example: Skip Odd Numbers
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

### Step 6: Using `pass`
The `pass` statement is a placeholder that does nothing, often used when a loop or block requires no action yet.

#### Example: Placeholder for Future Code
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

## 5. Nested Loops

Nested loops are loops within loops, useful for working with multi-dimensional data (e.g., matrices) or generating combinations.

### Syntax
```python
for outer_variable in outer_sequence:
    for inner_variable in inner_sequence:
        # Code block
```

### Step 7: Loops Within Loops
Nested loops allow you to iterate over multiple sequences simultaneously.

#### Example: Printing a Grid
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

## 6. Practical Example: Number Guessing Game

This example combines `while`, `break`, and user input to create a number guessing game.

```python
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

## 7. Common Pitfalls and Best Practices

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

## 8. Advanced Example: Multiplication Table Generator

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

## 9. Conclusion

Loops are a fundamental part of Python programming, enabling you to handle repetitive tasks efficiently. By mastering `for` and `while` loops, loop control statements, and nested loops, you can tackle a wide range of problems, from simple iterations to complex data processing. Practice with real-world scenarios like games or data generation to solidify your understanding.



This guide is formatted for GitHub’s `README.md`, with markdown headers, tables, code blocks, and a table of contents for easy navigation. You can copy this content into a `README.md` file in your GitHub repository. If you need additional examples, specific modifications, or further clarification, let me know!


### 3. Functions
### 4. Exception Handling
### 5. Objects and Classes
