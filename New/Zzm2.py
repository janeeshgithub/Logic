# m, n = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(m)]
# dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
# dp[1][1] = matrix[0][0]
# for i in range(1, m + 1):
#     for j in range(1, n + 1):
#         if i == 1 and j == 1:
#             continue
#         dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i - 1][j - 1]
# print(dp[m][n])

import heapq
def minPathSumBFS(grid):
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = [(grid[0][0], 0, 0)]
    visited = set()
    parent = {}
    min_cost = [[float('inf')] * n for _ in range(m)]
    min_cost[0][0] = grid[0][0]
    while pq:
        cost, i, j = heapq.heappop(pq)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if i == m - 1 and j == n - 1:
            path = []
            while (i, j) in parent:
                path.append((i, j))
                i, j = parent[(i, j)]
            path.append((0, 0))
            return cost, path[::-1]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                new_cost = cost + grid[ni][nj]
                if new_cost < min_cost[ni][nj]:
                    min_cost[ni][nj] = new_cost
                    parent[(ni, nj)] = (i, j)
                    heapq.heappush(pq, (new_cost, ni, nj))
matrix = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

min_cost, path = minPathSumBFS(matrix)
print(min_cost)
print(path)
