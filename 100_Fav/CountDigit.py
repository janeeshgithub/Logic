n = int(input())  # The number for which we need to count digits
d = int(input())  # The digit whose occurrences we need to count

count = 0  # To keep track of occurrences
place = 1  # To track the current place (1s, 10s, 100s, etc.)

while n // place > 0:
    higher = n // (place * 10)
    current_digit = (n // place) % 10
    lower = n % place

    if current_digit < d:
        count += higher * place
    elif current_digit == d:
        count += higher * place + (lower + 1)
    else:
        count += (higher + 1) * place

    place *= 10

print(count)
