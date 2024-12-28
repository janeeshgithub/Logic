def minIntervalsToRemove(intervals):
    if not intervals:
        return 0

    # Step 1: Sort the intervals by start times and end times
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])

    # Step 2: Initialize variables
    n = len(intervals)
    start_pointer = 0  # Pointer for start times
    end_pointer = 0  # Pointer for end times
    active_intervals = 0  # Active intervals (number of platforms required)
    max_active_intervals = 0  # Maximum number of active intervals at any point

    # Step 3: Sweep through the intervals using the two pointers
    while start_pointer < n:
        if starts[start_pointer] < ends[end_pointer]:
            active_intervals += 1  # A new interval is starting
            max_active_intervals = max(max_active_intervals, active_intervals)
            start_pointer += 1
        else:
            active_intervals -= 1  # An interval is ending
            end_pointer += 1

    # Step 4: The number of intervals to remove is the total intervals minus the max overlaps
    return n - max_active_intervals


# Read input
n = int(input())  # Number of intervals
intervals = []

# Reading the intervals
for _ in range(n):
    intervals.append(list(map(int, input().split())))

# Get the result
result = minIntervalsToRemove(intervals)
print(result)
