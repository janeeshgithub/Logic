def derangement(n):
    if n == 0:
        return 1  # Base case: Empty set has one derangement (do nothing)
    if n == 1:
        return 0  # Base case: 1 item cannot be deranged

    # Iterative computation of derangements
    der = [0] * (n + 1)
    der[0] = 1
    der[1] = 0
    for i in range(2, n + 1):
        der[i] = (i - 1) * (der[i - 1] + der[i - 2])
    return der[n]


# Input
n = 3

# Output
print(f"The number of ways to interchange {n} items such that no one gets their own item is: {derangement(n)}")
