#RECURSION
"""
def rec(val, wt, ind, W, dp):
    if ind == 0:
        if wt[0] <= W:
            return val[0]
        else:
            return 0
    if dp[ind][W] != -1:
        return dp[ind][W]
    not_taken = 0 + rec(val, wt, ind - 1, W, dp)
    taken = 0
    if wt[ind] <= W:
        taken = val[ind] + rec(val, wt, ind - 1, W - wt[ind], dp)
    dp[ind][W] = max(not_taken, taken)
    return dp[ind][W]

val = [90, 99, 100]
wt = [4, 2, 3]
W = 4
dp = [[-1] * (W + 1) for _ in range(len(val))]
result = rec(val, wt, len(val) - 1, W, dp)
print(result)
for i in dp:
    print(i)
"""
#DYNAMIC Programming
# DYNAMIC PROGRAMMING
val = [90, 99, 100]
wt = [4, 2, 3,5]
W = 4
n = len(val)
dp = [[0] * (W + 1) for _ in range(n)]
for cap in range(n):
    #if wt[0] <= cap:
    dp[cap][0] = val[cap]

for i in dp:
    print(i)

for ind in range(1, n):
    for cap in range(W + 1):
        # Not taking the current item
        not_taken = dp[ind - 1][cap]

        # Taking the current item (if it fits in the remaining capacity)
        taken = 0
        if wt[ind] <= cap:
            taken = val[ind] + dp[ind - 1][cap - wt[ind]]

        # Store the maximum of both choices
        dp[ind][cap] = max(not_taken, taken)

# Result is the maximum value for the full capacity
result = dp[n - 1][W]
print("Result (Dynamic Programming):", result)

# Print the DP table
for row in dp:
    print(row)
