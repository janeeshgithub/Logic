
def ninjaTraining(n, points):
    # Initialize a DP table with dimensions (n x 4) to store the maximum points.
    dp = [[0 for j in range(4)] for i in range(n)]

    # Initialize the DP table for day 0 with base cases.
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]))

    # Loop through the days starting from the second day.
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0  # Initialize the maximum points for the current day and last activity.
            for task in range(3):
                if task != last:
                    # Calculate the total points for the current day's activity and the previous day's maximum points.
                    activity = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], activity)

    # Return the maximum points achievable after the last day with any activity.
    return dp[n - 1][3]

def main():
    # Define the points matrix for each day.
    points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]
    n = len(points)  # Get the number of days.
    # Call the ninjaTraining function to find the maximum points.
    print(ninjaTraining(n, points))

if __name__ == '__main__':
    main()


def ninjaTraining(n, points):
    # Initialize a list 'prev' to store the maximum points for each possible last activity on the previous day.
    prev = [0] * 4

    # Initialize 'prev' with the maximum points for the first day's activities.
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]))

    # Loop through the days starting from the second day.
    for day in range(1, n):
        # Initialize a temporary list 'temp' to store the maximum points for each possible last activity on the current day.
        temp = [0] * 4

        for last in range(4):
            # Initialize 'temp' for the current last activity.
            temp[last] = 0

            for task in range(3):
                if task != last:
                    # Calculate the total points for the current day's activity and the previous day's maximum points.
                    activity = points[day][task] + prev[task]
                    # Update 'temp' with the maximum points for the current last activity.
                    temp[last] = max(temp[last], activity)

        # Update 'prev' with 'temp' for the next iteration.
        prev = temp

    # Return the maximum points achievable after the last day with any activity.
    return prev[3]

def main():
    # Define the points matrix for each day.
    points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]
    n = len(points)  # Get the number of days.
    # Call the ninjaTraining function to find and print the maximum points.
    print(ninjaTraining(n, points))

if __name__ == '__main__':
    main()

