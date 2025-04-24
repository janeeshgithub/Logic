m=9
def puz(a):
    for i in range(m):
        for j in range(m):
            print(a[i][j],end=" ")
        print()

def solve(grid,r,c,n):
    for x in range(9):
        if grid[r][x]==n:
            return False
    for x in range(9):
        if grid[x][c]==n:
            return False
    sr=r-r%3
    sc=c-c%3
    for i in range(3):
        for j in range(3):
            if grid[i+sr][j+sc]==n:
                return False
    return True
def sud(grid,r,c):
    if r==m-1 and c==m:
        return True
    if c==m:
        r+=1
        c=0
    if grid[r][c]>0:
        return sud(grid,r,c+1)
    for num in range(1,m+1,1):
        if solve(grid,r,c,n):
            grid[r][c]=num
            if sud(grid,r,c+1):
                return True
            grid[r][c]=0
    return False


