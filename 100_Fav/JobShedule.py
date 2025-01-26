def jobScheduling(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    # Find the maximum deadline
    maxi = max(jobs, key=lambda x: x[1])[1]
    # Initialize slot array to keep track of filled slots
    slot = [-1] * (maxi + 1)
    countJobs = 0
    jobProfit = 0

    # Schedule jobs
    for i in range(len(jobs)):
        for j in range(jobs[i][1], 0, -1):  # Loop through available slots for the current job
            if slot[j] == -1:  # If the slot is available
                slot[j] = i  # Mark the slot as filled
                countJobs += 1  # Increment job count
                jobProfit += jobs[i][2]  # Add profit of the scheduled job
                break

    return countJobs, jobProfit


if __name__ == "__main__":
    # Array of tuples: (Job ID, Deadline, Profit)
    jobs = [(1, 4, 20), (2, 1, 10), (3, 2, 40), (4, 2, 30)]

    count, profit = jobScheduling(jobs)
    print(count, profit)
