# Lesson 1 NumPy Arrays
NumPy arrays, the backbone of numerical computing in Python, are powerful, multidimensional data structures provided by the NumPy library, designed for efficient storage and manipulation of large datasets. Unlike Python lists, NumPy arrays (`ndarray`) support element-wise operations, broadcasting, and advanced mathematical functions, making them ideal for tasks in data analysis, scientific computing, and machine learning. They offer attributes like `shape`, `dtype`, and `ndim` for easy metadata access and can be created from lists, built-in functions like `np.zeros` or `np.arange`, or random generators. With their ability to handle complex operations on entire arrays without loops, NumPy arrays provide a fast, flexible, and intuitive way to process numerical data.

**How to Import NumPy**
```
import numpy as np
```
## Introduction
NumPy is the cornerstone of numerical computing in Python, providing a powerful array object that enables efficient storage and manipulation of large datasets. In this lesson, we'll explore how to create NumPy arrays, perform operations on them, and leverage broadcasting to simplify computations. Through detailed explanations and practical examples, you'll gain a solid understanding of these core concepts.

### 1. Creating NumPy Arrays
NumPy arrays, or ndarray, are multidimensional containers for elements of the same data type. They are more efficient than Python lists for numerical operations due to their fixed size and optimized memory usage.

#### 1.1. From Python Lists
You can create a NumPy array from a Python list or tuple using np.array().
import numpy as np

**Create a 1D array**
```
list1 = [1, 2, 3, 4]
array1 = np.array(list1)
print("1D Array:", array1)
```
**Create a 2D array**
```
list2 = [[1, 2, 3], [4, 5, 6]]
array2 = np.array(list2)
print("2D Array:\n", array2)
```
**Output:**
1D Array: [1 2 3 4]
2D Array:
 [[1 2 3]
  [4 5 6]]

#### 1.2. Using Built-in Functions
NumPy provides functions to create arrays with specific values or patterns:

np.zeros(shape): Creates an array filled with zeros.
np.ones(shape): Creates an array filled with ones.
np.arange(start, stop, step): Creates an array with a range of values.
np.linspace(start, stop, num): Creates an array with evenly spaced values.
np.random.rand(shape): Creates an array with random values between 0 and 1.

**Zeros and ones**
```
zeros_array = np.zeros((2, 3))
ones_array = np.ones((3, 2))
```
**Range and linspace**
```
range_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)
```
**Random array**
```
random_array = np.random.rand(2, 2)
print("Zeros:\n", zeros_array)
print("Ones:\n", ones_array)
print("Range:", range_array)
print("Linspace:", linspace_array)
print("Random:\n", random_array)
```
**Output:**
Zeros:
 [[0. 0. 0.]
  [0. 0. 0.]]
Ones:
 [[1. 1.]
  [1. 1.]
  [1. 1.]]
Range: [0 2 4 6 8]
Linspace: [0.   0.25 0.5  0.75 1.  ]
Random:
 [[0.12345678 0.98765432]
  [0.45678901 0.23456789]]

1.3. Array Attributes
NumPy arrays have attributes that provide metadata:

shape: Dimensions of the array.
dtype: Data type of the array elements.
ndim: Number of dimensions.
size: Total number of elements.

array = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape:", array.shape)
print("Data type:", array.dtype)
print("Dimensions:", array.ndim)
print("Size:", array.size)

Output:
Shape: (2, 3)
Data type: int64
Dimensions: 2
Size: 6

### 2. Array Operations
NumPy supports element-wise operations, mathematical functions, and matrix operations, making it ideal for numerical tasks.

#### 2.1. Element-wise Operations
You can perform arithmetic operations directly on arrays, which are applied element-wise.

**Create two arrays**
```
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```
**Arithmetic operations**
```
sum_array = a + b
diff_array = a - b
prod_array = a * b
div_array = a / b

print("Sum:", sum_array)
print("Difference:", diff_array)
print("Product:", prod_array)
print("Division:", div_array)
```
**Output:**
Sum: [5 7 9]
Difference: [-3 -3 -3]
Product: [ 4 10 18]
Division: [0.25 0.4  0.5 ]

#### 2.2. Mathematical Functions
NumPy provides universal functions (ufuncs) for mathematical operations like sin, cos, exp, and sqrt.

