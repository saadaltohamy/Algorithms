def selection_sort(array):
    """
    Selection sort algorithm

    asympotic complexity: O(n^2), Ω(n^2), Θ(n^2), in-place, stable 
    space complexity: O(1)
    """
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]



arr = [5, 2, 3, 8, 6, 9]
selection_sort(arr)
print(arr)
