from collections import deque

def jan(m, n, N):
    ns = []
    r, c = n // N, n % N
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        while 0 <= nr < N and 0 <= nc < N and m[nr][nc]:
            ns.append(nr * N + nc)
            nr, nc = nr + dr, nc + dc
    return ns

x = int(input())
m = [list(map(int, input().split())) for _ in range(x)]
s1, s2 = map(int, input().split())
d1, d2 = map(int, input().split())
s, d = s1 * x + s2, d1 * x + d2
v, st = [0] * (x * x), [-1] * (x * x)
q = deque([s])
v[s], st[s] = 1, 0
while q:
    n = q.popleft()
    for i in jan(m, n, x):
        if not v[i]:
            v[i], st[i] = 1, st[n] + 1
            if i == d:
                print(st[i])
                exit()
            q.append(i)

print("No path found")

from collections import deque

x = int(input())
m = [list(map(int, input().split())) for _ in range(x)]
s1, s2 = map(int, input().split())
d1, d2 = map(int, input().split())
s, d = s1 * x + s2, d1 * x + d2

v, st = [0] * (x * x), [-1] * (x * x)
q = deque([s])
v[s], st[s] = 1, 0

while q:
    n = q.popleft()
    r, c = n // x, n % x
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        while 0 <= nr < x and 0 <= nc < x and m[nr][nc]:
            idx = nr * x + nc
            if not v[idx]:
                v[idx], st[idx] = 1, st[n] + 1
                if idx == d:
                    print(st[idx])
                    exit()
                q.append(idx)
            nr, nc = nr + dr, nc + dc

print("No path found")
