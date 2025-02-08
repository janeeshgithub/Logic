from collections import Counter


def max_fence_length(arr):
    # Count frequency of each plank length
    freq = Counter(arr)
    max_fence = 0

    # Check pairs of planks and their sum
    for num1 in freq:
        for num2 in freq:
            if num1 == num2:  # If the two numbers are the same, they cannot be paired
                continue

            target_sum = num1 + num2

            if target_sum in freq:
                # We can form a fence by using num1, num2, and target_sum
                max_fence = max(max_fence, 3)  # As we use 3 planks in this case

    # Consider the case where we just use a single plank
    for num in freq:
        max_fence = max(max_fence, 1)  # Single plank can form a fence

    return max_fence


# Example usage
arr1 = [1, 3, 2, 5, 2, 5, 4, 2, 1]
arr2 = [2, 3, 7]
print(max_fence_length(arr1))  # Output: 3
print(max_fence_length(arr2))  # Output: 0
