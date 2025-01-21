# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
#
#         q = deque([0])
#         seen = [False] * (amount + 1)
#         seen[0] = True
#         res = 0
#
#         while q:
#             res += 1
#             for _ in range(len(q)):
#                 cur = q.popleft()
#                 for coin in coins:
#                     nxt = cur + coin
#                     if nxt == amount:
#                         return res
#                     if nxt > amount or seen[nxt]:
#                         continue
#                     seen[nxt] = True
#                     q.append(nxt)
#
#         return -1
#
#

coins=[1,2,2,4,5,6]
Sum=11
n=len(coins)
d=[0]*(Sum+1)
d[0]=1
for i in coins:
    for j in range(i,Sum+1):
        d[j]+=d[j-i]
print(d)

coins2=[1,2,5]
dp=[float('inf')]*(Sum+1)
dp[0]=1
for i in coins2:
    for j in range(i,Sum+1):
        dp[j]=min(dp[j],dp[j-i]+1)
print(dp)

