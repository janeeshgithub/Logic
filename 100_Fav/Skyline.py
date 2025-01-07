import heapq
def get_skyline(buildings):
    events = []
    for L, R, H in buildings:
        events.append((L, -H, R))
        events.append((R, 0, 0))
    events.sort(key=lambda x: (x[0], x[1]))
    result = []
    heap = [(0, float('inf'))]
    prev_max_height = 0
    for x, negH, R in events:
        while heap[0][1] <= x:
            heapq.heappop(heap)
        if negH != 0:
            heapq.heappush(heap, (negH, R))
        curr_max_height=-heap[0][0]
        if curr_max_height != prev_max_height:  # Only add a point if the height changes
            if curr_max_height == 0 and len(result) > 0 and result[-1][0] == x:  # Avoid duplicate zero points
                result[-1][1] = curr_max_height
            else:
                result.append([x, curr_max_height])
            prev_max_height = curr_max_height
    return result


# Example usage
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
skyline = get_skyline(buildings)
print(skyline)
