from collections import deque

def maximumMinutes(grid):
    def bfsCanReach(time):
        q = deque([(0, 0)])
        curGrid = [row[:] for row in grid]  # Copy the grid to mark visited
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if i == m - 1 and j == n - 1 and time <= fire[i][j]:
                    return True

                if fire[i][j] <= time or curGrid[i][j] == "#":
                    continue

                curGrid[i][j] = "#"
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and curGrid[ni][nj] == 0:
                        q.append((ni, nj))
            time += 1
        return False
    m, n = len(grid), len(grid[0])
    fire = [[float('inf')] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
    dist = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if fire[i][j] != float('inf'):
                continue
            fire[i][j] = dist
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and fire[ni][nj] == float('inf'):
                    q.append((ni, nj))
        dist += 1

    # Edge cases
    if not bfsCanReach(0):
        return -1

    if fire[m - 1][n - 1] == float('inf'):
        return "No fire, Bhai. Aram se aao!"

    left, right = 0, 10 ** 9
    while left < right:
        mid = left + (right-left)//2
        if bfsCanReach(mid):
            left = mid
        else:
            right = mid - 1

    return left

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 2, 0, 0, 1],
        [0, 2, 0, 2, 2],
        [0, 0, 0, 0, 0],
        [0, 2, 2, 2, 2],
        [0, 0, 0, 0, 0]
    ]
    print(maximumMinutes(grid))  # Output: 0
