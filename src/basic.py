def shell_sort(arr):
    n = len(arr)
    gap = n // 2 # Inicialization of gap as half of the length of the list

    # Loop over the gaps
    while gap > 0:

        # Insertion sort for each gap
        for i in range(gap, n):
            curr = arr[i]
            j = i

            while j >= gap and arr[j - gap] > curr:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = curr

        # Reduce the gap
        gap //= 2


array = [5, 3, 21, 13, 1, 7, 6, 15]
print("Before: ", array)

shell_sort(array)

print("After: ", array)
