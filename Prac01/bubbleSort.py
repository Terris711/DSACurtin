
import numpy as np

# Sorting as ascending 

def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr - 1 - i)):
                if (arr[j] >  arr[j + 1]):
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
    return arr

arr = np.array([ 1, 58, 32, 7, 8, 3, 5, 9, 14])
print(bubbleSort(arr))
