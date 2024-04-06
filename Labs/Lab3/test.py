import numpy as np

matrix = np.empty((11, 11), int)

count = 0
for i in range(11):
    for j in range(11):
        matrix[i, j] = count
        count += 1
print(matrix)