def insertion_sort(arr):
    """
    Insertion sort algorithm

    asympotic complexity: O(n^2), Ω(n), Θ(n^2), in-place, stable 
    space complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [5, 2, 3, 8, 6, 9]
insertion_sort(arr)
print(arr)