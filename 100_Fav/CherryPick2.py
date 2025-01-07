ROWS, COLS = map(int, input().split())
g = []
for _ in range(ROWS):
    g.append(list(map(int, input().split())))


c={}
def dfs(r,c1,c2):
    if (r,c1,c2) in c:
        return c[(r,c1,c2)]
    if c1==c2 or min(c1,c2)<0 or max(c1,c2)==COLS:
        return 0
    if r==ROWS-1:
        return g[r][c1]+g[r][c2]
    res=0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            res=max(res,dfs(r+1,c1+x,c2+y))
    c[(r,c1,c2)]=res+g[r][c1]+g[r][c2]
    return c[(r,c1,c2)]
print(dfs(0,0,COLS-1))


dp = [[0] * COLS for _ in range(COLS)]

for r in reversed(range(ROWS)):
    curdp = [[0] * COLS for _ in range(COLS)]
    for c1 in range(COLS - 1):
        for c2 in range(c1 + 1, COLS):
            mc = float('-inf')
            che = g[r][c1] + g[r][c2]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    nc1, nc2 = c1 + x, c2 + y
                    if 0 <= nc1 < COLS and 0 <= nc2 < COLS:
                        mc = max(mc, che + dp[nc1][nc2])
            curdp[c1][c2] = mc
    dp = curdp
print(dp[0][-1])