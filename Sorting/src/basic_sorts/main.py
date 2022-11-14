import numpy as np
from BasicSorts import insertionSort, recurSelectionSort, minIndex

a = np.random.randint(100, size=10)

recurSelectionSort(a, len(a))

print(a)
