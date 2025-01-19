def max_rectangle_area(heights):
    # Initialize an empty stack to keep track of bar indices
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n):
        # Process the current bar
        while stack and heights[stack[-1]] > heights[i]:
            # Pop the top of the stack and calculate the area
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)

        # Push the current index to the stack
        stack.append(i)

    # After finishing the loop, we may still have some indices in the stack
    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * w)

    return max_area

# Example usage:
heights = [2, 1, 5, 6,7,2, 3,4]
print("Maximum Rectangle Area:", max_rectangle_area(heights))
