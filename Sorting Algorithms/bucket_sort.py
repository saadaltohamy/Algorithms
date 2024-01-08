def bucket_sort(arr, num_buckets):
    """
    Bucket sort algorithm
    asympotic complexity: O(n^2), Ω(n + k), Θ(n + k), Stable Or UnStable? it depends on the sorting algorithm you use.
    space complexity: O(n + k)
    """
    # Create a list to store the final sorted array
    result = []

    # Create a list to store the buckets
    buckets = [[] for _ in range(num_buckets)]

    # Store the elements in the buckets
    for i in arr:
        x = int((i / (max(arr) + 1)) * num_buckets)     # Hash-function, you can change it to any hash-function as you want
        buckets[x].append(i)

    # Sort the elements in each bucket
    for i in range(num_buckets):
        buckets[i].sort()       # you can use any sorting algorithm as you want

    # Place the elements in sorted order
    for i in range(num_buckets):
        result.extend(buckets[i])

    # Copying the result array to arr[]
    for i in range(0, len(arr)):
        arr[i] = result[i]

arr = [4, 8, 4, 2, 9, 9, 6, 2, 9]
bucket_sort(arr, 3)
print(arr)