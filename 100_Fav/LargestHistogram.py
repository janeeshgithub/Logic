class Solution(object):
    def largestRectangleArea(self, heights):
        # Variable to store the maximum area
        max_area = 0
        # Stack to store pairs of (start_index, height)
        stack = []
        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            # Start index for the current bar
            start = i
            # If the current height is smaller than the height at the top of the stack,
            # we need to calculate the area for the bar at the top of the stack.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate the area using the height of the popped bar
                max_area = max(max_area, height * (i - index))
                # Update start to the index of the popped bar
                start = index
            # Push the current bar into the stack
            stack.append((start, h))

        # Process any remaining bars in the stack
        for i, h in stack:
            # Calculate the area for each bar, assuming it extends to the end of the histogram
            max_area = max(max_area, h * (len(heights) - i))

        # Return the maximum area found
        return max_area
