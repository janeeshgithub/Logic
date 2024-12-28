def jan(n, r, m, sw, nw, b):
    if r == n:
        return True
    if b[r]:
        return jan(n, r + 1, m, sw, nw, b)
    for i in range(n):
        if not sw[i - r + n - 1] and not nw[r + i]:
            m[r][i] = 1
            b[r] = True
            sw[i - r + n - 1] = True
            nw[i + r] = True
            if jan(n, r + 1, m, sw, nw, b):
                return True
            else:
                m[r][i] = 0
                b[r] = False
                sw[i - r + n - 1] = False
                nw[i + r] = False

    return False


n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
sw = [False] * (2 * n - 1)
nw = [False] * (2 * n - 1)
b = [False] * n
for i in range(n):
    for j in range(n):
        if m[i][j] == 1:
            b[i] = True
            nw[i + j] = True
            sw[n - i + j - 1] = True
if jan(n, 0, m, sw, nw, b):
    for i in m:
        print(*i)
else:
    print("NotPossible")
