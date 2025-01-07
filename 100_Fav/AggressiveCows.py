def check(stalls, k, dist):
    # Function to check if we can place k cows with at least `dist` distance
    cnt = 1  # First cow is placed at the first stall
    prev = stalls[0]  # Last placed cow's position
    for i in range(1, len(stalls)):
        if stalls[i] - prev >= dist:  # Can place next cow here
            cnt += 1
            prev = stalls[i]
            if cnt == k:  # Placed all cows2
                return True
    return False

def aggressiveCows(stalls, k):
    stalls.sort()  # Sort stall positions
    lo, hi = 1, stalls[-1] - stalls[0]  # Possible range of distances
    res = 0  # Store the best result

    while lo <= hi:
        mid = lo + (hi - lo) // 2  # Midpoint of current range
        if check(stalls, k, mid):  # Check if mid is a valid distance
            res = mid  # Update result
            lo = mid + 1  # Try for a larger minimum distance
        else:
            hi = mid - 1  # Try for a smaller minimum distance

    return res
stalls = [1, 2, 8, 4, 9]
k = 3
print(aggressiveCows(stalls, k))  # Output: 4
