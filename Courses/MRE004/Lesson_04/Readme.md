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

**Slicing 1D Arrays**

```
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d[1:4])  # Output: [20 30 40]  # Elements from index 1 to 3
print(arr_1d[::2])  # Output: [10 30 50]  # Every second element
print(arr_1d[-3:])  # Output: [30 40 50]  # Last three elements
```

**Slicing 2D Arrays**
```
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[0:2, 1:3])  # Output: [[2 3] [5 6]]  # Rows 0-1, columns 1-2
print(arr_2d[:, 1])      # Output: [2 5 8]       # All rows, column 1
print(arr_2d[1, :])      # Output: [4 5 6]       # Row 1, all columns
```

**Key Points**
- Use ```:``` to select all elements along a dimension (e.g., arr[:, 0] for the first column).
- Omitting start defaults to 0, omitting stop defaults to the end, and omitting step defaults to 1.
- Negative indices and steps are supported (e.g., [::-1] reverses the array).

**Boolean Indexing**
Boolean indexing uses a boolean array of the same shape as the target array (or compatible shape via broadcasting) to select elements where the condition is True. This is particularly useful for filtering data based on conditions.

**Boolean Indexing**
```
arr_1d = np.array([10, 20, 30, 40, 50])
mask = arr_1d > 25
print(mask)         # Output: [False False  True  True  True]
print(arr_1d[mask]) # Output: [30 40 50]  # Elements where mask is True

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[arr_2d % 2 == 0])  # Output: [2 4 6 8]  # Even elements
```

**Key Points**

- Boolean arrays are created using comparison operators (e.g., >, <, ==).
- The result is a 1D array of elements where the condition is True.
- Combine conditions using & (and), | (or), and ~ (not) for complex filters.

**Fancy Indexing**

Fancy indexing allows you to access elements using lists or arrays of indices, enabling non-contiguous or repeated selections. This is more flexible than slicing but may return a copy instead of a view.

```
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d[[0, 2, 4]])  # Output: [10 30 50]  # Elements at indices 0, 2, 4

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[[0, 2], [1, 2]])  # Output: [2 9]  # Elements at (0,1) and (2,2)
print(arr_2d[[0, 1], :])       # Output: [[1 2 3] [4 5 6]]  # Rows 0 and 1
```

**Key Points**

- Pass lists or NumPy arrays of indices for each dimension.
- Fancy indexing can select elements in any order or multiple times.
- Unlike slicing, fancy indexing typically creates a copy of the data.

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

