from collections import defaultdict,deque
arr = [4, 4, 1, 4, 13, 8, 8, 8, 0, 8, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21]
n = 23
c1, c2 = 9, 2
G = defaultdict(list)
for u, v in enumerate(arr):
    if v == -1: continue
    G[u].append(v)
def bfs():
    q = deque([[c1, 1], [c2, 2]])
    vis = [0] * n
    while q:
        node, num = q.popleft()
        if vis[node] == 2 and num == 1 or vis[node] == 1 and num == 2:  # this is the node visited by other path
            return node
        if vis[node] == num: continue
        vis[node] = num
        for nei in G[node]:
            q.append([nei, num])
    return -1
print(bfs())

from collections import deque

def shortestPathLength(graph):
    n = len(graph)
    all_visited = (1 << n) - 1  # Bitmask with all nodes visited (e.g., 111...111)
    queue = deque([(i, 1 << i, 0) for i in range(n)])  # (node, visited_mask, steps)
    visited = set((i, 1 << i) for i in range(n))  # Track visited states

    while queue:
        node, visited_mask, steps = queue.popleft()

        # If all nodes have been visited, return the number of steps
        if visited_mask == all_visited:
            return steps

        # Explore neighbors
        for neighbor in graph[node]:
            next_mask = visited_mask | (1 << neighbor)  # Mark neighbor as visited
            if (neighbor, next_mask) not in visited:  # Avoid revisiting states
                visited.add((neighbor, next_mask))
                queue.append((neighbor, next_mask, steps + 1))

# Example Input
graph = [
    [1, 2, 3],  # Node 0 connected to 1, 2, 3
    [0],        # Node 1 connected to 0
    [0],        # Node 2 connected to 0
    [0]         # Node 3 connected to 0
]

# Function Call
result = shortestPathLength(graph)
print("Length of the shortest path that visits every node:", result)
