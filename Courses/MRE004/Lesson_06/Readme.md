# Lesson 6 Array Operations and NumPy Functions

Array Operations and NumPy Functions form the backbone of numerical computing in Python, enabling efficient and intuitive manipulation of large datasets. NumPy provides a wide range of built-in functions that allow element-wise operations such as addition, subtraction, multiplication, and division across entire arrays, eliminating the need for cumbersome loops. These operations are performed in optimized C-based code under the hood, making them significantly faster and more memory-efficient than equivalent operations in native Python. In addition to basic arithmetic, NumPy offers a comprehensive suite of mathematical and statistical functions—including `np.sum()`, `np.mean()`, `np.std()`, `np.min()`, and `np.max()`—that operate on arrays to compute aggregate results along specified axes. Advanced operations like broadcasting enable arrays of different shapes to interact in computations, expanding dimensions automatically to make shapes compatible. Other essential functions such as `np.reshape()`, `np.concatenate()`, `np.split()`, and `np.transpose()` provide powerful tools for array manipulation, transformation, and restructuring. With these capabilities, NumPy simplifies complex numerical tasks, making it an indispensable library for scientific computing, data analysis, and machine learning.

1. Element-Wise Arithmetic Operations
NumPy supports element-wise arithmetic operations (addition, subtraction, multiplication, division, etc.) on arrays of the same shape or compatible shapes via broadcasting. These operations are vectorized, meaning they are applied to each element without explicit loops, ensuring high performance.
Example: Arithmetic Operations
import numpy as np

# Create two arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Element-wise operations
print(a + b)  # Output: [ 6  8 10 12]  # Addition
print(a - b)  # Output: [-4 -4 -4 -4ევ

System: 4]  # Subtraction
print(a * b)  # Output: [ 5 12 21 32]  # Multiplication
print(a / b)  # Output: [0.2 0.33333333 0.42857143 0.5]  # Division
print(a ** 2)  # Output: [ 1  4  9 16]  # Power

Key Points

Arrays must have compatible shapes or use broadcasting (covered later).
Operations are performed element-wise, producing an array of the same shape.
Use caution with division by zero, which may result in np.inf or np.nan.

2. Universal Functions (ufuncs)
NumPy’s universal functions (ufuncs) apply mathematical operations element-wise, such as trigonometric, exponential, and logarithmic functions. These functions are optimized for arrays and support a wide range of mathematical operations.
Example: Mathematical Functions
arr = np.array([0, np.pi/2, np.pi])

# Trigonometric functions
print(np.sin(arr))  # Output: [0. 1. 1.22464680e-16]  # Sine
print(np.cos(arr))  # Output: [ 1.  6.12323400e-17 -1.]  # Cosine

# Exponential and logarithmic functions
print(np.exp(arr))  # Output: [ 1.          4.81047738 23.14069263]  # e^x
print(np.log(arr))  # Output: [-inf  0.45158271  1.14472989]  # Natural log

Key Points

Common ufuncs include np.sin, np.cos, np.tan, np.exp, np.log, np.sqrt, etc.
Ufuncs handle np.nan and np.inf appropriately, propagating them as needed.
Use np.seterr to control behavior for invalid operations (e.g., division by zero).

3. Statistical Operations
NumPy provides functions to compute statistical measures across arrays, such as mean, median, standard deviation, and more. These functions can operate along specific axes or the entire array.
Example: Statistical Operations
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Basic statistics
print(np.mean(arr))         # Output: 3.5  # Mean of all elements
print(np.median(arr))       # Output: 3.5  # Median
print(np.std(arr))          # Output: 1.70782513  # Standard deviation
print(np.var(arr))          # Output: 2.91666667  # Variance
print(np.min(arr))          # Output: 1  # Minimum
print(np.max(arr))          # Output: 6  # Maximum

# Axis-specific statistics
print(np.mean(arr, axis=0)) # Output: [2.5 3.5 4.5]  # Mean of each column
print(np.sum(arr, axis=1))  # Output: [ 6 15]  # Sum of each row

Key Points

Use axis parameter to compute statistics along rows (axis=1) or columns (axis=0).
Functions like np.nanmean, np.nanstd, etc., ignore np.nan values.
Statistical operations are efficient for large datasets due to vectorization.

