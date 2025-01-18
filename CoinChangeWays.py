# Recursive solution with memoization
def countWaysToMakeChangeUtil(arr, ind, T, dp):
    # Base case: If we have reached the first element in the array.
    if ind == 0:
        return 1 if T % arr[0] == 0 else 0

    # If the result for this state is already calculated, return it.
    if dp[ind][T] != -1:
        return dp[ind][T]

    # Calculate the number of ways when the current element is not taken.
    not_taken = countWaysToMakeChangeUtil(arr, ind - 1, T, dp)

    # Initialize a variable for the number of ways when the current element is taken.
    taken = 0
    if arr[ind] <= T:
        taken = countWaysToMakeChangeUtil(arr, ind, T - arr[ind], dp)

    # Store the total number of ways in the DP table.
    dp[ind][T] = not_taken + taken
    return dp[ind][T]

# Function to count the number of ways to make change for a given target amount using recursion with memoization
def countWaysToMakeChange(arr, n, T):
    # Create a DP table with initial values as -1.
    dp = [[-1 for i in range(T + 1)] for j in range(n)]
    return countWaysToMakeChangeUtil(arr, n - 1, T, dp)

# Dynamic programming solution (Bottom-up)
def countWaysToMakeChangeDP(arr, n, T):
    # Create a DP table to store the number of ways for different target amounts
    dp = [[0 for j in range(T + 1)] for i in range(n)]

    # Initialize the base condition for the first element in the array
    for i in range(T + 1):
        if i % arr[0] == 0:
            dp[0][i] = 1
        # Else condition is automatically fulfilled, as dp array is initialized to zero

    # Iterate through the array elements and target amounts
    for ind in range(1, n):
        for target in range(T + 1):
            # Calculate the number of ways when the current element is not taken
            notTaken = dp[ind - 1][target]

            # Initialize a variable for the number of ways when the current element is taken
            taken = 0
            if arr[ind] <= target:
                taken = dp[ind][target - arr[ind]]

            # Store the total number of ways in the DP table
            dp[ind][target] = notTaken + taken

    # Return the total number of ways for the given target amount
    return dp[n - 1][T]

# Optimized space solution (Space-efficient DP)
def countWaysToMakeChangeSpace(arr, n, T):
    # Initialize a list 'prev' to store the number of ways for different target amounts
    prev = [0] * (T + 1)

    # Initialize the base condition for the first element in the array
    for i in range(T + 1):
        if i % arr[0] == 0:
            prev[i] = 1
    # Else condition is automatically fulfilled, as 'prev' is initialized to zeros.

    # Iterate through the array elements and target amounts
    for ind in range(1, n):
        # Initialize a list 'cur' to store the number of ways for the current element
        cur = [0] * (T + 1)
        for target in range(T + 1):
            # Calculate the number of ways when the current element is not taken
            notTaken = prev[target]

            # Initialize a variable for the number of ways when the current element is taken
            taken = 0
            if arr[ind] <= target:
                taken = cur[target - arr[ind]]

            # Store the total number of ways in 'cur'
            cur[target] = notTaken + taken

        # Update 'prev' with the results from 'cur' for the next iteration
        prev = cur

    # Return the total number of ways for the given target amount
    return prev[T]

# Main function to demonstrate all solutions
def main():
    arr = [1, 2, 3]
    target = 4
    n = len(arr)

    # Recursive with memoization solution
    print("Recursive with memoization:")
    print("The total number of ways is", countWaysToMakeChange(arr, n, target))

    # Dynamic Programming (Bottom-up) solution
    print("\nDynamic Programming (Bottom-up):")
    print("The total number of ways is", countWaysToMakeChangeDP(arr, n, target))

    # Optimized space solution (Space-efficient DP)
    print("\nOptimized Space Solution (Space-efficient DP):")
    print("The total number of ways is", countWaysToMakeChangeSpace(arr, n, target))

if __name__ == "__main__":
    main()
