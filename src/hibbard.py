def shell_sort(arr):
    n = len(arr)

    # Generate the Hibbard sequence of gaps (2^k - 1)
    gaps = []
    k = 1
    while (2**k - 1) < n:
        gaps.append(2**k - 1)
        k += 1

    gaps.reverse()

    # Loop over the gaps
    for gap in gaps:

        # Insertion sort for each gap
        for i in range(gap, n):
            j = i

            while j >= gap and arr[j - gap] > arr[j]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap


array = [5, 3, 21, 13, 1, 7, 6, 15]
print("Before: ", array)

shell_sort(array)

print("After: ", array)
