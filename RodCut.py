# 1. Recursion
def cutRodRecursive(price):
    def help(i, W):
        # Base case
        if i == len(price) or W <= 0:
            return 0
        # If the current rod length cannot be included
        if i + 1 > W:
            return help(i + 1, W)
        # Include or exclude the current piece
        include = price[i] + help(i, W - (i + 1))
        exclude = help(i + 1, W)
        return max(include, exclude)
    return help(0, len(price))

# 2. Memoization
def cutRodMemo(price):
    n = len(price)

    def help(i, W, mem):
        # Base case
        if i == n or W <= 0:
            return 0

        # Check memo
        if (i, W) in mem:
            return mem[(i, W)]

        # If the current rod length cannot be included
        if i + 1 > W:
            mem[(i, W)] = help(i + 1, W, mem)
            return mem[(i, W)]

        # Include or exclude the current piece
        include = price[i] + help(i, W - (i + 1), mem)
        exclude = help(i + 1, W, mem)

        # Store in memo
        mem[(i, W)] = max(include, exclude)
        return mem[(i, W)]

    return help(0, n, {})

# 3. Dynamic Programming (Iterative)
def cutRodDP(price):
    n = len(price)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        mv = -1
        for j in range(i):
            mv = max(mv, price[j] + dp[i - j - 1])
        dp[i] = mv

    return dp[n]


price = [1, 5, 8, 9, 10, 17, 17, 20]
print("Recursive:", cutRodRecursive(price))  # Output: 22
print("Memoization:", cutRodMemo(price))  # Output: 22
print("Dynamic Programming:", cutRodDP(price))  # Output: 22
