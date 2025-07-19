# TensorFlow learning basics 
TensorFlow is a powerful library for numerical computation, particularly for machine learning, and these terms are foundational for understanding how data is represented and manipulated in it. I'll provide concise explanations and examples, focusing on clarity for someone new to TensorFlow.

### 1. **Tensor**
**Definition**: A tensor is a generalization of scalars, vectors, and matrices to higher dimensions. It’s the fundamental data structure in TensorFlow, representing multi-dimensional arrays of numerical data.

**Example**:
```python
import tensorflow as tf

# Scalar (0D tensor)
scalar = tf.constant(5)
# Vector (1D tensor)
vector = tf.constant([1, 2, 3])
# Matrix (2D tensor)
matrix = tf.constant([[1, 2], [3, 4]])
# 3D tensor
tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Scalar:", scalar)
print("Vector:", vector)
print("Matrix:", matrix)
print("3D Tensor:", tensor_3d)
```
**Output** (simplified):
```
Scalar: tf.Tensor(5, shape=(), dtype=int32)
Vector: tf.Tensor([1 2 3], shape=(3,), dtype=int32)
Matrix: tf.Tensor([[1 2] [3 4]], shape=(2, 2), dtype=int32)
3D Tensor: tf.Tensor([[[1 2] [3 4]] [[5 6] [7 8]]], shape=(2, 2, 2), dtype=int32)
```
**Explanation**: Tensors can have any number of dimensions, from scalars (0D) to n-dimensional arrays, and are used to store data like inputs, weights, or outputs in TensorFlow.

---

### 2. **Tensor Shape**
**Definition**: The shape of a tensor describes the number of elements in each dimension. It’s represented as a tuple, where each value indicates the size of that dimension.

**Example**:
```python
# Define tensors
scalar = tf.constant(5)  # Shape: ()
vector = tf.constant([1, 2, 3])  # Shape: (3,)
matrix = tf.constant([[1, 2], [3, 4]])  # Shape: (2, 2)
tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Shape: (2, 2, 2)

print("Scalar shape:", scalar.shape)
print("Vector shape:", vector.shape)
print("Matrix shape:", matrix.shape)
print("3D Tensor shape:", tensor_3d.shape)
```
**Output**:
```
Scalar shape: ()
Vector shape: (3,)
Matrix shape: (2, 2)
3D Tensor shape: (2, 2, 2)
```
**Explanation**: The shape tells us how the tensor is structured. A scalar has an empty shape, a vector has one dimension, a matrix has two, and so on.

---

### 3. **Three-Channel Color Image**
**Definition**: A three-channel color image is a tensor representing an image with three color channels (typically Red, Green, Blue - RGB). It’s usually a 3D tensor with shape `(height, width, channels)`, where channels = 3 for RGB.

**Example**:
```python
# Simulate a 2x2 RGB image (height=2, width=2, channels=3)
image = tf.constant([
    [[255, 0, 0], [0, 255, 0]],  # First row: Red, Green
    [[0, 0, 255], [255, 255, 255]]  # Second row: Blue, White
], dtype=tf.uint8)

print("Image tensor:", image)
print("Shape:", image.shape)
```
**Output**:
```
Image tensor: tf.Tensor(
[[[255   0   0] [  0 255   0]]
 [[  0   0 255] [255 255 255]]], shape=(2, 2, 3), dtype=uint8)
Shape: (2, 2, 3)
```
**Explanation**: Each pixel has three values (RGB), and the tensor’s shape reflects the image’s height, width, and number of channels (3 for RGB).

---

### 4. **Dimensions**
**Definition**: Dimensions refer to the number of axes (or ranks) of a tensor, which is the length of its shape tuple. A scalar has 0 dimensions, a vector has 1, a matrix has 2, and so on.

