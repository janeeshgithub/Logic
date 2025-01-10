
def f(day, last, points, dp):
    if dp[day][last] != -1:
        return dp[day][last]
    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, points[0][i])
        dp[day][last] = maxi
        #print("----")
        return dp[day][last]
    maxi = 0
    for i in range(3):
        if i != last:
            activity = points[day][i] + f(day - 1, i, points, dp)
            maxi = max(maxi, activity)
    dp[day][last] = maxi
    for i in dp:
        print(i)
    return dp[day][last]

def ninjaTraining(n, points):
    # Initialize a DP table to store the computed results.
    dp = [[-1 for j in range(4)] for i in range(n)]
    # Start the recursive function from the last day with no previous activity.
    return f(n - 1, 3, points, dp)

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

