# Lesson 7 Aggregating Functions

Aggregating Functions in NumPy are essential tools for summarizing and analyzing data efficiently. These functions perform computations across entire arrays or along specified axes to return single or reduced-size output values that represent key statistical or mathematical properties of the data. Common aggregating functions include `np.sum()`, `np.mean()`, `np.median()`, `np.std()`, `np.var()`, `np.min()`, and `np.max()`, which allow users to quickly calculate totals, averages, measures of spread, and extreme values within datasets. NumPy also provides specialized versions like `np.nanmean()` and `np.nansum()` that safely ignore missing values (`NaN`) during computation—ensuring accuracy when working with incomplete data. Aggregation can be applied to arrays of any dimensionality, with the optional `axis` parameter allowing users to control whether calculations are performed row-wise, column-wise, or across the entire array. By leveraging these aggregation functions, data analysts and scientists can extract meaningful insights from large numerical arrays with minimal code, making NumPy a powerful foundation for data processing and analysis workflows.

- Aggregating functions perform operations on an array and return a single value or a smaller array.
- Common aggregations include sum, mean, standard deviation, minimum, maximum, etc.

**Let's use a sample array**
```
agg_array = np.arange(1, 10).reshape(3, 3)
print("\nSample array for aggregation:\n", agg_array)
```

## 1. Sum

```
# np.sum(array) calculates the sum of all elements in the array.
total_sum = np.sum(agg_array)
print("\nSum of all elements:", total_sum)

# You can aggregate along a specific axis.
# axis=0 means sum along the columns (collapse the rows). The result will have the number of columns.
column_sums = np.sum(agg_array, axis=0)
print("Sum along columns (axis=0):", column_sums)

# axis=1 means sum along the rows (collapse the columns). The result will have the number of rows.
row_sums = np.sum(agg_array, axis=1)
print("Sum along rows (axis=1):", row_sums)
```

## 2. Mean

```
# np.mean(array) calculates the mean of all elements.
total_mean = np.mean(agg_array)
print("\nMean of all elements:", total_mean)

# Mean along axes
column_means = np.mean(agg_array, axis=0)
print("Mean along columns (axis=0):", column_means)
row_means = np.mean(agg_array, axis=1)
print("Mean along rows (axis=1):", row_means)
```

## 3. Standard Deviation

```
# np.std(array) calculates the standard deviation of all elements.
total_std = np.std(agg_array)
print("\nStandard deviation of all elements:", total_std)

# Standard deviation along axes
column_stds = np.std(agg_array, axis=0)
print("Standard deviation along columns (axis=0):", column_stds)
row_stds = np.std(agg_array, axis=1)
print("Standard deviation along rows (axis=1):", row_stds)
```

## 4. Variance

```
# np.var(array) calculates the variance of all elements.
total_var = np.var(agg_array)
print("\nVariance of all elements:", total_var)

# Variance along axes
column_vars = np.var(agg_array, axis=0)
print("Variance along columns (axis=0):", column_vars)
row_vars = np.var(agg_array, axis=1)
print("Variance along rows (axis=1):", row_vars)
```

## 5. Minimum

```
# np.min(array) finds the minimum value in the array.
total_min = np.min(agg_array)
print("\nMinimum element:", total_min)

# Minimum along axes
column_mins = np.min(agg_array, axis=0)
print("Minimum along columns (axis=0):", column_mins)
row_mins = np.min(agg_array, axis=1)
print("Minimum along rows (axis=1):", row_mins)
```

## 6. Maximum

```
# np.max(array) finds the maximum value in the array.
total_max = np.max(agg_array)
print("\nMaximum element:", total_max)

# Maximum along axes
column_maxs = np.max(agg_array, axis=0)
print("Maximum along columns (axis=0):", column_maxs)
row_maxs = np.max(agg_array, axis=1)
print("Maximum along rows (axis=1):", row_maxs)
```

## 7. Argmin and Argmax

```
# np.argmin(array) finds the index of the minimum value in the flattened array.
total_argmin = np.argmin(agg_array)
print("\nIndex of minimum element (flattened):", total_argmin)

# np.argmax(array) finds the index of the maximum value in the flattened array.
total_argmax = np.argmax(agg_array)
print("Index of maximum element (flattened):", total_argmax)

# Argmin/Argmax along axes give the indices along that axis.
column_argmins = np.argmin(agg_array, axis=0)
print("Indices of minimum along columns (axis=0):", column_argmins)
row_argmins = np.argmin(agg_array, axis=1)
print("Indices of minimum along rows (axis=1):", row_argmins)
```

## 8. Prod

```
# np.prod(array) calculates the product of all elements.
total_prod = np.prod(agg_array)
print("\nProduct of all elements:", total_prod)

# Product along axes
column_prods = np.prod(agg_array, axis=0)
print("Product along columns (axis=0):", column_prods)
row_prods = np.prod(agg_array, axis=1)
print("Product along rows (axis=1):", row_prods)
```

## 9. Median

```
# np.median(array) calculates the median of all elements.
total_median = np.median(agg_array)
print("\nMedian of all elements:", total_median)

# Median along axes
column_medians = np.median(agg_array, axis=0)
print("Median along columns (axis=0):", column_medians)
row_medians = np.median(agg_array, axis=1)
print("Median along rows (axis=1):", row_medians)
```

## 10. Percentile

```
# np.percentile(array, q) calculates the q-th percentile.
# q is a value between 0 and 100.
twenty_fifth_percentile = np.percentile(agg_array, 25)
print("\n25th percentile of all elements:", twenty_fifth_percentile)

# Percentiles along axes
column_75th_percentiles = np.percentile(agg_array, 75, axis=0)
print("75th percentile along columns (axis=0):", column_75th_percentiles)


# Many of these aggregation methods are also available as methods of the array object itself:
print("\n--- Array Methods for Aggregation ---")
print("Sum (using method):", agg_array.sum())
print("Mean (using method):", agg_array.mean(axis=1))
print("Minimum (using method):", agg_array.min())
print("Maximum (using method, axis=0):", agg_array.max(axis=0))

# Using methods is often a bit cleaner syntactically.

# Aggregations are fundamental for summarizing and analyzing data stored in NumPy arrays.
# By specifying the `axis` parameter, you can perform these operations along specific dimensions.
```
