import heapq


def mincostToHireWorkers(quality, wage, k):
    workers = sorted([(w / q, q, w) for q, w in zip(quality, wage)])
    min_cost = float('inf')
    quality_heap = []
    quality_sum = 0

    for ratio, q, w in workers:
        heapq.heappush(quality_heap, -q)  # Use max-heap (negative values)
        quality_sum += q

        if len(quality_heap) > k:
            quality_sum += heapq.heappop(quality_heap)  # Remove largest quality

        if len(quality_heap) == k:
            min_cost = min(min_cost, quality_sum * ratio)

    return min_cost


# Example usage
quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
print(mincostToHireWorkers(quality, wage, k))  # Output: 105
