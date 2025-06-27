# Lesson 3 Working with Arrays in NumPy

is foundational to data manipulation and numerical computing in Python. NumPy, short for Numerical Python, provides a powerful `ndarray` object that allows efficient storage and operations on large datasets. Arrays in NumPy are homogeneous, meaning all elements must be of the same data type, which enables faster computations compared to standard Python lists. Understanding array attributes such as `.shape`, `.dtype`, `.ndim`, and `.size` helps in inspecting and managing array structure effectively. Accessing and slicing arrays—whether one-dimensional or multi-dimensional—is done using intuitive indexing syntax similar to Python lists but extended for multiple dimensions, allowing users to extract specific rows, columns, or sub-arrays with ease. Handling missing data is another crucial aspect when working with real-world datasets, and NumPy supports this through special values like `np.nan` (Not a Number). Functions such as `np.isnan()` help detect missing values, while others like `np.nanmean()` or `np.nansum()` allow for safe computations by ignoring NaNs. Together, these features make NumPy an essential tool for scientific computing, data analysis, and machine learning workflows.


**Array Attributes**
**1. shape:** This attribute returns a tuple representing the dimensions of the array.
```
# The shape indicates the number of elements along each dimension.
print("\n--- Array Attributes ---")
print("Shape of array1 (1D):", array1.shape)
print("Shape of array2 (2D):", array2.shape)
print("Shape of array3 (3D):", array3.shape)
print("Shape of array4 (4D):", array4.shape)

# For a 1D array, the shape is a tuple with one element, which is the number of elements in the array.
# For a 2D array (a matrix), the shape is a tuple (rows, columns).
# For higher dimensions, the tuple contains the size of each dimension.
```

**2. ndim:** This attribute returns an integer representing the number of dimensions of the array.
```
print("\nNumber of dimensions of array1 (1D):", array1.ndim)
print("Number of dimensions of array2 (2D):", array2.ndim)
print("Number of dimensions of array3 (3D):", array3.ndim)
print("Number of dimensions of array4 (4D):", array4.ndim)

# This is equivalent to the length of the `shape` tuple.
```

**3. size:** This attribute returns the total number of elements in the array.
```
# This is the product of the elements in the `shape` tuple.

print("\nTotal number of elements in array1 (1D):", array1.size)
print("Total number of elements in array2 (2D):", array2.size)
print("Total number of elements in array3 (3D):", array3.size)
print("Total number of elements in array4 (4D):", array4.size)
```

**4. dtype:** This attribute returns the data type of the elements in the array.
```
# NumPy tries to infer the data type when creating an array, or you can specify it.

print("\nData type of elements in array1:", array1.dtype)
print("Data type of elements in array2:", array2.dtype)

# Common data types include:
# int64: 64-bit integer
# float64: 64-bit floating-point number
# bool: Boolean values (True/False)
# object: Python objects (less efficient)
```

**5. nbytes:** This attribute returns the total number of bytes consumed by the elements of the array.
```
# This does not include the overhead for the array object itself, only the data.

print("\nNumber of bytes for data in array1:", array1.nbytes)
print("Number of bytes for data in array2:", array2.nbytes)

# This is calculated as `size * itemsize`.
```

**6. itemsize:** This attribute returns the size in bytes of each element in the array.
```
print("\nSize in bytes of each element in array1:", array1.itemsize)
print("Size in bytes of each element in array2:", array2.itemsize)

# The `itemsize` depends on the `dtype`. For example, `int64` uses 8 bytes.

# These attributes are fundamental for understanding and working with NumPy arrays,
# allowing you to inspect their structure, size, and data type.
```


