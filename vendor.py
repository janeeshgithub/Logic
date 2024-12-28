n,k=map(int,input().split())
t=[]
for i in range(k):
    a,b=map(int,input().split())
    t.append([a,b])
t.sort()
d=[[0]*(n+1) for _ in range(k+1)]
for i in range(1,k+1):
    a,b=t[i-1]
    for j in range(1,n+1):
        d[i][j]=max(d[i-1][j],d[i-1][j-a]+b if j>=a else 0)
print(d[-1][-1])