def heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def build_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    n = len(arr)
    build_heap(arr, n)

    # after building heap, the largest element is at the root. so, we swap it with the last element
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        # after swapping, the last element is at the root. but, it is not in the correct position. so, we heapify the root
        heapify(arr, i, 0)


arr = [20, 80, 50, 30, 90, 10, 40, 60, 70, 100]
heap_sort(arr)
print(arr)
