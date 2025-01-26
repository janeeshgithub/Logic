# from bisect import *
#
# class Solution:
#     def longestIncreasingSubsequence(self, N, arr):
#         prev_index = {}
#         dp = []
#
#         for i in range(N - 1, -1, -1):
#             value = -arr[i]
#             pos = bisect_left([x[0] for x in dp], value)
#             previous = -1
#             if pos == len(dp):
#                 if dp:
#                     previous = dp[-1][1]
#                 dp.append((value, i))
#             else:
#                 if pos > 0:
#                     previous = dp[pos - 1][1]
#                 dp[pos] = (value, i)
#
#             prev_index[i] = previous
#
#         result = []
#         current = dp[-1][1]
#
#         while current >= 0:
#             result.append(arr[current])
#             current = prev_index[current]
#         for i in dp:
#             print(i)
#         return result
#
# # Example test case
# if __name__ == "__main__":
#     # Example input
#     N = 8
#     arr = [10, 9, 2, 5, 3, 7, 101, 18]
#
#     # Create an instance of the Solution class
#     solution = Solution()
#
#     # Find the longest increasing subsequence
#     result = solution.longestIncreasingSubsequence(N, arr)
#
#     # Print the result
#     print("Array:", arr)
#     print("Longest Increasing Subsequence:", result)


def rec(arr,n,i,pi,dp):
    if i==n:
        return 0
    if dp[i][pi+1]!=-1:
        return dp[i][pi+1]
    nt=0+rec(arr,n,i+1,pi,dp)
    t=0
    if pi==-1 or arr[i]>arr[pi]:
        t=1+rec(arr,n,i+1,i,dp)
    dp[i][pi+1]=max(t,nt)
    return dp[i][pi+1]
arr=[1,2,3,4,3,2,1,5,6,3,2]
n = len(arr)
dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
rec(arr, n, 0, -1, dp)
for i in dp:
    print(i)

