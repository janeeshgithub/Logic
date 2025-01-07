def sum_of_factors(n):
    total = 0
    for i in range(1, n + 1):
        total += i * (n // i)
    return total

# Example Usage
N = 5
result = sum_of_factors(N)
print(f"Sum of factors for all numbers from 1 to {N}: {result}")
