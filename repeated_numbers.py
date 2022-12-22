def repeated_numbers(arr, n):
    map = {}
    # traverse through array elements and count frequencies
    for i in range(n):
        if arr[i] not in map:
            map[arr[i]] = 0
        map[arr[i]] += 1

    # to print elements according to first occurrance,
    # traverse array one more time, print frequencies and mark frequencies as -1
    # so that same element is not printed multiple times
    for i in range(n):
        if (map[arr[i]] != -1):
            print(arr[i], map[arr[i]])
        map[arr[i]] = -1


arr = [10, 20, 20, 10, 10, 20, 5, 20]
n = len(arr)
repeated_numbers(arr, n)
# Time: O(n) | space: O(n)
