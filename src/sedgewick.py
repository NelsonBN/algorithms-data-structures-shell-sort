def shell_sort(arr):
    n = len(arr)

    # Generate the sedgewick sequence of gaps
    gaps = []
    k = 0
    while True:
        if k % 2 == 0:
            gap = 9 * (2**k - 2**(k//2)) + 1
        else:
            gap = 8 * (2**k) - 6 * (2**((k+1)//2)) + 1
        if gap > n:
            break
        gaps.append(gap)
        k += 1

    gaps.reverse()

    # Loop over the gaps
    for gap in gaps:

        # Insertion sort for each gap
        for i in range(gap, n):
            curr = arr[i]
            j = i

            while j >= gap and arr[j - gap] > curr:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = curr


array = [5, 3, 21, 13, 1, 7, 6, 15]
print("Before: ", array)

shell_sort(array)

print("After: ", array)
