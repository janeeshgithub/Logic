def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    parent = [-1] * n

    # Compute dp array and parent array
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    # Find the index of the maximum length in dp
    max_length = max(dp)
    max_index = dp.index(max_length)

    # Reconstruct the LIS
    lis = []
    while max_index != -1:
        lis.append(arr[max_index])
        max_index = parent[max_index]

    lis.reverse()
    return max_length, lis

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60]
length, lis = longest_increasing_subsequence(arr)
print("Length of LIS:", length)
print("LIS Elements:", lis)
