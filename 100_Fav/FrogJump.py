
def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    prev1=0
    prev2=0
    for ind in range(1, n):
        jumpTwo = float('inf')
        jumpOne =  prev1 + abs(height[ind]-height[ind-1])
        if ind > 1:
            jumpTwo = prev2 + abs(height[ind]-height[ind-2])
        curr = min(jumpOne, jumpTwo)
        prev2,prev1=prev1,curr
    print(curr)

if __name__ == "__main__":
    main()


import sys

# Helper function to solve the problem using dynamic programming
def solve_util(n, height, dp, k):
    # Initialize the first element of the dp array as 0 since no steps are needed to reach the first position
    dp[0] = 0

    # Loop through the elements of the height array
    for i in range(1, n):
        mmSteps = sys.maxsize  # Initialize the minimum steps to a large value
        for j in range(1, k+1):
            if i - j >= 0:
                # Calculate the number of steps required to reach the current position from the previous positions
                jump = dp[i - j] + abs(height[i] - height[i - j])
                mmSteps = min(jump, mmSteps)  # Update the minimum steps
        dp[i] = mmSteps  # Store the minimum steps needed to reach the current position

    return dp[n-1]  # Return the minimum steps needed to reach the last position

# Main function to solve the problem
def solve(n, height, k):
    dp = [-sys.maxsize] * n  # Initialize a dp array with large negative values
    return solve_util(n, height, dp, k)  # Call the helper function

# Entry point of the program
def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    k = 2
    dp = [-sys.maxsize] * n  # Initialize dp array
    result = solve(n, height, k)  # Call the solve function
    print(result)  # Print the result

if __name__ == "__main__":
    main()

