"""
Merge Sort is a popular sorting algorithm that follows the divide-and-conquer strategy.
It divides the input array into two halves, recursively sorts them, and then merges the
sorted halves to produce a single sorted array. The key operation in Merge Sort is the
merging step, where two sorted arrays are combined to form a single sorted array.

Here's a step-by-step explanation of the Merge Sort algorithm:

Divide: Split the array into two halves.
Conquer: Recursively sort each half.
Combine (Merge): Merge the sorted halves to produce a single sorted array.
The merging step involves comparing elements from the two sorted halves and adding the
smaller (or larger, depending on the sorting order) element to the final merged array.
This process continues until all elements from both halves are merged.
"""


def merge_sort(arr: list) -> list[int]:
    if len(arr) > 1:
        # Split the array into two halves.
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort each half.
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves.
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [12, 654, 320, 5620, 123, 547, 8329]
merge_sort(arr)
print(arr)
