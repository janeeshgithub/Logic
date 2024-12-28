
"""from collections import deque

# Function to perform BFS on a graph
def bfs(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start_node])  # Queue to store nodes to explore

    while queue:
        node = queue.popleft()  # Dequeue a node from the front
        if node not in visited:
            print(node, end=' ')  # Process the current node
            visited.add(node)  # Mark the node as visited

            # Enqueue all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(graph, 'A')

# Perform BFS starting from node 'A'
# Function to perform DFS using recursion
"""
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes

    if node not in visited:
        print(node, end=' ')  # Process the current node
        visited.add(node)  # Mark the node as visited

        # Recur for all the adjacent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform DFS starting from node 'A'
dfs(graph, 'B')
# Function to perform DFS using a stack
def dfs_iterative(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    stack = [start_node]  # Stack to store nodes to explore

    while stack:
        node = stack.pop()  # Pop a node from the stack
        if node not in visited:
            print(node, end=' ')  # Process the current node
            visited.add(node)  # Mark the node as visited

            # Push all unvisited neighbors onto the stack
            for neighbor in reversed(graph[node]):  # Reversing ensures left-to-right order
                if neighbor not in visited:
                    stack.append(neighbor)

# Perform DFS using a stack starting from node 'A'
dfs_iterative(graph, 'A')
