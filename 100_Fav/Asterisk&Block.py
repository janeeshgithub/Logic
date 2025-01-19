from functools import lru_cache


def jan(s):
    sc = [0] * len(s)
    pi = []
    ct = 0
    for i, j in enumerate(s):
        if j == '*':
            ct += 1
        elif j == '|':
            pi.append(i)
        sc[i] = ct
    return sc, pi


@lru_cache(None)
def har(sc, pi, x, y):
    l = next((i for i in pi if i >= x), None)
    r = next((i for i in reversed(pi) if i <= y), None)
    if l is None or r is None or l >= r:
        return 0
    return sc[r] - sc[l]


s = input().strip()
n = int(input())
sc, pi = jan(s)
# print(sc)
# print(pi)
for _ in range(n):
    x, y = map(int, input().split())
    print(har(tuple(sc), tuple(pi), x - 1, y - 1))


def preprocess(s):
    # Preprocess the string to calculate cumulative '*' counts and indices of '|'
    n = len(s)
    sc = [0] * n  # Cumulative '*' counts
    pi = []  # Indices of '|'

    ct = 0
    for i, ch in enumerate(s):
        if ch == '*':
            ct += 1
        elif ch == '|':
            pi.append(i)
        sc[i] = ct
    return sc, pi


def query(x, y, sc, pi):
    # Find the first '|' after or at x and the last '|' before or at y
    l = -1
    r = -1

    # Find left closest '|' >= x
    for i in pi:
        if i >= x:
            l = i
            break

    # Find right closest '|' <= y
    for i in reversed(pi):
        if i <= y:
            r = i
            break

    # If valid left and right pipes found and left is before right, calculate the result
    if l != -1 and r != -1 and l < r:
        return sc[r] - sc[l]
    return 0


# Input
s = input().strip()  # Input string
n = int(input())  # Number of queries

# Preprocess the string
sc, pi = preprocess(s)

# Process each query
for _ in range(n):
    x, y = map(int, input().split())
    print(query(x - 1, y - 1, sc, pi))  # Adjust for 0-based indexing
