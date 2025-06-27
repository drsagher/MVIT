# Lesson 4 Accessing and Slicing Array

NumPy arrays, the cornerstone of numerical computing in Python, offer powerful mechanisms for accessing and slicing elements, enabling efficient data manipulation in data science, machine learning, and scientific applications. Unlike Python lists, NumPy arrays support advanced indexing techniques, including integer indexing, slicing, boolean indexing, and fancy indexing, which allow for precise and optimized access to array elements. This lesson provides a comprehensive overview of accessing and slicing NumPy arrays, covering basic and advanced techniques with clear explanations and practical examples. By mastering these methods, you can efficiently extract, modify, or manipulate subsets of data in multi-dimensional arrays, a critical skill for data analysis and computational tasks.

**Basic Accessing with Integer Indexing**

Integer indexing allows you to access specific elements in a NumPy array by specifying their indices. NumPy arrays are zero-indexed, meaning the first element has an index of 0. For multi-dimensional arrays, you provide indices for each dimension.

**Accessing Elements**

```
import numpy as np

# 1D array
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d[2])  # Output: 30  # Access element at index 2

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[1, 2])  # Output: 6  # Access element at row 1, column 2
```

**Key Points**
- For a 1D array, use a single index: arr[i].
- For a 2D array, use two indices: arr[i, j] for row i, column j.
- Negative indices count from the end (e.g., -1 for the last element).

**Slicing NumPy Arrays**

Slicing extracts a subset of an array using the syntax arr[start:stop:step], where start is the starting index, stop is the ending index (exclusive), and step is the increment. Slicing works across all dimensions of an array.

**Accessing elements in 1D arrays**

```
print("\nAccessing elements in array1 (1D):")
print("First element:", array1[0])
print("Last element:", array1[-1])
print("Element at index 2:", array1[2])
```

**Slicing 1D arrays**

```
print("\nSlicing array1 (1D):")
print("First two elements:", array1[0:2]) # or simply array1[:2]
print("Elements from index 2 onwards:", array1[2:])
print("Last two elements:", array1[-2:])
print("Every other element:", array1[::2])
print("Reverse the array:", array1[::-1])
```

**Accessing elements in 2D arrays**

```
print("\nAccessing elements in array2 (2D):")
# To access an element in a 2D array, you provide the row and column indices.
# The syntax is `array[row_index, column_index]`.
print("Element at row 0, column 1:", array2[0, 1]) # This is the element '2'
print("Element at row 1, column 2:", array2[1, 2]) # This is the element '6'

# You can also use separate indices:
print("Element at row 0, column 1 (using separate indices):", array2[0][1]) # Same as array2[0, 1]
```

**Slicing 2D Arrays**

```
# Slicing in 2D allows you to select subsets of rows and columns.
# The syntax is `array[row_slice, column_slice]`.

# Select the first row:
print("First row:", array2[0, :]) # or array2[0]
print("First row (alternative):", array2[0])

# Select the second column:
print("Second column:", array2[:, 1])

# Select a sub-matrix (first row, first two columns):
print("First row, first two columns:\n", array2[0, 0:2]) # or array2[0, :2]

# Select a sub-matrix (first two rows, first two columns):
print("First two rows, first two columns:\n", array2[0:2, 0:2]) # or array2[:2, :2]

# Select elements from the second row onwards, and the second column onwards:
print("Second row onwards, second column onwards:\n", array2[1:, 1:])

# Select all rows, but reverse the order of columns:
print("All rows, reversed columns:\n", array2[:, ::-1])
```

**Accessing and Slicing arrays with more dimensions**

```
print("\nAccessing and Slicing array3 (3D):")
# Accessing elements requires an index for each dimension.
# The syntax is `array[dim1_index, dim2_index, dim3_index, ...]`.
# For array3 (shape (2, 2, 2)): (matrix index, row index, column index)
print("Element at index (0, 0, 1):", array3[0, 0, 1]) # This is the element '2'
print("Element at index (1, 1, 0):", array3[1, 1, 0]) # This is the element '7'

# Slicing works similarly, applying slices to each dimension.
# Select the first matrix (index 0 along the first dimension):
print("First matrix (slice along dim 0):\n", array3[0, :, :]) # or array3[0, ...] or array3[0]

# Select the first row from both matrices (slice along dim 1):
print("First row from both matrices (slice along dim 1):\n", array3[:, 0, :])

# Select the second column from the second matrix:
print("Second column from the second matrix (slice along dim 0 and dim 2):\n", array3[1, :, 1])
```

