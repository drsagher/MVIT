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

## 2. Sorting Algorithms

### Overview:
Sorting rearranges data in ascending/descending order. Key metrics include time complexity, space complexity, and stability (preserves order of equal elements).

### A. O(n²) Algorithms

#### Bubble Sort:
Compares adjacent elements and swaps them if out of order.
Time: O(n²) worst/average case; Space: O(1).
Use Case: Small datasets or educational purposes.

#### Selection Sort:
Selects the smallest element and swaps it into place.
Time: O(n²); Space: O(1).
Unstable (e.g., swaps can disrupt order).

#### Insertion Sort:
Builds a sorted array by inserting elements one at a time.
Time: O(n²) worst case, O(n) best (already sorted); Space: O(1).
Use Case: Small or nearly sorted data.

### B. O(n log n) Algorithms
#### Merge Sort:
Divide & Conquer: Splits the array, sorts subarrays, and merges them.
Time: O(n log n); Space: O(n) (not in-place).
Stable; ideal for linked lists/external sorting.

#### Quick Sort:
Selects a pivot, partitions the array into elements < pivot and > pivot, then recurses.
Time: O(n log n) average, O(n²) worst (bad pivot choice); Space: O(log n) stack.
Unstable but fast in practice.

#### Heap Sort:
Builds a max-heap and repeatedly extracts the maximum element.
Time: O(n log n); Space: O(1).
Use Case: In-place sorting with guaranteed O(n log n).

### C. Non-Comparison Sorts
#### Counting Sort:
Counts occurrences of each element (works for integer keys in a range).
Time: O(n + k), where k is the range of keys.

#### Radix Sort:
Sorts by processing digits from least to most significant.
Time: O(nk) for k digits.

## 3. Searching Algorithms

#### A. Linear Search:
Checks each element sequentially.
Time: O(n); Space: O(1).
Use Case: Unsorted data or small datasets.

#### B. Binary Search:
Requires a sorted array. Repeatedly divides the search interval in half.
Time: O(log n); Space: O(1) (iterative) or O(log n) (recursive).

Example:
```
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

#### C. Interpolation Search:
Estimates the position of the target using formula:
pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
Time: O(log log n) for uniformly distributed data.

Trade-offs:
Sorting data (O(n log n)) + Binary Search (O(log n)) is efficient for multiple searches.
Linear Search is better for single searches on unsorted data.
