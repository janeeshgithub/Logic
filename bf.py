def bellman_ford(graph, V, source):
    dist = [float('inf')] * V
    dist[source] = 0
    for _ in range(V - 1):
        for u, v, weight in graph:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    for u, v, weight in graph:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            print("Graph contains a negative-weight cycle")
            return None
    shortest_path_sum = sum(d for d in dist if d < float('inf'))

    return shortest_path_sum
graph = [
    (0, 1, 5),   # edge from 0 to 1 with weight 5
    (0, 2, 4),   # edge from 0 to 2 with weight 4
    (1, 3, 3),   # edge from 1 to 3 with weight 3
    (2, 1, 6),   # edge from 2 to 1 with weight 6
    (3, 2, 2)    # edge from 3 to 2 with weight 2
]
V = 4
source = 1

result = bellman_ford(graph, V, source)
print("Sum of shortest path distances:", result)