**Example**:
```python
# Tensors with different dimensions
scalar = tf.constant(5)  # 0D
vector = tf.constant([1, 2, 3])  # 1D
matrix = tf.constant([[1, 2], [3, 4]])  # 2D
tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D

print("Scalar dimensions:", tf.rank(scalar))
print("Vector dimensions:", tf.rank(vector))
print("Matrix dimensions:", tf.rank(matrix))
print("3D Tensor dimensions:", tf.rank(tensor_3d))
```
**Output**:
```
Scalar dimensions: tf.Tensor(0, shape=(), dtype=int32)
Vector dimensions: tf.Tensor(1, shape=(), dtype=int32)
Matrix dimensions: tf.Tensor(2, shape=(), dtype=int32)
3D Tensor dimensions: tf.Tensor(3, shape=(), dtype=int32)
```
**Explanation**: The number of dimensions (rank) corresponds to how many indices are needed to access an element in the tensor.

---

### 5. **Permutation**
**Definition**: Permutation (or transpose in a general sense) involves rearranging the dimensions of a tensor according to a specified order. In TensorFlow, `tf.transpose` is used, often with a permutation list to reorder axes.

**Example**:
```python
# 3D tensor
tensor = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Shape: (2, 2, 2)
permuted = tf.transpose(tensor, perm=[1, 0, 2])  # Swap first two axes

print("Original tensor:", tensor)
print("Permuted tensor:", permuted)
print("Original shape:", tensor.shape)
print("Permuted shape:", permuted.shape)
```
**Output** (simplified):
```
Original tensor: tf.Tensor([[[1 2] [3 4]] [[5 6] [7 8]]], shape=(2, 2, 2), dtype=int32)
Permuted tensor: tf.Tensor([[[1 2] [5 6]] [[3 4] [7 8]]], shape=(2, 2, 2), dtype=int32)
Original shape: (2, 2, 2)
Permuted shape: (2, 2, 2)
```
**Explanation**: The permutation `[1, 0, 2]` swaps the first (0) and second (1) axes, keeping the third (2) unchanged, rearranging the tensor’s structure.

---

### 6. **Conjugate**
**Definition**: The conjugate of a tensor applies the complex conjugate operation to its elements (for complex numbers, `a + bi` becomes `a - bi`). For real-valued tensors, the conjugate is the same as the original tensor.

**Example**:
```python
# Complex-valued tensor
complex_tensor = tf.constant([[1+2j, 3+4j], [5+6j, 7+8j]], dtype=tf.complex64)
conjugate_tensor = tf.math.conj(complex_tensor)

print("Original:", complex_tensor)
print("Conjugate:", conjugate_tensor)
```
**Output**:
```
Original: tf.Tensor([[1.+2.j 3.+4.j] [5.+6.j 7.+8.j]], shape=(2, 2), dtype=complex64)
Conjugate: tf.Tensor([[1.-2.j 3.-4.j] [5.-6.j 7.-8.j]], shape=(2, 2), dtype=complex64)
```
**Explanation**: The imaginary parts of the complex numbers are negated, while the real parts remain unchanged.

---

### 7. **Transpose**
**Definition**: Transpose swaps the rows and columns of a matrix (or specific axes of a higher-dimensional tensor). For a 2D matrix, it flips elements across the main diagonal. For higher dimensions, you specify which axes to swap.

**Example**:
```python
# 2D matrix
matrix = tf.constant([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
transposed = tf.transpose(matrix)  # Default swaps rows and columns

print("Original:", matrix)
print("Transposed:", transposed)
print("Original shape:", matrix.shape)
print("Transposed shape:", transposed.shape)
```
**Output**:
```
Original: tf.Tensor([[1 2 3] [4 5 6]], shape=(2, 3), dtype=int32)
Transposed: tf.Tensor([[1 4] [2 5] [3 6]], shape=(3, 2), dtype=int32)
Original shape: (2, 3)
Transposed shape: (3, 2)
```
**Explanation**: Rows become columns, and the shape changes from `(2, 3)` to `(3, 2)`.

---

### 8. **Broadcast (broadcast_to)**
**Definition**: Broadcasting allows operations on tensors of different shapes by automatically expanding smaller tensors to match the shape of larger ones. `tf.broadcast_to` explicitly expands a tensor to a specified shape.

