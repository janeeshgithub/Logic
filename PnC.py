def combinations(x, s, n, r):
    if len(s) == n:  # Base case: when the current subset is of length n
        r.append(s.copy())  # Append the current combination
        return

    for i in range(x, len(arr)):  # Start loop from the current index to the end
        s.append(arr[i])  # Add current element to the combination
        combinations(i + 1, s, n, r)  # Recursively build the next combination
        s.pop()  # Backtrack to try the next element





def permutations(s, n, r):
    if len(s) == n:  # Base case: when the current subset is of length n
        r.append(s.copy())  # Append the current permutation
        return

    for i in range(len(arr)):
        if arr[i] not in s:  # Ensure the element hasn't been used yet
            s.append(arr[i])  # Add the element to the permutation
            permutations(s, n, r)  # Recursively build the next permutation
            s.pop()  # Backtrack to try the next element

arr = [1, 2, 3, 4, 5]  # Input array
r_combinations = []
r_permutations = []
permutations([], 3, r_permutations)  # Find permutations of length 3
print("Permutations:", r_permutations)
combinations(0, [], 3, r_combinations)  # Find combinations of length 3
print("Combinations:", r_combinations)
def generate_subsets(arr):
    n = len(arr)
    subsets = []

    # Loop over the range of 0 to (2^n - 1)
    for i in range(1 << n):  # 1 << n is equivalent to 2 ** n
        subset = []
        for j in range(n):
            # Check if j-th bit is set in i
            if i & (1 << j):  # If the j-th bit is set in i
                subset.append(arr[j])
        subsets.append(subset)

    return subsets

arr = [1, 2, 3, 4, 5]  # Input array
all_subsets = generate_subsets(arr)
print("All Subsets (Combinations):", all_subsets)
