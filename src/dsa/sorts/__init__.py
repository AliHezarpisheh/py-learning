"""
Sorting Algorithms

This module provides a brief overview of various sorting algorithms. Sorting algorithms
are used to arrange elements in a list or array in a specific order, typically in
ascending or descending order.

1. Bubble Sort
   - Description: Bubble Sort repeatedly steps through the list, compares adjacent
     elements, and swaps them if they are in the wrong order. The process is repeated
     until the list is sorted.
   - Time Complexity: O(n^2) in the average and worst case.
   - Space Complexity: O(1).
   - Stability: Yes.

2. Selection Sort
   - Description: Selection Sort repeatedly finds the minimum element from the unsorted
     portion of the list and places it at the beginning. It maintains two sublists
     within the given list, one that is sorted and one that is unsorted.
   - Time Complexity: O(n^2) for both average and worst-case scenarios.
   - Space Complexity: O(1).
   - Stability: No.

3. Insertion Sort
   - Description: Insertion Sort builds the sorted array one item at a time. It takes
     each element from the input data and finds the position it belongs to in the
     sorted list and inserts it there.
   - Time Complexity: O(n^2) in the average and worst case, O(n) in the best case.
   - Space Complexity: O(1).
   - Stability: Yes.

4. Merge Sort
   - Description: Merge Sort is a divide-and-conquer algorithm that divides the input
     list into two halves, recursively sorts them, and then merges the two sorted halves
     to produce the sorted list.
   - Time Complexity: O(n log n) for average and worst cases.
   - Space Complexity: O(n).
   - Stability: Yes.

5. Quick Sort
   - Description: Quick Sort is a divide-and-conquer algorithm that selects a 'pivot'
     element from the array and partitions the other elements into two sub-arrays,
     according to whether they are less than or greater than the pivot. The sub-arrays
     are then sorted recursively.
   - Time Complexity: O(n log n) on average, O(n^2) in the worst case.
   - Space Complexity: O(log n) due to the recursive stack space.
   - Stability: No.

6. Heap Sort
   - Description: Heap Sort involves building a heap data structure from the input data,
     and then repeatedly extracting the maximum element from the heap and rebuilding the
     heap until it is empty, thus forming a sorted list.
   - Time Complexity:
   - Time Complexity: O(n log n) for both average and worst cases.
   - Space Complexity: O(1).
   - Stability: No.

7. Radix Sort
   - Description: Radix Sort is a non-comparative sorting algorithm that sorts numbers
     by processing individual digits. It processes each digit from the least significant
     to the most significant, grouping the numbers by each digit's value.
   - Time Complexity: O(d * (n + k)), where d is the number of digits, n is the number
     of elements, and k is the range of the digit values.
   - Space Complexity: O(n + k).
   - Stability: Yes.

8. Counting Sort
   - Description: Counting Sort is a non-comparative integer sorting algorithm that
     works by counting the number of objects that have distinct key values, and then
     calculating the positions of each key in the output sequence.
   - Time Complexity: O(n + k), where n is the number of elements and k is the range of
     the input.
   - Space Complexity: O(n + k).
   - Stability: Yes.
"""
