# Input grid dimensions and grid
from collections import deque
r, c = 5,5
m = [[0]*c for _ in range(r)]
m[0][0]=1
m[0][4]=1
m[4][0]=1
m[1][1]=1
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
v1 = [[False] * c for _ in range(r)]
v2 = [[False] * c for _ in range(r)]
# Recursive DFS function
def dfs(x, y):
    v1[x][y] = True
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and not v1[nx][ny] and m[nx][ny] == 1:
            dfs(nx, ny)

def bfs(x,y):
    q=deque([(x,y)])
    while q:
        x,y=q.popleft()
        v2[x][y]=True
        for dr,dc in dir:
            nx,ny=dr+x,dc+y
            if 0<=nx<r and 0<=ny<c and not v2[nx][y] and m[nx][ny]==1:
                v2[x][y]=True
                q.append((nx,ny))


# Count islands
island_countdfs = 0

for i in range(r):
    for j in range(c):
        if m[i][j] == 1 and not v1[i][j]:  # Found an unvisited land cell
             # Start DFS to mark the entire island
            dfs(i,j)
            island_countdfs += 1

print("Number of islands:", island_countdfs)

island_countbfs=0
for i in range(r):
    for j in range(c):
        if m[i][j] == 1 and not v2[i][j]:
            bfs(i,j)
            island_countbfs+=1

print("Number of islands:", island_countbfs)
