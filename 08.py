from collections import deque

# Function to check if the goal is achievable
def water_jug_problem(capacity_x, capacity_y, target):
    # Set to store the visited states (a, b) to avoid revisiting
    visited = set()

    # Queue for BFS; stores the state (jug1, jug2)
    queue = deque([(0, 0)])

    # BFS to find the solution
    while queue:
        jug1, jug2 = queue.popleft()

        # If we reach the target amount of water in either jug, return True
        if jug1 == target or jug2 == target:
            return True

        # Add the current state to visited
        visited.add((jug1, jug2))

        # Possible next states to explore
        next_states = [
            (capacity_x, jug2),  # Fill jug1
            (jug1, capacity_y),  # Fill jug2
            (0, jug2),           # Empty jug1
            (jug1, 0),           # Empty jug2
            (jug1 - min(jug1, capacity_y - jug2), jug2 + min(jug1, capacity_y - jug2)),  # Pour jug1 into jug2
            (jug1 + min(jug2, capacity_x - jug1), jug2 - min(jug2, capacity_x - jug1))   # Pour jug2 into jug1
        ]

        # Enqueue the valid states which haven't been visited yet
        for state in next_states:
            if state not in visited:
                queue.append(state)

    # If no solution is found
    return False

# Example usage
capacity_x = 4  # Capacity of jug1
capacity_y = 3  # Capacity of jug2
target = 2      # Target amount of water to measure

if water_jug_problem(capacity_x, capacity_y, target):
    print(f"It's possible to measure {target} liters.")
else:
    print(f"It's not possible to measure {target} liters.")
