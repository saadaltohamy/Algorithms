def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [5, 4, 3, 2, 1]
print(linear_search(arr, 3))