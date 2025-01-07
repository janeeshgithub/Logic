a = input().strip()  # Input string a
b = input().strip()  # Input string b

r = len(a)  # Length of string a
c = len(b)  # Length of string b

# Create a matrix of size (r+1) x (c+1)
d = [[0] * (c + 1) for _ in range(r + 1)]

# Initialize the first row and first column
for i in range(c + 1):
    d[0][i] = i  # Cost of transforming an empty string to b[0..i]
for i in range(r + 1):
    d[i][0] = i  # Cost of transforming a[0..i] to an empty string

# Fill the matrix using dynamic programming
for i in range(1, r + 1):
    for j in range(1, c + 1):
        if a[i - 1] == b[j - 1]:  # No change needed if characters match
            d[i][j] = d[i - 1][j - 1]
        else:
            # Take the minimum cost of the three operations: delete, insert, or substitute
            d[i][j] = min(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1]) + 1

# Output the edit distance (Levenshtein distance)
print(d[-1][-1])