4. Logical and Comparison Operations
Logical and comparison operations produce boolean arrays, useful for filtering, masking, or conditional operations. These operations are also element-wise.
Example: Logical and Comparison Operations
a = np.array([1, 2, 3, 4])
b = np.array([2, 2, 2, 2])

# Comparison operations
print(a == b)  # Output: [False True False False]  # Equality
print(a > b)   # Output: [False False True True]  # Greater than

# Logical operations
mask = (a > 2) & (b == 2)
print(mask)    # Output: [False False True True]  # AND
print(a[mask]) # Output: [3 4]  # Filter using boolean mask

# Any and all
print(np.any(a > 3))  # Output: True  # Any element > 3
print(np.all(b == 2)) # Output: True  # All elements == 2

Key Points

Comparison operators: ==, !=, <, >, <=, >=.
Logical operators: & (and), | (or), ~ (not).
Use np.any and np.all to check conditions across arrays or axes.

5. Linear Algebra Operations
NumPy’s linalg module provides functions for linear algebra operations, such as matrix multiplication, dot products, determinants, and eigenvalues, critical for scientific and machine learning applications.
Example: Linear Algebra Operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print(np.matmul(A, B))  # Output: [[19 22] [43 50]]
print(A @ B)            # Output: [[19 22] [43 50]]  # Alternative syntax

# Dot product (for vectors or matrices)
print(np.dot(A, B))     # Output: [[19 22] [43 50]]

# Determinant and inverse
print(np.linalg.det(A)) # Output: -2.0
print(np.linalg.inv(A)) # Output: [[-2.   1. ] [ 1.5 -0.5]]

# Eigenvalues and eigenvectors
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)          # Output: [-0.37228132  5.37228132]

Key Points

np.matmul or @ is used for matrix multiplication; np.dot is similar but also works for vectors.
Ensure matrices have compatible shapes for operations (e.g., (m, n) @ (n, p)).
Linear algebra functions are optimized for numerical stability and performance.

6. Broadcasting
Broadcasting allows NumPy to perform operations on arrays of different shapes by automatically expanding their dimensions to match. This is a powerful feature that eliminates the need for explicit looping or reshaping.
Broadcasting Rules

Arrays with fewer dimensions are padded with ones on the left.
Arrays with equal dimensions are compatible if their sizes match or one is 1.
Arrays are stretched to match the largest compatible shape.

Example: Broadcasting
a = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
b = np.array([10, 20, 30])           # Shape: (3,)

# Broadcasting b to match a’s shape
print(a + b)  # Output: [[11 22 33] [14 25 36]]

# Scalar broadcasting
print(a * 2)  # Output: [[ 2  4  6] [ 8 10 12]]

# 2D array with a 1D column array
c = np.array([[100], [200]])  # Shape: (2, 1)
print(a + c)  # Output: [[101 102 103] [204 205 206]]

Key Points

Broadcasting is memory-efficient, as it avoids creating large temporary arrays.
Check array shapes with arr.shape to ensure compatibility.
Broadcasting errors occur if shapes are incompatible (e.g., (2, 3) and (4,)).

7. Practical Example: Data Analysis with Array Operations
Let’s apply array operations to analyze a dataset of student scores across three subjects for five students.
# Student scores (5 students, 3 subjects)
scores = np.array([[85, 90, 88], [78, 82, 80], [92, 95, 90], [65, 70, 68], [88, 85, 87]])

# Compute average score per student
student_means = np.mean(scores, axis=1)
print("Student averages:", student_means)
# Output: [87.66666667 80.         92.33333333 67.66666667 86.66666667]

# Normalize scores (subtract mean and divide by standard deviation)
subject_means = np.mean(scores, axis=0)
subject_std = np.std(scores, axis=0)
normalized_scores = (scores - subject_means) / subject_std
print("Normalized scores:\n", normalized_scores)
# Output: [[ 0.10482848  0.70710678  0.39223227]
#          [-0.62776951 -0.14142136 -0.39223227]
#          [ 0.83742647  1.06066018  0.78446454]
#          [-1
