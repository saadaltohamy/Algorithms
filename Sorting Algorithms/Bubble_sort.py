def bubble_sort(arr):
    """
    Bubble sort algorithm

    asympotic complexity: O(n^2), Ω(n), Θ(n^2), in-place, stable 
    space complexity: O(1)
    """
    swapped = True
    while swapped:
        i = 0
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True
        i += 1


arr = [5, 2, 3, 8, 6, 9]
bubble_sort(arr)
print(arr)

'''
| Sorting Algorithm      |         (Big-O)         |         (Big-Ω)         |         (Big-Θ)         | Space Complexity |
|------------------------|-------------------------|-------------------------|-------------------------|------------------|
| Bubble Sort            | O(n^2)                  | Ω(n)                    | Θ(n^2)                  | O(1)             |
| Selection Sort         | O(n^2)                  | Ω(n^2)                  | Θ(n^2)                  | O(1)             |
| Insertion Sort         | O(n^2)                  | Ω(n)                    | Θ(n^2)                  | O(1)             |
| Merge Sort             | O(n log n)              | Ω(n log n)              | Θ(n log n)              | O(n)             |
| Quick Sort             | O(n^2)                  | Ω(n log n)              | Θ(n log n)              | O(log n)         |
| Heap Sort              | O(n log n)              | Ω(n log n)              | Θ(n log n)              | O(1)             |
| Counting Sort          | O(n + k)                | Ω(n + k)                | Θ(n + k)                | O(k)             |
| Radix Sort             | O(nk)                   | Ω(nk)                   | Θ(nk)                   | O(n + k)         |
| Bucket Sort            | O(n^2)                  | Ω(n + k)                | Θ(n + k)                | O(n + k)         |

'''
