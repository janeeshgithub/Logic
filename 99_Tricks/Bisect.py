import bisect


def bisect_examples():
    # Sample sorted list
    numbers = [1, 2, 4, 4, 5, 6, 8, 10]

    # Using bisect_left
    pos_left = bisect.bisect_left(numbers, 4)
    print(f'Index for 4 using bisect_left: {pos_left}')  # Output: 2
    # Explanation: The first 4 is at index 2, so bisect_left inserts 4 at index 2.

    # Using bisect_right
    pos_right = bisect.bisect_right(numbers, 4)
    print(f'Index for 4 using bisect_right: {pos_right}')  # Output: 4
    # Explanation: The second 4 is at index 3, so bisect_right inserts 4 at index 4.


def insertion_examples():
    # Using insort_left
    numbers = [1, 2, 4, 4, 5, 6, 8, 10]
    bisect.insort_left(numbers, 7)
    print(f'List after insort_left(7): {numbers}')  # Output: [1, 2, 4, 4, 5, 6, 7, 8, 10]

    # Using insort_right
    bisect.insort_right(numbers, 4)
    print(f'List after insort_right(4): {numbers}')  # Output: [1, 2, 4, 4, 4, 5, 6, 7, 8, 10]


def maintain_sorted_order():
    # Sorted list of scores
    scores = [10, 20, 30, 40, 50]

    # We are inserting a new score (25)
    bisect.insort_left(scores, 25)

    # Now the list is sorted
    print("Sorted scores:", scores)  # Output: [10, 20, 25, 30, 40, 50]


def insertion_position_example():
    scores = [50, 60, 70, 85, 90]

    new_score = 80

    # Find the position to insert 80
    position = bisect.bisect_left(scores, new_score)
    print(f'Insert {new_score} at index {position}')

    # Insert the new score using the bisect position
    bisect.insort_left(scores, new_score)
    print(f'Updated scores: {scores}')  # Output: [50, 60, 70, 80, 85, 90]


if __name__ == "__main__":
    print("=== bisect_examples ===")
    bisect_examples()
    print("\n=== insertion_examples ===")
    insertion_examples()
    print("\n=== maintain_sorted_order ===")
    maintain_sorted_order()
    print("\n=== insertion_position_example ===")
    insertion_position_example()
