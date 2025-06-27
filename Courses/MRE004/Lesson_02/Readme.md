# Lesson 2 Meet the NumPy Array
The NumPy array, or `ndarray` (N-dimensional array), is the core data structure of the NumPy library, designed for high-performance numerical computing in Python. Unlike Python's built-in lists, NumPy arrays are homogeneous (all elements must be of the same data type) and stored in contiguous memory blocks, enabling faster computations through vectorized operations and optimized C-based backend processing. These arrays can be **one-dimensional (1D)**, like vectors; **two-dimensional (2D)**, like matrices; or **multi-dimensional (nD)**, supporting complex data structures used in scientific computing, image processing, and machine learning. Key features of NumPy arrays include **broadcasting** (element-wise operations on arrays of different shapes), **slicing and indexing** for efficient data access, and support for a wide range of **mathematical functions** (linear algebra, statistics, Fourier transforms). Additionally, NumPy arrays seamlessly integrate with other libraries like Pandas, SciPy, and TensorFlow, making them indispensable for data analysis, simulations, and AI applications. Their efficiency, flexibility, and interoperability make NumPy arrays the foundation of numerical computing in Python.

**Importing NumPy Library**

```
import numpy as np
```

**one-dimensional (1D)**

```
# Create a 1D array
list1 = [1, 2, 3, 4]
array1 = np.array(list1)
print("1D Array:", array1)
```

**two-dimensional (2D)**
```
# Create a 2D array
list2 = [[1, 2, 3], [4, 5, 6]]
array2 = np.array(list2)
print("2D Array:\n", array2)
```
**multi-dimensional (nD)**
```
# prompt: write example for multi-dimensional (nD)

# Create a 3D array
list3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
array3 = np.array(list3)
print("3D Array:\n", array3)

# Create a 4D array
list4 = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
array4 = np.array(list4)
print("4D Array:\n", array4)

# You can create arrays of any dimension by nesting lists accordingly.
# The number of opening brackets `[` at the beginning of the innermost list determines the dimension.
```

**NumPy Arrays vs Python Lists**
```
# prompt: write example for NumPy Arrays vs Python Lists

import time

# Example illustrating the difference in speed for operations
size = 1000000
list_a = list(range(size))
list_b = list(range(size))
array_a = np.arange(size)
array_b = np.arange(size)

# List addition
start_time = time.time()
result_list = [list_a[i] + list_b[i] for i in range(size)]
end_time = time.time()
print(f"\nTime for list addition: {end_time - start_time:.6f} seconds")

# NumPy array addition
start_time = time.time()
result_array = array_a + array_b
end_time = time.time()
print(f"Time for NumPy array addition: {end_time - start_time:.6f} seconds")


# Example illustrating memory usage difference
import sys

list_memory = sys.getsizeof(list_a)
array_memory = array_a.nbytes

print(f"\nMemory used by list: {list_memory} bytes")
print(f"Memory used by NumPy array: {array_memory} bytes")


# Example illustrating convenience of operations

list_mult = [1, 2, 3]
# list_mult * 2 would repeat the list: [1, 2, 3, 1, 2, 3]

array_mult = np.array([1, 2, 3])
array_mult_result = array_mult * 2 # Multiplies each element: [2, 4, 6]

print(f"\nList multiplication (repeats): {list_mult * 2}")
print(f"NumPy array multiplication (element-wise): {array_mult * 2}")

# Example of element-wise operations not easily done with lists
list_sqrt = [1, 4, 9]
# To get square roots with lists, you need a loop or list comprehension
list_sqrt_result = [x**0.5 for x in list_sqrt]

array_sqrt = np.array([1, 4, 9])
array_sqrt_result = np.sqrt(array_sqrt) # Applies square root to each element

print(f"\nList square root: {list_sqrt_result}")
print(f"NumPy array square root: {array_sqrt_result}")
```

