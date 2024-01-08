def binary_search(array, start, end, target):
    while end > start:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        else:
            if target < array[mid]:
                end = mid - 1
                binary_search(array, start, end, target)
            if target > array[mid]:
                start = mid + 1
                binary_search(array, start, end, target)
    return -1


arr = [8, 10, 15, 17, 19]
print(binary_search(arr, 0, len(arr), 15))