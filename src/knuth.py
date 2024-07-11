import math

def shell_sort(arr):
    n = len(arr)

    # Calculate k based on Knuth's sequence
    k = math.log(n + 1) / math.log(3)
    k = math.floor(k + 0.5)

    # Calcula inicial gap based on Knuth's sequence
    gap = (3 ** k - 1) // 2

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

        # Reduce the gap for the next sequence
        gap = (gap - 1) // 3


array = [5, 3, 21, 13, 1, 7, 6, 15]
print("Before: ", array)

shell_sort(array)

print("After: ", array)
