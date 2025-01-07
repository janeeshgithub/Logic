x = int(input("Enter the number of terms: "))
t = "1"
for _ in range(x):
    next_term = ""
    count = 1
    for i in range(1, len(t)):
        if t[i] == t[i - 1]:
            count += 1
        else:
            next_term += str(count) + t[i - 1]
            count = 1
    next_term += str(count) + t[-1]
    t = next_term
print(t)