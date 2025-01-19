def minimumPathSum(triangle, n):
    # Initialize two lists: front and cur to represent the current and previous rows in dp
    front = [0] * n  # This represents the previous row
    cur = [0] * n  # This represents the current row

    # Initialize the bottom row of dp (front) with the values from the last row of the triangle
    for j in range(n):
        front[j] = triangle[n - 1][j]

    # Start from the second-to-last row and work upwards
    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            # Calculate the minimum path sum for the current cell by considering two possible moves: down and diagonal
            down = triangle[i][j] + front[j]
            diagonal = triangle[i][j] + front[j + 1]

            # Store the minimum of the two possible moves in the current row (cur)
            cur[j] = min(down, diagonal)

        # Update the previous row (front) with the current row (cur) for the next iteration
        front = cur

    # The minimum path sum will be stored in the first element of the front list after the loops
    return front[0]


def main():
    # Define the input triangle and its size
    triangle = [[1], [2, 2], [3, 2, 3], [1, 1, 4, 1]]
    n = len(triangle)

    # Call the minimumPathSum function and print the result
    print(minimumPathSum(triangle, n))


if __name__ == '__main__':
    main()

