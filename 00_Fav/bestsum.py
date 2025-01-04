def bestsum(ts, nums,memo={}):
    if ts in memo:
        return memo[ts]
    if ts==0:
        return []
    if ts<0:
        return None

    sc = None  # Shortest combination
    for i in nums:
        r = ts - i
        rc = bestsum(r, nums)  # Recursive call

        if rc is not None:
            c = rc + [i]  # Create a new combination
            if sc is None or len(c) < len(sc):
                sc = c  # Update if current combination is shorter
    memo[ts]=sc
    return sc

def bestsumdp(ts, num):
    # Initialize the table with None values; the size is ts + 1.
    t = [None] * (ts + 1)
    # Base case: the sum 0 can be achieved with an empty list.
    t[0] = []

    for i in range(ts + 1):
        # Only proceed if there's already a combination that adds up to i
        if t[i] is not None:
            for j in num:
                # Check if adding j goes out of bounds
                if i + j <= ts:
                    # Create a new combination by adding j to the current combination at t[i]
                    combination = t[i] + [j]
                    # Update t[i+j] if it's None or if the new combination is shorter than the existing one
                    if t[i + j] is None or len(combination) < len(t[i + j]):
                        t[i + j] = combination

    return t[ts]  # Return the shortest combination that adds up to ts, or None if not possible

# Example call
print(bestsumdp(30, [10]))  # Expected output: [10, 10, 10] or similar



print(bestsumdp(30,[10]))
# Example call
print(bestsum(16, [2, 3,4,5,6,10]))
