def count_good_pairs(n, k):
    """
    Calculate the number of good pairs (x,y) where:
    0 <= x <= n
    x <= y <= n
    y - x is divisible by k

    Args:
        n: Upper bound for x and y
        k: The divisibility factor

    Returns:
        Number of good pairs modulo 10^9 + 7
    """
    MOD = 10 ** 9 + 7

    # For each x from 0 to n:
    # Number of valid y values = floor((n-x)/k) + 1
    # Sum can be calculated using arithmetic progression

    # Calculate complete groups
    complete_groups = n // k

    # Calculate the sum in O(1) using mathematical formula
    total_pairs = 0

    # Handle complete groups
    if complete_groups > 0:
        # For each complete group, calculate contribution
        # Using arithmetic sequence sum formula: n*(a1 + an)/2
        group_count = complete_groups * k
        first_term = complete_groups
        last_term = 1
        groups_sum = (group_count * (first_term + last_term)) // 2
        total_pairs = (total_pairs + groups_sum) % MOD

    # Handle remaining elements
    remaining = n % k
    if remaining > 0:
        remaining_count = remaining + 1
        pairs_in_last = (n - remaining) // k + 1
        total_pairs = (total_pairs + remaining_count * pairs_in_last) % MOD

    print(total_pairs)
    return total_pairs
count_good_pairs(2, 2)