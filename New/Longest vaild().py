s = "()()()()(()()())"  # Input string containing parentheses
n = len(s)  # Length of the string

s1 = s2 = c1 = c2 = 0  # Counters for open/close brackets and valid sequence lengths
a = 0  # Stores the maximum valid parentheses length

for i in range(n):
    # Forward pass: Checking valid parentheses from left to right
    if s[i] == '(':
        s1 += 1  # Increment open bracket counter
    else:
        if s1:  # If there's an unmatched open bracket
            s1 -= 1  # Match it with the current closing bracket
            c1 += 2  # Increase valid sequence length by 2
            if not s1:  # If all open brackets are matched
                a = max(a, c1)  # Update max valid length
        else:
            c1 = 0  # Reset valid length if unmatched closing bracket appears

    # Backward pass: Checking valid parentheses from right to left
    if s[n - 1 - i] == ')':
        s2 += 1  # Increment close bracket counter
    else:
        if s2:  # If there's an unmatched close bracket
            s2 -= 1  # Match it with the current opening bracket
            c2 += 2  # Increase valid sequence length by 2
            if not s2:  # If all close brackets are matched
                a = max(a, c2)  # Update max valid length
        else:
            c2 = 0  # Reset valid length if unmatched opening bracket appears

print(a)  # Output the maximum valid parentheses length
