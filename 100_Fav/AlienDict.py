from collections import defaultdict, deque

def alien_order(words):
    # Step 1: Create graph and in-degree count
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    # Step 2: Build the graph by comparing adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
        else:
            if len(word1) > len(word2):  # Case where prefix is longer but same in both
                return ""

    # Step 3: Topological sort using BFS (Kahn's algorithm)
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    order = []

    while queue:
        char = queue.popleft()
        order.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: If there are still letters with non-zero in-degree, there's a cycle
    if len(order) != len(in_degree):
        return ""

    return ''.join(order)

# Example usage
words1 = ["wrf", "wrt", "er", "ett", "rftt"]
result = alien_order(words1)
print(result)
