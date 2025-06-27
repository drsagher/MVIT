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


