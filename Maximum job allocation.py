x = int(input())
r, c = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(r)]
d = [[0] * c for _ in range(r)]
for i in range(c):
    d[0][i] = m[0][i]
k = m[0][:]
k.sort()
fm = k[-1]
sm = k[-2]
for i in range(1, r):
    for j in range(c):
        if d[i - 1][j] != fm:
            d[i][j] += fm
            d[i][j] += m[i][j]
        else:
            d[i][j] += sm
            d[i][j] += m[i][j]
    jan = d[i][:]
    jan.sort()
    fm = jan[-1]
    sm = jan[-2]
print(fm)

