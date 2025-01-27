from collections import deque

# BFS Implementation
def bfs(jug1Capacity, jug2Capacity, targetCapacity):
    # Initialize the queue for BFS and other required data structures
    queue = deque()
    visited = set()
    parent = {}  # To store parent states for path reconstruction
    actions = {}  # To store actions taken to reach each state
    # Initial state: both jugs are empty
    queue.append((0, 0))
    visited.add((0, 0))
    parent[(0, 0)] = None  # Starting state has no parent
    actions[(0, 0)] = "Start"  # Initial action

    # BFS Loop
    while queue:
        a, b = queue.popleft()

        # If the target capacity is reached
        if a == targetCapacity or b == targetCapacity:
            # Reconstruct the path from the target state to the initial state
            path = []
            current = (a, b)
            while current:
                path.append((current, actions[current]))
                current = parent[current]
            path.reverse()  # Reverse to get the path in correct order

            # Print the path with actions
            print(f"Steps to achieve {targetCapacity}L:")
            for state, action in path:
                print(f"{state} -> {action}")
            print("Number of Steps Take",len(path))
            return

        # List all possible next states and actions
        next_states = [
            ((jug1Capacity, b), f"Fill jug1 to {jug1Capacity}L"),  # Fill jug1
            ((a, jug2Capacity), f"Fill jug2 to {jug2Capacity}L"),  # Fill jug2
            ((0, b), "Empty jug1 completely"),  # Empty jug1
            ((a, 0), "Empty jug2 completely"),  # Empty jug2
            ((max(0, a - (jug2Capacity - b)), min(jug2Capacity, b + a)), f"Pour water from jug1 to jug2"),  # Pour jug1 to jug2
            ((min(jug1Capacity, a + b), max(0, b - (jug1Capacity - a))), f"Pour water from jug2 to jug1")  # Pour jug2 to jug1
        ]

        # Process each next state
        for (next_a, next_b), action in next_states:
            if (next_a, next_b) not in visited:
                visited.add((next_a, next_b))
                queue.append((next_a, next_b))
                parent[(next_a, next_b)] = (a, b)  # Track the parent state
                actions[(next_a, next_b)] = action  # Track the action

    print("No solution exists!")
    return

# DFS Implementation
def dfs(jug1Capacity, jug2Capacity, targetCapacity):
    # Set to track visited states
    visited = set()

    # Helper function to print actions and current state
    def print_action(a, b, action):
        print(f"Action: {action} -> Jug1: {a}, Jug2: {b}")

    # Recursive DFS function to explore all states
    def explore(a, b):
        # If the target capacity is reached
        if a + b == targetCapacity:
            print_action(a, b, "Reached target")
            return True  # Target is achieved

        # Avoid revisiting the same state
        if (a, b) in visited:
            return False

        visited.add((a, b))  # Mark the current state as visited

        # Explore possible next states and actions
        # 1. Fill Jug1 completely
        if explore(jug1Capacity, b):
            print_action(jug1Capacity, b, "Fill Jug1 completely")
            return True

        # 2. Fill Jug2 completely
        if explore(a, jug2Capacity):
            print_action(a, jug2Capacity, "Fill Jug2 completely")
            return True

        # 3. Empty Jug1
        if explore(0, b):
            print_action(0, b, "Empty Jug1")
            return True

        # 4. Empty Jug2
        if explore(a, 0):
            print_action(a, 0, "Empty Jug2")
            return True

        # 5. Pour from Jug1 to Jug2
        if explore(max(0, a - (jug2Capacity - b)), min(jug2Capacity, a + b)):
            print_action(max(0, a - (jug2Capacity - b)), min(jug2Capacity, a + b), "Pour water from Jug1 to Jug2")
            return True

        # 6. Pour from Jug2 to Jug1
        if explore(min(jug1Capacity, a + b), max(0, b - (jug1Capacity - a))):
            print_action(min(jug1Capacity, a + b), max(0, b - (jug1Capacity - a)), "Pour water from Jug2 to Jug1")
            return True

        return False

    # Start DFS from both jugs being empty
    return explore(0, 0)

# Example usage:
jug1 = int(input("ENTER THE JUG1 CAPACITY: "))
jug2 = int(input("ENTER THE JUG2 CAPACITY: "))
target = int(input("ENTER THE TARGET: "))



print("BFS Solution:")
bfs(jug1, jug2, target)

print("\nDFS Solution:")
dfs(jug1, jug2, target)
