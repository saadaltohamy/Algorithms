# merge sort algorithm


def merge_sort(arr):
    '''
    Merge sort algorithm
    asympotic complexity: O(n log n), Ω(n log n), Θ(n log n), stable
    space complexity: O(n)
    '''
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


# merge function
def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while i < len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1


arr = [5, 4, 3, 2, 1]
merge_sort(arr)
print(arr)