**Example**:
```python
# Scalar to vector
scalar = tf.constant(5)
broadcasted = tf.broadcast_to(scalar, [3, 2])

print("Original scalar:", scalar)
print("Broadcasted tensor:", broadcasted)
print("Broadcasted shape:", broadcasted.shape)
```
**Output**:
```
Original scalar: tf.Tensor(5, shape=(), dtype=int32)
Broadcasted tensor: tf.Tensor([[5 5] [5 5] [5 5]], shape=(3, 2), dtype=int32)
Broadcasted shape: (3, 2)
```
**Explanation**: The scalar `5` is expanded to fill a `(3, 2)` tensor, enabling operations with other tensors of that shape.

---

### 9. **Matrix**
**Definition**: A matrix is a 2D tensor with rows and columns, often used for linear algebra operations like matrix multiplication.

**Example**:
```python
# 2x2 matrix
matrix_a = tf.constant([[1, 2], [3, 4]])
matrix_b = tf.constant([[5, 6], [7, 8]])
# Matrix multiplication
result = tf.matmul(matrix_a, matrix_b)

print("Matrix A:", matrix_a)
print("Matrix B:", matrix_b)
print("A * B:", result)
```
**Output**:
```
Matrix A: tf.Tensor([[1 2] [3 4]], shape=(2, 2), dtype=int32)
Matrix B: tf.Tensor([[5 6] [7 8]], shape=(2, 2), dtype=int32)
A * B: tf.Tensor([[19 22] [43 50]], shape=(2, 2), dtype=int32)
```
**Explanation**: Matrices are used for transformations, such as in neural network layers, where weights are often represented as matrices.

---

### 10. **Splitting**
**Definition**: Splitting divides a tensor into multiple smaller tensors along a specified axis. `tf.split` is commonly used, specifying the number of splits or split sizes.

**Example**:
```python
# 2D tensor
tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8]])  # Shape: (2, 4)
split_tensors = tf.split(tensor, num_or_size_splits=2, axis=1)  # Split along axis 1

print("Original tensor:", tensor)
print("Split tensors:", split_tensors)
```
**Output** (simplified):
```
Original tensor: tf.Tensor([[1 2 3 4] [5 6 7 8]], shape=(2, 4), dtype=int32)
Split tensors: [
    tf.Tensor([[1 2] [5 6]], shape=(2, 2), dtype=int32),
    tf.Tensor([[3 4] [7 8]], shape=(2, 2), dtype=int32)
]
```
**Explanation**: The tensor is split into two tensors along axis 1 (columns), each with shape `(2, 2)`.

---

### 11. **Indices**
**Definition**: Indices are used to access or manipulate specific elements of a tensor. In TensorFlow, operations like `tf.gather` or indexing use indices to select elements or subtensors.

**Example**:
```python
# 1D tensor
tensor = tf.constant([10, 20, 30, 40, 50])
indices = tf.constant([0, 2, 4])  # Select elements at these indices
selected = tf.gather(tensor, indices)

print("Original tensor:", tensor)
print("Selected elements:", selected)
```
**Output**:
```
Original tensor: tf.Tensor([10 20 30 40 50], shape=(5,), dtype=int32)
Selected elements: tf.Tensor([10 30 50], shape=(3,), dtype=int32)
```
**Explanation**: The indices `[0, 2, 4]` select the 1st, 3rd, and 5th elements of the tensor.

---

### Summary
These terms form the backbone of TensorFlow’s data manipulation capabilities. Tensors are the core data structure, with shapes and dimensions defining their structure. Operations like permutation, transpose, and splitting allow reshaping and reorganizing tensors, while broadcasting enables flexible computations. Matrices are key for linear algebra, and indices help access specific data. Three-channel images illustrate real-world tensor applications, and conjugates handle complex numbers. Together, these concepts enable building and training machine learning models in TensorFlow.
