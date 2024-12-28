def longest_increasing_subsequence_length(arr):
    n = len(arr)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                print(dp)
        print("\\")

    print("DP array:", dp)

    return max(dp)


if __name__ == "__main__":
    arr = [1,2,3,4,5]

    result = longest_increasing_subsequence_length(arr)
    print("The length of the longest increasing subsequence is", result)
