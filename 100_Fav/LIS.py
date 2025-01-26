nums=[4,1,2,3,4,5,6,5,4,3]
dp = [1] * len(nums)
for i in range(len(nums)):
    for j in range(i):
        if nums[j]<nums[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(dp)

def get_longest_increasing_subsequence_length(arr, n, ind, prev_index, dp):
    if ind == n:
        return 0
    if dp[ind][prev_index + 1] != -1:
        return dp[ind][prev_index + 1]
    not_take = 0 + get_longest_increasing_subsequence_length(arr, n, ind + 1, prev_index, dp)
    take = 0
    if prev_index == -1 or arr[ind] > arr[prev_index]:
        take = 1 + get_longest_increasing_subsequence_length(arr, n, ind + 1, ind, dp)
    dp[ind][prev_index + 1] = max(not_take, take)
    return dp[ind][prev_index + 1]
def longest_increasing_subsequence_length(arr):
    n = len(arr)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
    k=get_longest_increasing_subsequence_length(arr, n, 0, -1, dp)
    for i in dp:
        print(i)
    return k



if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]

    result = longest_increasing_subsequence_length(arr)
    print("The length of the longest increasing subsequence is", result)

import bisect
x = [1, 2, 3, 4, 8, 6, 3, 4, 5, 9, 7, 8, 9]
tail = []
for num in x:
    pos = bisect.bisect_left(tail, num)
    if pos == len(tail):
        tail.append(num)
    else:
        tail[pos] = num
print("Length of Longest Increasing Subsequence:", len(tail))


class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        import bisect  # Import bisect for binary search operations

        prev_index = {}  # Dictionary to store the previous index for each element in the subsequence
        dp = []  # List to store pairs of (negative value, index) for the subsequence

        # Iterate over the array in reverse order
        for i in range(N - 1, -1, -1):
            value = -arr[i]  # Negate the value to work with decreasing order
            pos = bisect.bisect_left([x[0] for x in dp], value)  # Find position for the current value in dp
            previous = -1  # Initialize the previous index as -1 (no valid previous index)

            if pos == len(dp):  # If the value is greater than all elements in dp
                if dp:  # Check if dp is not empty
                    previous = dp[-1][1]  # Set previous to the index of the last element in dp
                dp.append((value, i))  # Append the current value and index to dp
            else:  # If the value replaces an element in dp
                if pos > 0:  # Check if there is a valid element before the current position
                    previous = dp[pos - 1][1]  # Set previous to the index of the element before the current position
                dp[pos] = (value, i)  # Replace the element at position pos with the current value and index

            prev_index[i] = previous  # Store the previous index for the current element

        result = []  # List to store the final longest increasing subsequence
        current = dp[-1][1]  # Start from the index of the last element in dp

        # Reconstruct the subsequence by following the previous indices
        while current >= 0:
            result.append(arr[current])  # Append the current element to the result
            current = prev_index[current]  # Move to the previous index

        return result  # Return the longest increasing subsequence

