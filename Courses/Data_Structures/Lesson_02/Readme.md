# Lesson 02 Recursion, Sorting, and Searching Algorithms

## 1. Recursion

Definition:
Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller subproblems. It relies on two key components:
- Base Case: A condition that stops the recursion (prevents infinite loops).
- Recursive Case: A step that reduces the problem into a smaller instance of the same problem.

Example: Factorial Calculation
```
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n-1)
```

Mechanics:
- Each recursive call adds a frame to the call stack, storing local variables and parameters.
- The stack unwinds when the base case is reached, returning values back up the stack.

Pros & Cons:
- ✔️ Simplifies code for problems like tree traversals, Tower of Hanoi.

- ❌ Higher memory usage (risk of stack overflow) and potential inefficiency compared to iteration.

Advanced Topics:
Tail Recursion: A recursive call is the last operation. Some languages optimize this to avoid stack growth.
Indirect Recursion: Functions A and B call each other (e.g., A → B → A).
