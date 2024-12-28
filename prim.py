x, y = map(int, input().split())
m = [[-1] * (x) for _ in range(x)]
v = [0] * x
mcs, mcd, = -1, -1
mc = float('inf')
for _ in range(y):
    a, b, c = map(int, input().split())
    m[a][b] = m[b][a] = c
    if mc > c:
        mc = c
        mcs = a
        mcd = b
tmc = mc
rc = x - 2
v[mcs] = v[mcd] = 1
while (rc > 0):
    mc = float('inf')
    for i in range(x):
        if v[i] == 1:
            for j in range(x):
                if i == j or v[j] or m[i][j] == -1:
                    continue
                if m[i][j] < mc:
                    mc = m[i][j]
                    mcd = j
    tmc += mc
    v[mcd] = 1
    rc -= 1
print(tmc)
