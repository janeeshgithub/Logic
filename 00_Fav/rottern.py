from collections import deque
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
day=0
q=deque()
d=[(0,1),(0,-1),(1,0),(-1,0)]
h=0
for i in range(r):
    for j in range(c):
        if m[i][j]==1:
            h+=1
        if m[i][j]==2:
            q.append(i*c+j)
q.append(-1)
while q:
    n=q.popleft()
    if n==-1:
        if q:
            day+=1
            q.append(-1)
        continue
    i,j=n//c,n%c
    for x,y in d:
        nr,nc=i+x,j+y
        if 0<=nr<r and 0<=nc<c and m[nr][nc]==1:
            h-=1
            q.append(c*nr+nc)
            m[nr][nc]=2
print(day if h==0 else -1)