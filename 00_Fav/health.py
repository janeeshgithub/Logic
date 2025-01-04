from collections import deque


def can_reach_with_health(r, c, h, grid):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = [[-1] * c for _ in range(r)]
    q = deque([(0, 0, h)])
    visited[0][0] = h
    while q:
        x, y, health = q.popleft()
        if x == r - 1 and y == c - 1 and health >= 1:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                new_health = health - 1 if grid[nx][ny] == 1 else health  # Unsafe cells reduce health
                if new_health >= 1 and new_health > visited[nx][ny]:
                    visited[nx][ny] = new_health
                    q.append((nx, ny, new_health))

    # If we exit the loop, it means we couldn't reach the goal with enough health
    return False



def can_reach_with_health_dfs(r, c, h, grid):
    # Directions for moving: right, down, up, left
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # Visited matrix to keep track of visited cells and remaining health
    visited = [[-1] * c for _ in range(r)]

    def dfs(x, y, health):
        # If we reached the bottom-right corner and have enough health
        if x == r - 1 and y == c - 1 and health >= 1:
            return True

        # Mark the current cell as visited with current health
        visited[x][y] = health

        # Explore all 4 possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < r and 0 <= ny < c:  # Check bounds
                new_health = health - 1 if grid[nx][ny] == 1 else health  # Unsafe cells reduce health

                # If we haven't visited this cell with more health before
                if new_health >= 1 and new_health > visited[nx][ny]:
                    if dfs(nx, ny, new_health):  # Recur to explore the next cell
                        return True

        return False

    # Start DFS from the top-left corner (0, 0) with full health
    return dfs(0, 0, h)


# Input reading
r, c, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

# Output the result
if can_reach_with_health(r, c, h, grid):
    print("true")
else:
    print("false")

if can_reach_with_health_dfs(r, c, h, grid):
    print("true")
else:
    print("false")
