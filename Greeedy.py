def maximumMeetings(self, start, end):
    # Create a list of [start, end, index] tuples for all meetings
    meetings = []
    for i in range(len(start)):
        meetings.append([start[i], end[i], i])

    # Sort meetings based on their end time
    # If end times are the same, sort by their original order (optional)
    meetings.sort(key=lambda x: x[1])

    # Initialize variables
    count = 0
    last_end_time = 0

    # Iterate through sorted meetings
    for s, e, _ in meetings:
        # If the meeting starts after the last meeting ends
        if s > last_end_time:
            count += 1
            last_end_time = e  # Update the end time to current meeting's end time

    return count

def minimumPlatform(self, arr, dep):
    arr.sort()
    dep.sort()
    a=1
    c=1
    i=1
    j=0
    while i<len(arr) and j<len(dep):
        if arr[i]<=dep[j]:
            c+=1
            i+=1
        else:
            c-=1
            j+=1
        a=max(a,c)
    return a
class Solution:
    def JobSequencing(self, id, deadline, profit):
        # Create a list of jobs, each as a tuple (id, deadline, profit)
        jobs = [(id[i], deadline[i], profit[i]) for i in range(len(id))]

        # Sort jobs in decreasing order of profit
        jobs.sort(key=lambda x: x[2], reverse=True)

        # Find the maximum deadline to know the range of time slots
        max_deadline = max(deadline)

        # Initialize an array to track the available time slots
        time_slots = [-1] * (max_deadline + 1)  # -1 means the time slot is empty

        total_profit = 0
        job_count = 0

        # Iterate over the sorted jobs
        for job in jobs:
            job_id, job_deadline, job_profit = job

            # Find a time slot for the current job, starting from its deadline
            for t in range(job_deadline, 0, -1):
                if time_slots[t] == -1:
                    # If the slot is available, schedule the job
                    time_slots[t] = job_id
                    total_profit += job_profit
                    job_count += 1
                    break

        # Return the total profit and the count of jobs scheduled
        return job_count, total_profit

