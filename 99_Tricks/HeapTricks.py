import heapq


def mincostToHireWorkers(quality, wage, k):
    workers = sorted([(w / q, q, w) for q, w in zip(quality, wage)])
    min_cost = float('inf')
    quality_heap = []
    quality_sum = 0

    for ratio, q, w in workers:
        heapq.heappush(quality_heap, -q)  # Use max-heap (negative values)
        quality_sum += q

        if len(quality_heap) > k:
            quality_sum += heapq.heappop(quality_heap)  # Remove largest quality

        if len(quality_heap) == k:
            min_cost = min(min_cost, quality_sum * ratio)

    return min_cost


# Example usage
quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
print(mincostToHireWorkers(quality, wage, k))  # Output: 105

import heapq


def min_heap_examples():
    # Create an empty min-heap
    min_heap = []

    # Insert elements using heapq.heappush()
    heapq.heappush(min_heap, 20)
    heapq.heappush(min_heap, 10)
    heapq.heappush(min_heap, 30)
    print("Min Heap:", min_heap)  # Output: Min Heap: [10, 20, 30]

    # Remove and return the smallest element using heappop()
    min_element = heapq.heappop(min_heap)
    print(f"Removed {min_element}, Min Heap: {min_heap}")  # Output: Removed 10, Min Heap: [20, 30]

    # Peek the smallest element (root) without removal
    print(f"Minimum Element: {min_heap[0]}")  # Output: Minimum Element: 20

    # Convert a list into a heap using heapq.heapify()
    arr = [12, 7, 9, 15, 10]
    heapq.heapify(arr)
    print("Heapified Array:", arr)  # Output: Heapified Array: [7, 10, 9, 15, 12]


def max_heap_examples():
    # Create an empty max-heap (using negation to simulate max-heap)
    max_heap = []

    # Insert elements using heapq.heappush() (negate values to simulate max-heap)
    heapq.heappush(max_heap, -20)
    heapq.heappush(max_heap, -10)
    heapq.heappush(max_heap, -30)
    print("Max Heap (Simulated):", [-x for x in max_heap])  # Output: Max Heap (Simulated): [30, 20, 10]

    # Remove and return the largest element (simulated max-heap by negating)
    max_element = -heapq.heappop(max_heap)
    print(f"Maximum Element: {max_element}")  # Output: Maximum Element: 30


def priority_queue_example():
    # Create a priority queue where each element is a tuple of (priority, task)
    priority_queue = []
    heapq.heappush(priority_queue, (2, "task1"))
    heapq.heappush(priority_queue, (1, "task2"))
    heapq.heappush(priority_queue, (3, "task3"))

    # Pop the task with the highest priority (lowest priority number)
    priority, task = heapq.heappop(priority_queue)
    print(f"Processing {task} with priority {priority}")  # Output: Processing task2 with priority 1


def kth_largest_element(arr, k):
    # Find the Kth largest element using heap
    heapq.heapify(arr)
    for i in range(len(arr) - k):
        heapq.heappop(arr)
    return heapq.heappop(arr)


def insertion_and_peek_example():
    heap = [10, 20, 30, 40, 50]

    # Insert new element
    heapq.heappush(heap, 5)
    print(f"Heap after insertion: {heap}")  # Output: Heap after insertion: [5, 20, 10, 40, 50, 30]

    # Peek the smallest element
    print(f"Smallest Element (Peek): {heap[0]}")  # Output: Smallest Element (Peek): 5

    # Pop the smallest element
    smallest = heapq.heappop(heap)
    print(f"Removed {smallest}, New Heap: {heap}")  # Output: Removed 5, New Heap: [10, 20, 30, 40, 50]


def heap_pushpop_example():
    heap = [10, 20, 30]
    heapq.heapify(heap)

    # Push a new element and pop the smallest in one step
    element = heapq.heappushpop(heap, 15)
    print(f"Pushed 15, Popped {element}, New Heap: {heap}")  # Output: Pushed 15, Popped 10, New Heap: [15, 20, 30]


def heap_sort_example():
    # Using heap to sort an array
    arr = [12, 7, 9, 15, 10]
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    print("Sorted Array:", sorted_arr)  # Output: Sorted Array: [7, 9, 10, 12, 15]


def main():
    print("=== Min Heap Examples ===")
    min_heap_examples()

    print("\n=== Max Heap (Simulated) Examples ===")
    max_heap_examples()

    print("\n=== Priority Queue Example ===")
    priority_queue_example()

    print("\n=== Kth Largest Element Example ===")
    arr = [12, 3, 5, 7, 19, 1]
    k = 3
    result = kth_largest_element(arr, k)
    print(f"The {k}th largest element is: {result}")  # Output: The 3rd largest element is: 7

    print("\n=== Insertion and Peek Example ===")
    insertion_and_peek_example()

    print("\n=== Heap Pushpop Example ===")
    heap_pushpop_example()

    print("\n=== Heap Sort Example ===")
    heap_sort_example()


if __name__ == "__main__":
    main()
