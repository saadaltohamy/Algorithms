def counting_sort(array):
    """
    Counting sort algorithm
    asympotic complexity: O(n + k), Ω(n + k), Θ(n + k), stable
    space complexity: O(n + k)
    """
    # Create a list to store the final sorted array
    result = [0] * (len(array))

    # Create a list to store the count of each element
    count = [0] * (max(array) + 1) 

    # Store the count of each element in count_array
    for i in array:
        count[i] += 1

    # Store the cumulative count of each array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = len(array) - 1
    while i >= 0:
        count[array[i]] -= 1
        x = count[array[i]]
        result[x] = array[i]
        i -= 1
    
    # Copying the result array to array[],
    for i in range(0, len(array)):
        array[i] = result[i]

arr = [4, 8, 4, 2, 9, 9, 6, 2, 9]
counting_sort(arr)
print(arr)
