# Sorting Algorithms in Python

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    # Merge the sorted halves into arr
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements in left and right
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr



def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
    import heapq
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Test all sorting algorithms
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]

    print("Original Array:", arr)
    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Selection Sort:", selection_sort(arr.copy()))
    print("Insertion Sort:", insertion_sort(arr.copy()))
    print("Merge Sort:", merge_sort(arr.copy()))
    print("Quick Sort:", quick_sort(arr.copy()))
    print("Heap Sort:", heap_sort(arr.copy()))


class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, l, r):
        if l < r:
            p = self.partition(arr, l, r)
            self.quickSort(arr, l, p - 1)
            self.quickSort(arr, p + 1, r)

    def partition(self, arr, l, r):
        p = arr[r]  # Choose the pivot as the last element
        i = l - 1  # Index for the smaller element

        for j in range(l, r):  # Iterate from l to r-1
            if arr[j] <= p:  # If the current element is <= pivot
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap

        # Place the pivot in its correct position
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1  # Return the pivot index


# Example Usage
arr = [38, 27, 43, 3, 9, 82, 10]
solution = Solution()
solution.quickSort(arr, 0, len(arr) - 1)
print(arr)  # Output: [3, 9, 10, 27, 38, 43, 82]


from typing import List
import math

def merge(arr : List[int], low : int, mid : int, high : int) -> int:
    temp = []   # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1 # starting index of right half of arr

    cnt = 0     # Modification 1: cnt variable to count the pairs

    # storing elements in the temporary array in a sorted manner
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)  # Modification 2
            right += 1

    # if elements on the left half are still left
    while (left <= mid):
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while (right <= high):
        temp.append(arr[right])
        right += 1

    # transfering all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt   # Modification 3

def mergeSort(arr : List[int], low : int, high : int) -> int:
    cnt = 0
    if low >= high:
        return cnt
    mid = math.floor((low + high) / 2)
    cnt += mergeSort(arr, low, mid)    # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += merge(arr, low, mid, high)  # merging sorted halves
    return cnt

def numberOfInversions(a : List[int], n : int) -> int:
    # Count the number of pairs:
    n = len(a)
    # Count the number of pairs:
    return mergeSort(a, 0, n - 1)

if __name__ == "__main__":
    a = [5, 4, 3,3, 2, 1]
    n = 5
    cnt = numberOfInversions(a, n)
    print("The number of inversions are:", cnt)


