def cal(s, si, ei, p, m):
    if p[si][ei]:
        return 0
    if m[si][ei] != -1:
        return m[si][ei]
    ml = float('inf')
    for i in range(si, ei):
        if p[si][i]:
            cs = 1 + cal(s, i + 1, ei, p, m)
            ml = min(ml, cs)
    m[si][ei] = ml
    return ml


s = input().strip()
n = len(s)
p = [[False] * n for _ in range(n)]
for i in range(n):
    p[i][i] = True
for i in range(n - 1):
    if s[i] == s[i + 1]:
        p[i][i + 1] = True
for i in range(3, n + 1):
    for j in range(n - i + 1):
        if s[j] == s[j + i - 1] and p[j + 1][j + i - 2]:
            p[j][j + i - 1] = True
m = [[-1] * n for _ in range(n)]
print(cal(s, 0, n - 1, p, m))


