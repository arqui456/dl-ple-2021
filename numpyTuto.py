import numpy as np

# NumPy Array

# How to create an empty and a full NumPy array?
empa = np.empty((3, 4), dtype=int)
print("Empty Array")
print(empa)

flla = np.full([3, 3], 55, dtype=int)
print("\n Full Array")
print(flla)

# Create a Numpy array filled with all zeros
zeros = np.zeros(5)
print("\n Zeros Array")
print(zeros)

# Create a Numpy array filled with all ones
ones = źeros.fill(1)
print("\n ones Array")
print(ones)

# Check whether a Numpy array contains a specified row
arr = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])
    
print([1, 2, 3, 4, 5] in arr.tolist())

# How to Remove rows in Numpy array that contains non-numeric values?
n_arr = np.array([[10.5, 22.5, 3.8],
                  [41, np.nan, np.nan]])
  
print(n_arr[~np.isnan(n_arr).any(axis=1)])

# Remove single-dimensional entries from the shape of an array
in_arr = np.array([[[2, 2, 2], [2, 2, 2]]])  
out_arr = np.squeeze(in_arr)

# Find the number of occurrences of a sequence in a NumPy array
arr = np.array([[2, 8, 9, 4], 
                   [9, 4, 9, 4],
                   [4, 5, 9, 7],
                   [2, 9, 4, 3]])
  
output = repr(arr).count("9, 4")

# Find the most frequent value in a NumPy array
x = np.array([1,2,3,4,5,1,2,1,1,1])
print(np.bincount(x).argmax())

# Combining a one and a two-dimensional NumPy Array
num_1d = np.arange(5)  
num_2d = np.arange(10).reshape(2,5) 
for a, b in np.nditer([num_1d, num_2d]):
    print("%d:%d" % (a, b),)

# How to build an array of all combinations of two NumPy arrays?
np.array(np.meshgrid([1, 2, 3], [4, 5], [6, 7])).T.reshape(-1,3)

# How to add a border around a NumPy array?
array = np.ones((2, 2))
array = np.pad(array, pad_width=1, mode='constant',
               constant_values=0)

# How to compare two NumPy arrays?
np.array_equal([1, 2], [1, 2])

# How to check whether specified values are present in NumPy array?
n_array = np.array([[2, 3, 0],
                    [4, 1, 6]])

print(2 in n_array)

# How to get all 2D diagonals of a 3D NumPy array?
np_array = np.arange(3*4*5).reshape(3,4,5)
result = np.diagonal(np_array, axis1=1, axis2=2)

# Flatten a Matrix in Python using NumPy
gfg = np.array([[2, 3], [4, 5]])
flat_gfg = gfg.flatten()

# Flatten a 2d numpy array into 1d array
array_2d = np.array([[1, 2], [3, 4]])
array_1d = array_2d.flatten()

# Move axes of an array to new positions
x = np.zeros((2, 3, 4))
print(np.moveaxis(x, 0, -1).shape)
print(np.moveaxis(x, -1, 0).shape)

# Interchange two axes of an array
x = np.array([[1,2,3]])
y =  np.swapaxes(x,0,1)

# NumPy – Fibonacci Series using Binet Formula
a = np.arange(1, 11)
lengthA = len(a)
sqrtFive = np.sqrt(5)
alpha = (1 + sqrtFive) / 2
beta = (1 - sqrtFive) / 2
Fn = np.rint(((alpha ** a) - (beta ** a)) / (sqrtFive))
print("The first {} numbers of Fibonacci series are {} . ".format(lengthA, Fn))

# Counts the number of non-zero values in the array
np.count_nonzero(np.eye(4))

# Count the number of elements along a given axis
np.unique([1, 1, 2, 2, 3, 3])

# Trim the leading and/or trailing zeros from a 1-D array
gfg = np.array((0, 0, 0, 0, 1, 5, 7, 0, 6, 2, 9, 0, 10, 0, 0))
res = np.trim_zeros(gfg)
print(res)

# Change data type of given numpy array
array = np.array([1.5, 2.6, 3.7, 4.8, 5.9])
array = array.astype(np.int32)

# Reverse a numpy array

# How to make a NumPy array read-only?

# Questions on NumPy Matrix

# Get the maximum value from given matrix

# Get the minimum value from given matrix

# Find the number of rows and columns of a given matrix using NumPy

# Select the elements from a given matrix

# Find the sum of values in a matrix

# Calculate the sum of the diagonal elements of a NumPy array

# Adding and Subtracting Matrices in Python

# Ways to add row/columns in numpy array

# Matrix Multiplication in NumPy

# Get the eigen values of a matrix

