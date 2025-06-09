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
### 3. Functions
### 4. Exception Handling
### 5. Objects and Classes
