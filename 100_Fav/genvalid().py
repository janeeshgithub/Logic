class Solution(object):
    def removeInvalidParentheses(self, s):
        # Helper function to check if the parentheses in the string are balanced
        def isValid(s):
            stack = []
            for char in s:
                if char == '(':
                    stack.append('(')
                elif char == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(')')
            return not stack

        # Depth-First Search to explore all possible valid strings
        def dfs(s, left_rem, right_rem):
            # If the current string is valid and no parentheses need to be removed
            if left_rem == 0 and right_rem == 0 and isValid(s):
                results.append(s)
                return

            for i in range(len(s)):
                # Skip non-parenthesis characters
                if s[i] not in '()':
                    continue

                # Skip if removing the current parenthesis is unnecessary
                if (s[i] == '(' and left_rem == 0) or (s[i] == ')' and right_rem == 0):
                    continue

                # Generate new string by removing the current parenthesis
                new_s = s[:i] + s[i + 1:]
                if new_s not in visited:
                    visited.add(new_s)
                    dfs(new_s, left_rem - (s[i] == '('), right_rem - (s[i] == ')'))

        # Initial counts for left and right parentheses to remove
        left_count = sum(1 for char in s if char == '(')
        right_count = sum(1 for char in s if char == ')')

        # Store the results and a visited set to avoid revisiting strings
        results = []
        visited = set([s])

        # Start DFS to find all valid strings
        dfs(s, left_count, right_count)

        return results
