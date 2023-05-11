import numpy as np

dataset1 = np.array([1, 2, 3, 4, 5])
dataset2 = np.array([5, 4, 3, 2, 1])

print(np.corrcoef(dataset1, dataset2))
