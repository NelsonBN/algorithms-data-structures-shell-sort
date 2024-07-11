import random
import math

def insert_sort(arr):
    total_swaps = 0
    total_comparisons = 0

    n = len(arr)

    for i in range(1, n):
        curr = arr[i]
        j = i

        while j > 0:
            total_comparisons += 1

            if arr[j - 1] > curr:
                total_swaps += 1
                arr[j] = arr[j - 1]
                j -= 1
            else:
                break

        arr[j] = curr

    return total_swaps, total_comparisons



def shell_sort(arr):
    total_swaps = 0
    total_comparisons = 0

    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            curr = arr[i]
            j = i

            while j >= gap:
                total_comparisons += 1

                if arr[j - gap] > curr:
                    total_swaps += 1
                    arr[j] = arr[j - gap]
                    j -= gap
                else:
                    break

            arr[j] = curr

        gap //= 2

    return total_swaps, total_comparisons



def shell_sort_knuth(arr):
    total_swaps = 0
    total_comparisons = 0

    n = len(arr)

    k = math.log(n + 1) / math.log(3)
    k = math.floor(k + 0.5)

    gap = (3 ** k - 1) // 2

    while gap > 0:
        for i in range(gap, n):
            curr = arr[i]
            j = i

            while j >= gap:
                total_comparisons += 1

                if arr[j - gap] > curr:
                    total_swaps += 1
                    arr[j] = arr[j - gap]
                    j -= gap
                else:
                    break

            arr[j] = curr

        gap = (gap - 1) // 3

    return total_swaps, total_comparisons


def shell_sort_sedgewick(arr):
    total_swaps = 0
    total_comparisons = 0

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

            while j >= gap:
                total_comparisons += 1

                if arr[j - gap] > curr:
                    total_swaps += 1
                    arr[j] = arr[j - gap]
                    j -= gap
                else:
                    break

            arr[j] = curr

    return total_swaps, total_comparisons




total_items = 30

array_insert = [random.randint(0, 100) for _ in range(total_items)]
array_shell = array_insert.copy()
array_knuth = array_insert.copy()
array_sedgewick = array_insert.copy()


print("Insertion Sort")
print("Before: ", array_insert)
swaps, comparisons = insert_sort(array_insert)
print("After: ", array_insert)
print("Total swaps: ", swaps)
print("Total comparisons: ", comparisons)


print("\nShell Sort")
print("Before: ", array_shell)
swaps, comparisons = shell_sort(array_shell)
print("After: ", array_shell)
print("Total swaps: ", swaps)
print("Total comparisons: ", comparisons)


print("\nShell Sort - Knuth's sequence")
print("Before: ", array_knuth)
swaps, comparisons = shell_sort_knuth(array_knuth)
print("After: ", array_knuth)
print("Total swaps: ", swaps)
print("Total comparisons: ", comparisons)


print("\nShell Sort - Sedgewick's sequence")
print("Before: ", array_sedgewick)
swaps, comparisons = shell_sort_sedgewick(array_sedgewick)
print("After: ", array_sedgewick)
print("Total swaps: ", swaps)
print("Total comparisons: ", comparisons)
