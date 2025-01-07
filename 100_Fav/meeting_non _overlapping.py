n = int(input())  # Number of time intervals
start_times = []
end_times = []

# Read input times
for _ in range(n):
    start, end = input().split()
    start_hours, start_minutes = map(int, start.split(":"))
    end_hours, end_minutes = map(int, end.split(":"))

    # Convert times to minutes since midnight
    start_times.append(start_hours * 60 + start_minutes)
    end_times.append(end_hours * 60 + end_minutes)

# Sort both start and end times
start_times.sort()
end_times.sort()

max_overlap = 0  # To track the maximum overlap
current_overlap = 0  # To track the current overlap
si = 0  # Pointer for start_times
ei = 0  # Pointer for end_times

# Traverse through both sorted start and end times
while si < n:
    if start_times[si] < end_times[ei]:  # A new meeting is starting before the current one ends
        current_overlap += 1
        si += 1
    else:  # A meeting has ended, reduce overlap
        current_overlap -= 1
        ei += 1

    # Update the maximum overlap
    max_overlap = max(max_overlap, current_overlap)

# Print the result
print(max_overlap)
