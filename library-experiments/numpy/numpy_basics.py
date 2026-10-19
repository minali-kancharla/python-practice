import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
numbers = np.array([12, 18, 25, 31, 44])
strings = np.array(['apple', 'banana', 'cherry'])

print(arr[1:5]) # start at index 1, stop before index 5.
print(arr[2:]) # Start at index 2 and go to the end.
print(arr[:4]) # Start at the beginning and stop before index 4.
print(arr[-3:-1]) # Indices -3 through before -1
print(arr[1:5:2]) # Start at index 1, stop before 5, move by 2.
print(arr[::4]) # Start at the beginning, go to the end, take every 4th element.

print(arr2[1, 1:4]) # Row 1, columns 1 through 3.
print(arr2[0:2, 2]) # Rows 0 through 1, column 2.
print(arr2[0:2, 1:4]) # Rows 0–1, columns 1–3.
print(arr2.dtype) # dtype = data type
print(strings.dtype) # Unicode strings with a maximum length of x characters.

print(numbers) # outputs array
print(np.mean(numbers)) # average of array of integers
print(np.min(numbers)) # minimum of array
print(np.max(numbers)) # maximum of array
print(np.sum(numbers)) # sum of array
print(numbers * 2) # multiplies array by 2
print(numbers + 10) # adds 10 to array 