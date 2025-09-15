import numpy as np

# ---------------------------
# Question 1: Array Creation
# ---------------------------

# 1.1 Create a 1D array of integers ranging from 5 to 25
myFirstArray = np.arange(5, 26)
print("Question 1.1 - Array from 5 to 25:")
print(myFirstArray)

# 1.2 Create a 2D array with 3 rows and 4 columns, filled with random integers between 10 and 50
myRandomArray = np.random.randint(10, 51, size=(3,4))
print("\nQuestion 1.2 - Random 3x4 array:")
print(myRandomArray)


# ---------------------------
# Question 2: Array Attributes
# ---------------------------

# 2.1 For the 1D array created in Question 1.1, find and print its attributes
print("\nQuestion 2.1 - Attributes of 1D array:")
print("Shape of array:", myFirstArray.shape)
print("Size of array:", myFirstArray.size)
print("Data type:", myFirstArray.dtype)

# 2.2 For the 2D array created in Question 1.2, find and print its attributes
print("\nQuestion 2.2 - Attributes of 2D array:")
print("Shape of array:", myRandomArray.shape)
print("Size of array:", myRandomArray.size)
print("Data type:", myRandomArray.dtype)


# ---------------------------
# Question 3: Array Operations
# ---------------------------

# 3.1 Create two 1D arrays
firstNumbers = np.array([2,4,6,8,10])
secondNumbers = np.array([1,3,5,7,9])

# 3.2 Perform operations on the arrays
print("\nQuestion 3.2 - Array Operations:")
print("Addition result:", firstNumbers + secondNumbers)
print("Subtraction result:", firstNumbers - secondNumbers)
print("Element-wise multiplication:", firstNumbers * secondNumbers)
print("Element-wise division:", firstNumbers / secondNumbers)


# ---------------------------
# Question 4: Broadcasting
# ---------------------------

# 4.1 Create a 2D array of shape (3, 3) with values starting from 1 to 9
mySquareArray = np.arange(1,10).reshape(3,3)
print("\nQuestion 4.1 - 3x3 array:")
print(mySquareArray)

# 4.2 Using broadcasting, multiply this 2D array by a scalar value of 5
multipliedArray = mySquareArray * 5
print("\nQuestion 4.2 - Array multiplied by 5:")
print(multipliedArray)


# ---------------------------
# Question 5: Slicing and Indexing
# ---------------------------

# 5.1 Create a 2D array of shape (4, 4) with values ranging from 10 to 25
myGridArray = np.arange(10,26).reshape(4,4)
print("\nQuestion 5.1 - 4x4 array:")
print(myGridArray)

# 5.2 Extract the second row and the last column of the array
secondRow = myGridArray[1]
lastColumn = myGridArray[:, -1]
print("\nQuestion 5.2 - Second row:", secondRow)
print("Last column:", lastColumn)

# 5.3 Replace the elements of the first row with zeros
myGridArray[0] = 0
print("\nQuestion 5.3 - After replacing first row with zeros:")
print(myGridArray)


# ---------------------------
# Question 6: Boolean Indexing
# ---------------------------

# 6.1 Create a 1D array with 10 elements, filled with random integers between 20 and 40
myRandomNumbers = np.random.randint(20,41, size=10)
print("\nQuestion 6.1 - Random array:")
print(myRandomNumbers)

# 6.2 Use Boolean indexing to find all elements in this array that are greater than 30
greaterThanThirty = myRandomNumbers[myRandomNumbers > 30]
print("\nQuestion 6.2 - Elements greater than 30:")
print(greaterThanThirty)


# ---------------------------
# Question 7: Reshaping
# ---------------------------

# 7.1 Create a 1D array containing 12 elements, starting from the value 11
myLinearArray = np.arange(11, 23)
print("\nQuestion 7.1 - 1D array:")
print(myLinearArray)

# 7.2 Reshape the 1D array into a 2D array with a shape of (3, 4)
reshapedArray = myLinearArray.reshape(3,4)
print("\nQuestion 7.2 - Reshaped to 3x4:")
print(reshapedArray)


# ---------------------------
# Question 8: Matrix Operations
# ---------------------------

# 8.1 Create two 2x2 matrices
matrixA = np.array([[1,2],[3,4]])
matrixB = np.array([[5,6],[7,8]])

# 8.2 Perform matrix operations
matrixProduct = np.dot(matrixA, matrixB)
transposeA = matrixA.T
print("\nQuestion 8.2 - Matrix Operations:")
print("Matrix multiplication result:")
print(matrixProduct)
print("\nTranspose of Matrix A:")
print(transposeA)


# ---------------------------
# Question 9: Statistical Functions
# ---------------------------

# 9.1 Create a 1D array containing 15 random integers, with values ranging between 10 and 60
myDataArray = np.random.randint(10,61, size=15)
print("\nQuestion 9.1 - Random data array:")
print(myDataArray)

# 9.2 Compute statistics for the array
arrayMean = np.mean(myDataArray)
arrayMedian = np.median(myDataArray)
arrayStdDev = np.std(myDataArray)
print("\nQuestion 9.2 - Statistics:")
print("Mean:", arrayMean)
print("Median:", arrayMedian)
print("Standard deviation:", arrayStdDev)


# ---------------------------
# Question 10: Linear Algebra
# ---------------------------

# 10.1 Create a 3x3 matrix
myMatrix = np.array([[2,1,3],[0,5,6],[7,8,9]])

# 10.2 Perform linear algebra operations
matrixDeterminant = np.linalg.det(myMatrix)
matrixInverse = np.linalg.inv(myMatrix)
eigenvalues, eigenvectors = np.linalg.eig(myMatrix)
print("\nQuestion 10.2 - Linear Algebra Operations:")
print("Determinant:", matrixDeterminant)
print("\nInverse matrix:")
print(matrixInverse)
print("\nEigenvalues:", eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)


# ---------------------------
# Question 11: Robot Movement and Distance
# ---------------------------

# Dataset: Robot positions at different time steps
robotPositions = np.array([[0,0],[2,3],[4,7],[7,10],[10,15]])

# 11.1 Euclidean distance between the first and last recorded positions
firstPosition = robotPositions[0]
lastPosition = robotPositions[-1]
directDistance = np.linalg.norm(lastPosition - firstPosition)
print("\nQuestion 11.1 - Direct distance from first to last position:")
print("Distance:", directDistance)

# 11.2 Total distance traveled by the robot (sum of distances between consecutive positions)
positionDifferences = np.diff(robotPositions, axis=0)
stepDistances = np.linalg.norm(positionDifferences, axis=1)
totalDistanceTraveled = np.sum(stepDistances)
print("\nQuestion 11.2 - Total distance traveled:")
print("Total distance:", totalDistanceTraveled)