
def solveNQueens(n):
    def back(r, c, a, b, grid):
        if n == r:
            ans.append(["".join(i) for i in grid])
            return
        for i in range(n):
            if i not in c and (r - i) not in a and (r + i) not in b:
                grid[r][i] = 'Q'
                c.add(i)
                a.add(r - i)
                b.add(r + i)
                back(r + 1, c, a, b, grid)
                grid[r][i] = '0'
                c.remove(i)
                a.remove(r - i)
                b.remove(r + i)

    ans = []
    grid = [['0'] * n for _ in range(n)]
    back(0, set(), set(), set(), grid)
    return ans,len(ans)
t,l=solveNQueens(5)
for i in t:
    for j in t:
        print(j)

