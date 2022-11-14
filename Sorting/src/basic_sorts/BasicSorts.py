def minIndex(a, i, j):
    if i == j:
        return i

    # Find minimum of remaining elements
    k = minIndex(a, i + 1, j)

    # Return minimum of current and remaining
    return i if a[i] < a[k] else k


def recurSelectionSort(a, n, index=0):
    # Return when starting and size
    if index == n:
        return -1

    # Calling minimum index function for minimum index
    k = minIndex(a, index, n - 1)

    # Swapping when index and minimum index are not the same
    if k != index:
        a[k], a[index] = a[index], a[k]

    # Recursively calling selection sort function
    recurSelectionSort(a, n, index + 1)


# Time complexity O(n^2)

def insertionSort(arr, n):
    # Base case
    if n <= 1:
        return

    # Sort first n-1 elements
    insertionSort(arr, n - 1)

    # Insert last element at its correct position

    last = arr[n - 1]
    j = n - 2

    # Move elements of arr[0...i-1] that are greater than key, to one position ahead of there current position
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last