**Using Ellipsis (...) for convenient slicing**

```
print("\nUsing Ellipsis (...) for slicing:")
# The ellipsis `...` is a placeholder for a full set of slice notations `:, :, ..., :`
# For example, `array[..., 1]` means "select the second element along the last dimension, for all combinations of indices in the preceding dimensions".

# Get the second column of the last dimension for all matrices and rows in array3:
print("Second element along the last dimension in array3:\n", array3[..., 1])

# Get the first row for all matrices and columns in array3:
print("First row along the second dimension in array3:\n", array3[:, 0, ...]) # or array3[:, 0, :]

# In 2D arrays, `array[..., column_index]` is equivalent to `array[:, column_index]`.
print("Second column in array2 using ellipsis:", array2[..., 1])

# The ellipsis can appear in the middle as well.
# For a 4D array (array4, shape (2, 2, 2, 2)), `array4[0, ..., 1]` means:
# "Select the first element along the first dimension (matrix block),
# then take all elements along the intermediate dimensions (the two 2x2 matrices),
# and finally select the second element along the last dimension (the column within the innermost pairs)."
print("\nAccessing using ellipsis in array4:")
print("array4[0, ..., 1]:\n", array4[0, ..., 1])
# This is equivalent to array4[0, :, :, 1]
```

**Boolean Indexing (or Masking)**

```
print("\nBoolean Indexing:")
# You can use a boolean array of the same shape as the original array to select elements.
# Elements where the boolean array is True are selected, and elements where it's False are not.

print("Original array1:", array1)
# Select elements in array1 that are greater than 2:
boolean_mask_1d = array1 > 2
print("Boolean mask for array1 > 2:", boolean_mask_1d)
print("Elements in array1 greater than 2:", array1[boolean_mask_1d])

print("\nOriginal array2:\n", array2)
# Select elements in array2 that are even:
boolean_mask_2d = (array2 % 2 == 0)
print("Boolean mask for array2 even:\n", boolean_mask_2d)
print("Even elements in array2:", array2[boolean_mask_2d]) # Returns a 1D array
```

**Integer Array Indexing**

```
print("\nInteger Array Indexing:")
# You can use lists or arrays of integers to select elements at specific indices.

# Select elements at indices 0, 2, and 3 from array1:
indices_1d = [0, 2, 3]
print("Elements at indices [0, 2, 3] in array1:", array1[indices_1d])

# For 2D arrays, you can select specific rows or columns using integer arrays.
# Select rows at indices 1 and 0 from array2:
row_indices = [1, 0]
print("Rows at indices [1, 0] in array2:\n", array2[row_indices, :])

# Select columns at indices 2 and 0 from array2:
col_indices = [2, 0]
print("Columns at indices [2, 0] in array2:\n", array2[:, col_indices])

# You can also use integer arrays to select individual elements at specific (row, column) pairs.
# The shape of the index arrays determines the shape of the output.
# Select elements at (0, 1) and (1, 0) from array2:
row_indices = [0, 1]
col_indices = [1, 0]
print("Elements at (0, 1) and (1, 0) in array2:", array2[row_indices, col_indices]) # Returns a 1D array

# If you want to select elements based on a grid of indices, the index arrays should have the same shape.
# Let's say we want to select the elements at (0, 1), (0, 2), (1, 0), and (1, 1) from array2.
row_indices_grid = np.array([[0, 0], [1, 1]])
col_indices_grid = np.array([[1, 2], [0, 1]])
print("Elements at indices specified by grid:\n", array2[row_indices_grid, col_indices_grid]) # Returns a 2D array

# Understanding boolean and integer array indexing is crucial for powerful data manipulation with NumPy.

# These are the fundamental methods for accessing and slicing NumPy arrays. Mastering them is essential
# for efficiently working with numerical data in Python using NumPy.
```

**Views vs. Copies**
- Understanding whether an operation returns a view or a copy is critical for memory efficiency and avoiding unintended modifications.
- View: A slice of an array shares the same memory as the original array. Modifying the slice modifies the original array.
- Copy: A new array with independent memory is created. Modifying the copy does not affect the original array.

