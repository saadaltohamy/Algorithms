import random
# quick sort

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


def partition(arr, s, e):
    # Get a random pivot index
    pivot_index = random.randint(s, e)
    pivot_value = arr[pivot_index]

    # Move pivot to the end
    swap(arr, pivot_index, e)

    # Apply partition algorithm
    pivot = s - 1
    for i in range(s, e):
        if arr[i] < pivot_value:    # if element is less than pivot value
            pivot += 1
            swap(arr, pivot, i)     # then, element should be in the left side of pivot
    # Now, all elements less than pivot value are in the left side of pivot index
            
    pivot += 1                      
    swap(arr, e, pivot)             # then, increase pivot index by 1 and swap 

    return pivot


def quick_sort(arr, s, e):
    '''
    Quick sort algorithm
    asympotic complexity: O(n^2), Ω(n log n), Θ(n log n), in-place, unstable
    space complexity: O(log n) 
    '''
    if e > s:
        pivot = partition(arr, s, e)
        quick_sort(arr, s, pivot - 1)
        quick_sort(arr, pivot + 1, e)


arr = [5, 3, 3, 2, 7, 6]
quick_sort(arr, 0, len(arr) - 1)
print(f"Sorted array with Quick Sort:\n {arr}")