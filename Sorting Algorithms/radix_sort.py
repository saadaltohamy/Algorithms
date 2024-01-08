def counting_sort(array, exp1):
    """
    Counting sort algorithm
    asymptotic complexity: O(n + k), Ω(n + k), Θ(n + k), stable
    space complexity: O(n + k)
    """
    n = len(array)
    # The output array elements that will have sorted array
    output = [0] * (n)
    # initialize count array as 0
    count = [0] * (10)
    # Store count of occurrences in count[]
    for i in array:
        index = i // exp1
        count[index % 10] += 1
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build the output array
    i = n - 1
    while i >= 0:
        index = (array[i] // exp1)
        count[index % 10] -= 1
        x = count[index % 10]
        output[x] = array[i]
        i -= 1
    # Copying the output array to array[],
    # so that array now contains sorted numbers
    for i in range(0, len(array)):
        array[i] = output[i]
def radix_sort(array):
    """
    Radix sort algorithm
    asymptotic complexity: O(nk), Ω(nk), Θ(nk), stable
    space complexity: O(n + k)
    """
    # Find the maximum number to know number of digits
    max1 = max(array)
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort(array, exp)
        exp *= 10


arr = [195, 25, 86, 689, 750]
radix_sort(arr)
print(arr)
