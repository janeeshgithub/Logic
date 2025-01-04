r, c = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(r)]

# Initialize two path matrices
p1 = [[0] * c for _ in range(r)]  # Top-left to bottom-right
p2 = [[0] * c for _ in range(r)]  # Bottom-left to top-right

# Top-left to bottom-right (p1)
p1[0][0] = m[0][0]
for i in range(1, r):
    if m[i][0] == 1:
        p1[i][0] = p1[i - 1][0]
for i in range(1, c):
    if m[0][i] == 1:
        p1[0][i] = p1[0][i - 1]
for i in range(1, r):
    for j in range(1, c):
        if m[i][j] == 1:
            p1[i][j] = p1[i - 1][j] + p1[i][j - 1]

# Bottom-left to top-right (p2)
p2[r - 1][0] = m[r - 1][0]
for i in range(r - 2, -1, -1):
    if m[i][0] == 1:
        p2[i][0] = p2[i + 1][0]
for i in range(1, c):
    if m[r - 1][i] == 1:
        p2[r - 1][i] = p2[r - 1][i - 1]
for i in range(r - 2, -1, -1):
    for j in range(1, c):
        if m[i][j] == 1:
            p2[i][j] = p2[i + 1][j] + p2[i][j - 1]

# Print both matrices
print("Top-left to bottom-right (p1):")
for row in p1:
    print(row)

print("\nBottom-left to top-right (p2):")
for row in p2:
    print(row)
