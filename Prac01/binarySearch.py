import numpy as np

def binarySearch(arr, target):
    matchIndex = -1
    lowerBd = 0
    upperBd = len(arr) - 1
    found = False

    while (not found and lowerBd <= upperBd):
       
        checkIndex = (lowerBd + upperBd) // 2

        if (arr[checkIndex] < target):
            lowerBd = checkIndex + 1

        elif (arr[checkIndex] > target):
            upperBd = checkIndex - 1
        else:
            matchIndex = checkIndex
            found = True
            return matchIndex

target = int(input("Please enter your number: "))
arr = np.array([1,2,3,6,4,7,8])
answer = binarySearch(arr, target)
print("Answer: ", answer)



