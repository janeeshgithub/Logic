def isSafe(N,g,n,colarr,col):
    for i in range(N):
        if colarr[i]==col and i!=n and g[i][n]==1:
            return False
    return True

def solve(color,N,g,n,m):
    if n==N:
        return True
    for i in range(1,m+1):
        if isSafe(N,g,n,color,i):
            color[n]=i
            if solve(color, N, g, n+1, m):
                return True
            color[n]=-1
    return False

N=4
m=2
g = [[0 for i in range(10)] for j in range(10)]
g[0][1]=1
g[1][2]=1
g[2][0]=1
c=[-1]*N
print("Y" if solve(c,N,g,0,m) else "N")