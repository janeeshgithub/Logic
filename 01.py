from itertools import permutations


# Function to check if the current permutation satisfies the crypt-arithmetic equation
def is_valid_solution(solution, letters, words):
    # Mapping from letters to digits
    letter_to_digit = dict(zip(letters, solution))

    # Convert words to numbers using the current solution
    values = []
    for word in words:
        value = 0
        for letter in word:
            value = value * 10 + letter_to_digit[letter]
        values.append(value)

    # Check if the equation holds (sum of the left part equals the right part)
    return sum(values[:-1]) == values[-1]


# Function to solve the crypt-arithmetic problem
def solve_crypt_arithmetic(equation):
    # Split the equation into left and right parts
    left_part, right_part = equation.split("=")

    # Get the words involved in the equation
    words = left_part.split("+") + [right_part]

    # Find the unique letters in the equation
    letters = set(''.join(words))

    # Check if there are more than 10 unique letters (which makes it impossible to solve)
    if len(letters) > 10:
        print("Too many unique letters, no solution possible!")
        return None

    # Generate all possible permutations of digits for the letters
    solutions = []
    for solution in permutations(range(10), len(letters)):
        if is_valid_solution(solution, letters, words):
            # If a valid solution is found, store it
            letter_to_digit = dict(zip(letters, solution))
            solutions.append(letter_to_digit)

    return solutions


def main():
    # Take the crypt-arithmetic equation as input
    equation = input("Enter the crypt-arithmetic equation (e.g., 'CROSS+ROAD=DANGER'): ").strip()

    # Solve the equation and get all solutions
    solutions = solve_crypt_arithmetic(equation)

    if solutions:
        print("All possible valid solutions found:")
        # Print each solution
        for solution in solutions:
            for letter, digit in solution.items():
                print(f"{letter} = {digit}")
            print("-" * 20)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
