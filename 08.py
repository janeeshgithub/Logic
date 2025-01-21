def min_subsequence_for_max_or(arr):
    """
    Find the minimum length subsequence whose bitwise OR equals the maximum possible OR value,
    and return the subsequence along with its length.

    Args:
        arr: List of positive integers
    Returns:
        Tuple of (length, subsequence)
    """
    if not arr:
        return 0, []

    # Calculate the maximum possible bitwise OR value
    max_or = 0
    for num in arr:
        max_or |= num

    # Keep track of remaining required bits and the numbers contributing to max OR
    remaining_bits = max_or
    bits_needed = []

    # Sort array in descending order to prefer numbers with multiple bits set
    for num in sorted(arr, reverse=True):
        # Check if this number contributes any new required bits
        unique_contribution = num & remaining_bits
        if unique_contribution:
            bits_needed.append(num)
            # Remove the bits this number contributes
            remaining_bits &= ~unique_contribution

        # If all required bits are collected, stop
        if remaining_bits == 0:
            break

    return len(bits_needed), bits_needed


# Example usage
arr = [1, 2, 3, 4, 5]
length, subsequence = min_subsequence_for_max_or(arr)
print(f"Minimum subsequence length: {length}")
print(f"Subsequence: {subsequence}")
