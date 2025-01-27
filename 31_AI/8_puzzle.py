from heapq import heappush, heappop

# Define the target state of the 8-puzzle
TARGET = ((1, 2, 3), (4, 5, 6), (7, 8, 0))  # Goal state (0 represents the empty space)


# Function to compute the Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0
    for r in range(3):
        for c in range(3):
            value = state[r][c]
            if value != 0:
                target_r, target_c = divmod(value - 1, 3)
                distance += abs(target_r - r) + abs(target_c - c)
    return distance


# Function to get possible moves (up, down, left, right)
def get_neighbors(state):
    neighbors = []
    empty_r, empty_c = next((r, c) for r in range(3) for c in range(3) if state[r][c] == 0)

    # Define possible moves for the empty space
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dr, dc in directions:
        new_r, new_c = empty_r + dr, empty_c + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            # Swap the empty space with the adjacent tile
            new_state = [list(row) for row in state]
            new_state[empty_r][empty_c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[empty_r][empty_c]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


# A* Algorithm to solve the 8-puzzle
def a_star(start_state):
    open_list = []
    heappush(open_list, (0 + manhattan_distance(start_state), 0, start_state, []))  # f(n) = g(n) + h(n)
    visited = set()

    while open_list:
        _, cost, current_state, path = heappop(open_list)

        # If we reach the goal state, print the solution path
        if current_state == TARGET:
            print("Solution found!")
            print(f"Steps to reach the target state:")
            for state in path + [current_state]:
                for row in state:
                    print(row)
                print()
            return

        visited.add(current_state)

        # Explore neighbors
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                heappush(open_list,
                         (cost + 1 + manhattan_distance(neighbor), cost + 1, neighbor, path + [current_state]))

    print("No solution exists!")
    return


# Example usage
start_state = ((1, 2, 3), (0, 5, 6), (4, 7, 8))  # Initial state
a_star(start_state)
