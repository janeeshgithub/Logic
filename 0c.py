def solve(n):
    if n % 2 == 0:
        max_product = (n // 2) * (n // 2)
    else:
        max_product = (n // 2) * (n // 2 + 1)

    min_product = 1

    total_edges = n * (n - 1) // 2

    if n % 2 == 0:
        edges_removed_max = (n // 2) * (n // 2)
    else:
        edges_removed_max = (n // 2) * (n // 2 + 1)

    edges_removed_min = total_edges - (n - 1)

    return edges_removed_max, edges_removed_min


n = 3
max_edges_removed, min_edges_removed = solve(n)
print(f"Maximum number of edges that can be removed: {max_edges_removed}")
print(f"Minimum number of edges that can be removed: {min_edges_removed}")
