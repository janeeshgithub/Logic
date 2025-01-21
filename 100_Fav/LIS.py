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
