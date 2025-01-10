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



