from collections import deque

# Input processing
x = int(input())  # Grid size
m = [list(map(int, input().strip())) for _ in range(x)]  # The grid (matrix)
a = list(map(int, input().split()))  # Start and target positions

# Create a visited matrix initialized to False
v = [[False] * x for _ in range(x)]

# Directions for movement (right, down, left, up)
dir = ['R', 'D', 'L', 'U']
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

# Initialize the queue with the start position, and a direction count
q = deque([(a[0], a[1], -1, 0)])  # (x, y, last_direction, direction_changes)
v[a[0]][a[1]] = True

# To keep track of parent cells for path reconstruction
par = {(a[0], a[1]): None}

# Target position
t = (a[2], a[3])

# BFS traversal
while q:
    i, j, ld, dirc = q.popleft()

    # If we reach the target
    if (i, j) == t:
        # Reconstruct the path
        p = []
        while (i, j) is not None:
            p.append((i, j))
            i, j = par[(i, j)]

        p.reverse()  # Reverse the path to start from the beginning
        print("Shortest Path:", p)
        print("Minimum Direction Changes:", dirc)
        exit()

    # Explore neighbors (right, down, left, up)
    for k, (dr, dc) in enumerate(d):
        nr, nc = i + dr, j + dc
        if 0 <= nr < x and 0 <= nc < x and not v[nr][nc] and m[nr][nc] == 1:
            v[nr][nc] = True
            par[(nr, nc)] = (i, j)  # Set parent for path reconstruction
            ndc = dirc
            # Check if the direction has changed
            if ld != -1 and dir[ld] != dir[k]:
                ndc += 1
            q.append((nr, nc, k, ndc))

# If no path is found, print -1
print(-1)