**Apply mathematical functions**
```
angles = np.array([0, np.pi/2, np.pi])
sin_values = np.sin(angles)
sqrt_values = np.sqrt(a)

print("Sine:", sin_values)
print("Square root:", sqrt_values)
```
**Output:**
```
Sine: [0.0000000e+00 1.0000000e+00 1.2246468e-16]
Square root: [1.         1.41421356 1.73205081]
```
#### 2.3. Matrix Operations
For matrix operations, use np.dot() for dot products or @ for matrix multiplication.

**Matrix multiplication**
```
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(A, B)
# or: matrix_product = A @ B

print("Matrix Product:\n", matrix_product)
```
**Output:**
Matrix Product:
 [[19 22]
  [43 50]]

### 3. Broadcasting
Broadcasting allows NumPy to perform operations on arrays of different shapes by automatically expanding their dimensions to be compatible.

#### 3.1. Broadcasting Rules

- Arrays with fewer dimensions are padded with ones on the left.
- Arrays with different shapes are compatible if their dimensions are either equal or one of them is 1.
- The smaller array is "stretched" to match the larger array's shape.

#### 3.2. Example: Scalar and Array
Adding a scalar to an array broadcasts the scalar to every element.

**Scalar broadcasting**
```
array = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
result = array + scalar

print("Array + Scalar:\n", result)
```
**Output:**
Array + Scalar:
 [[11 12 13]
  [14 15 16]]

#### 3.3. Example: Different Shapes
You can add a 1D array to a 2D array if their shapes are compatible.

**Broadcasting with different shapes**
```
A = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
B = np.array([10, 20, 30])           # Shape: (3,)
result = A + B

print("Broadcasting Result:\n", result)
```
**Output:**
Broadcasting Result:
 [[11 22 33]
  [14 25 36]]

Here, B is broadcasted to match A's shape by replicating [10, 20, 30] across both rows.

#### 3.4. Advanced Broadcasting
You can reshape arrays to make them compatible for broadcasting.

**Advanced broadcasting**
```
A = np.array([[1], [2], [3]])  # Shape: (3, 1)
B = np.array([10, 20, 30])     # Shape: (3,)
result = A + B

print("Advanced Broadcasting:\n", result)
```
**Output:**
Advanced Broadcasting:
 [[11 21 31]
  [12 22 32]
  [13 23 33]]

B is broadcasted across columns, and A is broadcasted across rows, resulting in a (3, 3) array.

### 4. Practical Example: Image Processing
Let’s apply these concepts to a simple image processing task. Suppose you have a grayscale image represented as a 2D array, and you want to adjust its brightness by adding a value and normalizing it.

**Simulate a grayscale image (values between 0 and 255)**
```
image = np.random.randint(0, 256, size=(4, 4))
print("Original Image:\n", image)
```
**Increase brightness by 50 (broadcasting)**
```
bright_image = image + 50
```
**Clip values to stay within [0, 255]**
```
bright_image = np.clip(bright_image, 0, 255)
```
**Normalize to [0, 1]**
```
normalized_image = bright_image / 255.0

print("Brightened Image:\n", bright_image)
print("Normalized Image:\n", normalized_image)
```
**Output (example, random values vary):**
Original Image:
 [[100 150 200 50]
  [75  125 175 25]
  [200 100 50  150]
  [25  75  125 200]]
Brightened Image:
 [[150 200 250 100]
  [125 175 225 75]
  [250 150 100 200]
  [75  125 175 250]]
Normalized Image:
 [[0.58823529 0.78431373 0.98039216 0.39215686]
  [0.49019608 0.68627451 0.88235294 0.29411765]
  [0.98039216 0.58823529 0.39215686 0.78431373]
  [0.29411765 0.49019608 0.68627451 0.98039216]]

## Conclusion
In this lesson, you’ve learned how to create NumPy arrays, perform element-wise and matrix operations, and utilize broadcasting to simplify computations. These skills are fundamental for numerical computing tasks in data science, machine learning, and scientific research. Practice these concepts with real-world datasets to deepen your understanding!

## Exercises
- Create a 3x3 array of random integers between 1 and 10, then multiply it element-wise by 5.
- Use broadcasting to subtract the mean of each row from a 4x4 random array.
- Compute the dot product of two 2x2 arrays and verify the result manually.
