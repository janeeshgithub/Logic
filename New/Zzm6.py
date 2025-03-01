def egg_drop_recursive(eggs, floors, memo):
    if floors == 0 or floors == 1:
        return floors
    if eggs == 1:  # Base case: Only one egg left
        return floors
    if (eggs, floors) in memo:  # Check memoization
        return memo[(eggs, floors)]

    min_drops = float('inf')
    low, high = 1, floors

    # **Binary search optimization**
    while low <= high:
        mid = (low + high) // 2

        # Egg breaks: check below
        break_case = egg_drop_recursive(eggs - 1, mid - 1, memo)
        # Egg survives: check above
        survive_case = egg_drop_recursive(eggs, floors - mid, memo)

        worst_case = 1 + max(break_case, survive_case)
        min_drops = min(min_drops, worst_case)

        # Move search window
        if break_case > survive_case:
            high = mid - 1  # Search lower floors
        else:
            low = mid + 1  # Search higher floors

    memo[(eggs, floors)] = min_drops  # Store result
    return min_drops


# **Driver Code**
def egg_drop(eggs, floors):
    return egg_drop_recursive(eggs, floors, {})


# **Example Test**
print(egg_drop(2, 10))  # Output: 4
