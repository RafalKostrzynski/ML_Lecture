import numpy as np

# Array with zeros only
zeros = np.zeros(10)
print("Zeros:\n", zeros, "\n")

# Array with fives only
fives = np.ones(10) * 5
print("Fives:\n", fives, "\n")

# Array with digits from 10 to 50
tableTenToFifty = np.arange(10, 51, 1)
print("Ten to Fifty array:\n", tableTenToFifty, "\n")

# 3x3 Array with digits from 0 to 8
matrix = np.arange(0, 9, 1).reshape((3, 3))
print("3x3 matrix 0 to 8:\n", matrix, "\n")

# 3x3 Array with zeros only
d3zerosMatrix = np.zeros((3, 3))
print("3x3 matrix zeros:\n", d3zerosMatrix, "\n")

# 3x3 Array with zeros only
d3zerosMatrix = np.zeros((3, 3))
print("3x3 matrix zeros:\n", d3zerosMatrix, "\n")

# 5x5 Array gauss distributed values
gauss = np.random.normal(size=(5, 5))
print("Gaus:\n", gauss, "\n")

# 10x10 Array digits from 0.01 to 1
tenXTenArray = np.arange(0.01, 1.01, 0.01).reshape((10, 10))
print("10x10 Array:\n", tenXTenArray, "\n")

# Array with digits from 0 to 1 included, linear distributed
linspaceValues = np.linspace(0, 1, 20)
print("Evenly spaced values:\n", linspaceValues, "\n")

# Array with random values from 1 to 25 (reshape(),sum(),mean(), std(), sum(axis))
randomNumbers1To25 = np.random.randint(1, 26, 25)
print("Random numbers from 1 to 25:\n", randomNumbers1To25, "\n")
randomNumbers1To25 = randomNumbers1To25.reshape((5, 5))
print("Reshaped random numbers:\n", randomNumbers1To25, "\n")
print("Sum of all values:\n", randomNumbers1To25.sum(), "\n")
print("Mean of all values:\n", randomNumbers1To25.mean(), "\n")
print("Deviation of all values:\n", randomNumbers1To25.std(), "\n")

sumOfColumns = randomNumbers1To25.sum(axis=0)
print("Sum of columns:\n", sumOfColumns, "\n")

# Array with random values from 0 to 100 (median(), min(), max())
randomNumbers5x5 = np.random.randint(0, 101, (5, 5))
print("5 x 5 random numbers:\n", randomNumbers5x5, "\n")
print("Median of the random numbers:\n", np.median(randomNumbers5x5), "\n")
print("Min of the random numbers:\n", np.min(randomNumbers5x5), "\n")
print("Max of the random numbers:\n", np.max(randomNumbers5x5), "\n")

# Random numbers with random axis size (transposition)


def set_y():
    y_axis = np.random.randint(2, 11)
    if y_axis != x:
        return y_axis
    else:
        y_axis = set_y()
        return y_axis


x = np.random.randint(2, 11)
y = set_y()
randomNumbersRandomAxis = np.random.randint(0, 101, (x, y))
print("Random numbers with random axis size:\n", randomNumbersRandomAxis, "\n")
print("Transposition:\n", randomNumbersRandomAxis.transpose(), "\n")

# Matrix addition
matrixX = np.random.randint(2, 11)
matrixY = np.random.randint(2, 11)
matrixA = np.random.randint(0, 101, (matrixX, matrixY))
print("Matrix A + Matrix B:\n", matrixA, "\n")
matrixB = np.random.randint(0, 101, (matrixX, matrixY))
print("Matrix A + Matrix B:\n", matrixB, "\n")
print("Matrix A + Matrix B:\n", matrixA + matrixB, "\n")

# Matrix multiplication
matrixXMultiply = np.random.randint(2, 11)
matrixYMultiply = np.random.randint(2, 11)
matrixAMultiply = np.random.randint(0, 101, (matrixXMultiply, matrixYMultiply))
print("Matrix A for multiplication:\n", matrixAMultiply, "\n")
matrixBMultiply = np.random.randint(0, 101, (matrixYMultiply, matrixXMultiply))
print("Matrix B for multiplication:\n", matrixBMultiply, "\n")
print("Matrix A * Matrix B with np.matmul():\n", np.matmul(matrixAMultiply, matrixBMultiply), "\n")
print("Matrix A * Matrix B with np.dot():\n", np.dot(matrixAMultiply, matrixBMultiply), "\n")
