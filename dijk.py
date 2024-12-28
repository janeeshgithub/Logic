import heapq


def dijkstra(graph, source):
    V = len(graph)
    dist = [float('inf')] * V
    dist[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(priority_queue, (dist[v], v))

    return dist


# Example usage
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
source = 2
distances = dijkstra(graph, source)
print("Shortest distances from source:", distances)
