# Lesson 5 Handling Missing Data

**Handling Missing Data using NumPy** is a critical skill when working with real-world datasets, where incomplete or missing values are common. In NumPy, missing data is typically represented using the special floating-point value `NaN` (Not a Number), which acts as a placeholder for undefined or unrepresentable values. This allows arrays to maintain their structure and dimensionality even when some entries are unknown or unavailable. NumPy provides several tools to detect, filter, and manage missing values efficiently. For instance, the function `np.isnan()` can be used to identify positions of missing values within an array, returning a boolean mask that highlights where data is absent. Users can then use this mask to either remove missing values or replace them with appropriate substitutes such as the mean, median, or a constant value using functions like `np.nanmean()` or `np.where()`. Additionally, NumPy offers versions of common mathematical operations—such as `np.nanmean()`, `np.nanstd()`, and `np.nansum()`—that automatically skip over `NaN` values during computation, ensuring accurate results without requiring prior data cleaning. While NumPy does not support as extensive missing data handling capabilities as Pandas, its foundational tools provide a robust starting point for preprocessing numerical arrays before further analysis or modeling. Properly addressing missing data is essential for maintaining data integrity and avoiding skewed or incorrect conclusions in scientific computing and data science workflows.

**Handling Missing Data using NumPy**

- Missing data is a common problem in real-world datasets.
- In NumPy, missing values are typically represented by `NaN` (Not a Number).
- `NaN` is a special floating-point value.

**Creating arrays with missing values**
```
# You can explicitly include NaN using np.nan
data_with_nan = np.array([1, 2, np.nan, 4, 5])
print("\n--- Handling Missing Data ---")
print("\nArray with NaN:", data_with_nan)
```

**NaN missing values**
```
# Many functions in NumPy will produce NaN if there are missing values
# For example, calculating the mean of an array with NaN
mean_with_nan = np.mean(data_with_nan)
print("Mean of array with NaN:", mean_with_nan)
# The mean is NaN because standard arithmetic operations involving NaN result in NaN.
```

**Identifying Missing Values**
```
# Use np.isnan() to create a boolean mask indicating where NaN values are
nan_mask = np.isnan(data_with_nan)
print("Boolean mask for NaN:", nan_mask)
```

**Counting Missing Values**
```
# You can sum the boolean mask to count the number of True values (NaNs)
num_nan = np.sum(nan_mask)
print("Number of NaN values:", num_nan)

# You can also count non-missing values
num_non_nan = np.sum(~nan_mask) # Use the tilde (~) for logical NOT
print("Number of non-NaN values:", num_non_nan)
```

**Handling Missing Values**

**Method 1:** Removing rows/elements with missing values

```
# For a 1D array, you can use the boolean mask to select non-NaN elements
data_cleaned = data_with_nan[~nan_mask]
print("\nArray after removing NaN:", data_cleaned)

# For a 2D array, removing rows with any NaN requires more care.
# Let's create a 2D array with NaNs
data_2d_with_nan = np.array([
    [1, 2, 3],
    [4, np.nan, 6],
    [7, 8, np.nan],
    [9, 10, 11]
])
print("\nOriginal 2D array with NaN:\n", data_2d_with_nan)

# To identify rows with any NaN:
# np.isnan(data_2d_with_nan) gives a boolean array of the same shape.
# np.any(axis=1) checks if *any* element in each row (axis=1) is True (is NaN).
row_has_nan_mask = np.isnan(data_2d_with_nan).any(axis=1)
print("Boolean mask indicating rows with NaN:", row_has_nan_mask)

# To keep rows that *do not* have any NaN:
data_2d_cleaned = data_2d_with_nan[~row_has_nan_mask]
print("2D array after removing rows with NaN:\n", data_2d_cleaned)
```

**Method 2:** Imputing Missing Values (Replacing NaN)

```
# Replacing NaN with a specific value (e.g., 0, mean, median)

# Replacing NaN with 0
data_filled_zero = np.nan_to_num(data_with_nan, nan=0)
print("\nArray after filling NaN with 0:", data_filled_zero)

# Replacing NaN with the mean of the non-missing values
# First, calculate the mean ignoring NaN values
mean_ignoring_nan = np.nanmean(data_with_nan)
print("Mean ignoring NaN:", mean_ignoring_nan)

# Create a copy to avoid modifying the original array
data_filled_mean = np.copy(data_with_nan)
# Use the boolean mask to select NaN positions and assign the mean
data_filled_mean[nan_mask] = mean_ignoring_nan
print("Array after filling NaN with mean:", data_filled_mean)

# For 2D arrays, you might want to impute based on column means or row means.
# Imputing NaNs with the mean of each column:
# Calculate the mean of each column, ignoring NaNs. np.nanmean with axis=0.
column_means = np.nanmean(data_2d_with_nan, axis=0)
print("Column means ignoring NaN:", column_means)

# Create a copy
data_2d_filled_col_mean = np.copy(data_2d_with_nan)

# Find where NaNs are in the 2D array
nan_2d_mask = np.isnan(data_2d_with_nan)

# Iterate through columns and fill NaNs
# A more efficient way might involve advanced indexing or broadcasting,
# but a loop is clearer for demonstration here.
for i in range(data_2d_filled_col_mean.shape[1]):
    data_2d_filled_col_mean[nan_2d_mask[:, i], i] = column_means[i]

print("2D array after filling NaNs with column means:\n", data_2d_filled_col_mean)


# NumPy functions that handle NaNs
# NumPy provides specialized functions that operate while ignoring NaN values.
# These functions typically start with 'nan'.

# np.nansum(): Calculate the sum of array elements ignoring NaN.
print("\nSum ignoring NaN:", np.nansum(data_with_nan))

# np.nanmean(): Calculate the mean of array elements ignoring NaN.
print("Mean ignoring NaN:", np.nanmean(data_with_nan))

# np.nanmedian(): Calculate the median of array elements ignoring NaN.
print("Median ignoring NaN:", np.nanmedian(data_with_nan))

# np.nanmax(): Find the maximum value ignoring NaN.
print("Maximum ignoring NaN:", np.nanmax(data_with_nan))

# np.nanmin(): Find the minimum value ignoring NaN.
print("Minimum ignoring NaN:", np.nanmin(data_with_nan))

# np.nanstd(): Calculate the standard deviation ignoring NaN.
print("Standard deviation ignoring NaN:", np.nanstd(data_with_nan))

# np.nanvar(): Calculate the variance ignoring NaN.
print("Variance ignoring NaN:", np.nanvar(data_with_nan))

# These 'nan' functions are very useful when you need to perform calculations
# on arrays that might contain missing values without having to explicitly
# remove or impute them beforehand for that specific calculation.

# Important Note:
# - `NaN` is a float. If your array has an integer `dtype`, NumPy cannot
#   directly represent `NaN`. When you introduce `np.nan` into an integer array,
#   NumPy will automatically cast the array to a float `dtype` to accommodate `NaN`.

int_array = np.array([1, 2, 3])
print("\nOriginal integer array dtype:", int_array.dtype)
int_array_with_nan = np.array([1, 2, np.nan, 3])
print("Array with NaN added dtype:", int_array_with_nan.dtype)

# In summary, NumPy provides robust tools for identifying, counting,
# and handling missing data represented as `NaN`. You can choose to
# remove rows/elements with missing values or impute them using
# appropriate strategies (like filling with mean, median, or a constant).
# Additionally, NumPy's 'nan' functions simplify calculations on arrays
# containing missing data.
```


