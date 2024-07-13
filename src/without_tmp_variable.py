def shell_sort(arr):
    n = len(arr)
    gap = n // 2 # Inicialization of gap as half of the length of the list

    # Loop over the gaps
    while gap > 0:

        # Insertion sort for each gap
        for i in range(gap, n):
            j = i

            while j >= gap and arr[j - gap] > arr[j]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap

        # Reduce the gap
        gap //= 2


array = [5, 3, 21, 13, 1, 7, 6, 15]
print("Before: ", array)

shell_sort(array)

print("After: ", array)
