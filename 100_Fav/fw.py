n,x=map(int,input().split())
m=[[float('inf')]*n for _ in range(n)]
for i in range(n):
    m[i][i]=0
for _ in range(x):
    r,c,w=map(int,input().split())
    m[r-1][c-1]=w
for k in range(n):
    for i in range(n):
        for j in range(n):
            m[i][j]=min(m[i][j],m[i][k]+m[k][j])
print(*m[0][1:])