**Views and Copies**
```
arr = np.array([1, 2, 3, 4, 5])
slice_view = arr[1:4]  # View
slice_view[0] = 99
print(arr)  # Output: [1 99 3 4 5]  # Original array modified

# Using fancy indexing (creates a copy)
copy_arr = arr[[1, 2, 3]]
copy_arr[0] = 88
print(arr)  # Output: [1 99 3 4 5]  # Original array unchanged

# Explicit copy
explicit_copy = arr[1:4].copy()
explicit_copy[0] = 77
print(arr)  # Output: [1 99 3 4 5]  # Original array unchanged
```

**Key Points**

- Slicing (arr[start:stop:step]) returns a view.
- Fancy indexing and boolean indexing return copies.
- Use .copy() to explicitly create a copy when needed.

**Modifying Arrays Using Indexing and Slicing**

Indexing and slicing can be used to modify array elements by assigning new values to selected subsets.

**Modifying Arrays**
```
arr_1d = np.array([10, 20, 30, 40, 50])
arr_1d[2] = 99  # Modify single element
print(arr_1d)  # Output: [10 20 99 40 50]

arr_1d[1:4] = 0  # Modify slice
print(arr_1d)  # Output: [10  0  0  0 50]

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_2d[0, :] = [10, 20, 30]  # Modify first row
print(arr_2d)
# Output: [[10 20 30]
#          [ 4  5  6]
#          [ 7  8  9]]

# Boolean indexing for modification
arr_2d[arr_2d > 5] = 0
print(arr_2d)
# Output: [[0 0 0]
#          [4 5 0]
#          [0 0 0]]
```

**Key Points**
- Assignments to slices modify the original array (since slices are views).
- Ensure the assigned values are compatible with the shape and data type of the target slice.

**Practical Example: Data Analysis with Accessing/Slicing**

Let’s apply these techniques to a real-world data science scenario, such as filtering and modifying a dataset of temperatures.
```
# Temperature data (3 cities, 4 days)
temps = np.array([[25.1, 26.3, 24.8, 27.2],
                  [22.5, 23.7, 21.9, 24.0],
                  [28.4, 29.1, 27.8, 30.2]])

# Access temperature for city 1, day 2
print(temps[1, 2])  # Output: 21.9

# Slice temperatures for first two cities, last two days
print(temps[0:2, 2:4])
# Output: [[24.8 27.2]
#          [21.9 24.0]]

# Filter temperatures above 25°C
hot_temps = temps[temps > 25]
print(hot_temps)  # Output: [25.1 26.3 27.2 28.4 29.1 27.8 30.2]

# Increase temperatures for city 3 by 1°C
temps[2, :] += 1
print(temps)
# Output: [[25.1 26.3 24.8 27.2]
#          [22.5 23.7 21.9 24.0]
#          [29.4 30.1 28.8 31.2]]
```

**Common Pitfalls and Best Practices**

Shape Mismatch Errors: Ensure the shape of assigned values matches the slice or index target. For example, arr[0:2] = [1, 2, 3] will raise an error if arr[0:2] has a different shape.
Memory Management: Be cautious with views vs. copies to avoid unintended modifications or excessive memory usage. Use .copy() when a copy is needed.
Boolean Indexing Memory: Boolean indexing creates copies, which can be memory-intensive for large arrays. Use slicing where possible for views.
Advanced Indexing Order: In fancy indexing, the order of indices matters (e.g., arr[[0, 1], [0, 1]] picks specific elements, not a subarray).

**Conclusion**
Accessing and slicing NumPy arrays are fundamental skills for efficient data manipulation in data science and numerical computing. By leveraging integer indexing, slicing, boolean indexing, and fancy indexing, you can extract and modify specific elements or subsets of arrays with precision. Understanding the distinction between views and copies ensures memory-efficient operations, while mastering these techniques enables seamless integration with data science workflows, such as data preprocessing, filtering, or analysis. With practice, these methods become intuitive, empowering you to handle complex datasets and build robust applications.

**Exercises**

- Create a 3x4 NumPy array and extract the second column using slicing.
- Use boolean indexing to find all elements greater than the mean in a 1D array.
- Modify a 2D array’s diagonal elements using fancy indexing.
- Create a copy of a slice from a 3D array and verify it does not modify the original.