# How to Calculate the determinant of a matrix using NumPy?
# How to inverse a matrix using NumPy
# How to count the frequency of unique values in NumPy array?
# Multiply matrices of complex numbers using NumPy in Python
# Compute the outer product of two given vectors using NumPy in Python
# Calculate inner, outer, and cross products of matrices and vectors using NumPy
# Compute the covariance matrix of two given NumPy arrays
# Convert covariance matrix to correlation matrix using Python
# Compute the Kronecker product of two mulitdimension NumPy arrays
# Convert the matrix into a list
# Questions on NumPy Indexing
# Replace NumPy array elements that doesn’t satisfy the given condition
# Return the indices of elements where the given condition is satisfied
# Replace NaN values with average of columns
# Replace negative value with zero in numpy array
# How to get values of an NumPy array at certain index positions?
# Find indices of elements equal to zero in a NumPy array
# How to Remove columns in Numpy array that contains non-numeric values?
# How to access different rows of a multidimensional NumPy array?
# Get row numbers of NumPy array having element larger than X
# Get filled the diagonals of NumPy array
# Check elements present in the NumPy array
# Combined array index by index
# Questions on NumPy Linear Algebra
# Find a matrix or vector norm using NumPy
# Calculate the QR decomposition of a given matrix using NumPy
# Compute the condition number of a given matrix using NumPy
# Compute the eigenvalues and right eigenvectors of a given square array using NumPy?
# Calculate the Euclidean distance using NumPy
# Questions on NumPy Random
# Create a Numpy array with random values
# How to choose elements from the list with different probability using NumPy?
# How to get weighted random choice in Python?
# Generate Random Numbers From The Uniform Distribution using NumPy
# Get Random Elements form geometric distribution
# Get Random elements from Laplace distribution
# Return a Matrix of random values from a uniform distribution
# Return a Matrix of random values from a Gaussian distribution
# Questions on NumPy Sorting and Searching
# How to get the indices of the sorted array using NumPy in Python?
# Finding the k smallest values of a NumPy array
# How to get the n-largest values of an array using NumPy?
# Sort the values in a matrix
# Filter out integers from float numpy array
# Find the indices into a sorted array
# Questions on NumPy Mathematics
# How to get element-wise true division of an array using Numpy?
# How to calculate the element-wise absolute value of NumPy array?
# Compute the negative of the NumPy array
# Multiply 2d numpy array corresponding to 1d array
# Computes the inner product of two arrays
# Compute the nth percentile of the NumPy array
# Calculate the n-th order discrete difference along the given axis
# Calculate the sum of all columns in a 2D NumPy array
# Calculate average values of two given NumPy arrays
# How to compute numerical negative value for all elements in a given NumPy array?
# How to get the floor, ceiling and truncated values of the elements of a numpy array?
# How to round elements of the NumPy array to the nearest integer?
# Find the round off the values of the given matrix
# Determine the positive square-root of an array
# Evaluate Einstein’s summation convention of two multidimensional NumPy arrays
# Questions on NumPy Statistics
# Compute the median of the flattened NumPy array
# Find Mean of a List of Numpy Array
# Calculate the mean of array ignoring the NaN value
# Get the mean value from given matrix
# Compute the variance of the NumPy array
# Compute the standard deviation of the NumPy array
# Compute pearson product-moment correlation coefficients of two given NumPy arrays
# Calculate the mean across dimension in a 2D NumPy array
# Calculate the average, variance and standard deviation in Python using NumPy
# Describe a NumPy Array in Python
# Questions on Polynomial
# Define a polynomial function
# How to add one polynomial to another using NumPy in Python?
# How to subtract one polynomial to another using NumPy in Python?
# How to multiply a polynomial to another using NumPy in Python?
# How to divide a polynomial to another using NumPy in Python?
# Find the roots of the polynomials using NumPy
# Evaluate a 2-D polynomial series on the Cartesian product
# Evaluate a 3-D polynomial series on the Cartesian product
# Questions on NumPy Strings
# Repeat all the elements of a NumPy array of strings
# How to split the element of a given NumPy array with spaces?
# How to insert a space between characters of all the elements of a given NumPy array?
# Find the length of each string element in the Numpy array
# Swap the case of an array of string
# Change the case to uppercase of elements of an array
# Change the case to lowercase of elements of an array
# Join String by a seperator
# Check if two same shaped string arrayss one by one
# Count the number of substrings in an array
# Find the lowest index of the substring in an array
# Get the boolean array when values end with a particular character
# More Questions on NumPy
# Different ways to convert a Python dictionary to a NumPy array
# How to convert a list and tuple into NumPy arrays?
# Ways to convert array of strings to array of floats
# Convert a NumPy array into a csv file
# How to Convert an image to NumPy array and save it to CSV file using Python?
# How to save a NumPy array to a text file?
# Load data from a text file
# Plot line graph from NumPy array
# Create Histogram using NumPy