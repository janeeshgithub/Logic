# def dfs(graph,node,vis):
#     if node in vis:
#         return
#     print(node)
#     vis.add(node)
#     for i in graph[node]:
#         dfs(graph,i,vis)

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
vis= set()
def dfs(node):
    if node in vis:
        return
    print(node)
    vis.add(node)
    for i in graph[node]:
        dfs(i)
dfs(0)
