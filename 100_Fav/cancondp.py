def cancondp(ts, wb):
    t = [False] * (len(ts) + 1)
    t[0] = True
    for i in range(len(ts) + 1):
        if t[i] == True:
            for j in wb:
                if ts[i:i+len(j)] == j and i + len(j) <= len(ts):
                    t[i + len(j)] = True
    return t[-1]

def countcons(ts,wb):
    t=[0]*(len(ts)+1)
    t[0]=1
    for i in range(len(ts)+1):
        if t[i]!=0:
            for j in wb:
                if ts[i:i+len(j)]==j and i+len(j)<=len(ts):
                    t[i+len(j)]+=1
    return t[-1]

def allConstruct(t, wb):
    dp = [[] for _ in range(len(t) + 1)]  # Create an empty list for each position in the string
    dp[len(t)] = [[]]  # Base case: there's one way to construct an empty string (by doing nothing)

    for i in range(len(t) - 1, -1, -1):  # Start from the end of the string
        for word in wb:
            if t[i:i+len(word)] == word:  # Check if the word is a prefix of t[i:]
                # For every way of constructing the suffix (dp[i + len(word)]), prepend `word` to it
                for way in dp[i + len(word)]:
                    dp[i].append([word] + way)

    return dp[0]  # The result for the whole string is stored in dp[0]

# Test
print(allConstruct("purple", ["pur", "p", "ur", "le", "purp", "e"]))



print(cancondp("jan", ["j", "an"]))
print(countcons("jan", ["j", "an","ja","n"])) # Output should be True
