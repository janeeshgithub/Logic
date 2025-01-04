def countAndSay(n):
    if n == 1:
        return "1"
    t = "1"
    for _ in range(n - 1):
        current = ""
        count = 1
        for i in range(1, len(t)):
            if t[i] == t[i - 1]:
                count += 1
            else:
                current += str(count) + t[i - 1]
                count = 1

        current += str(count) + t[-1]
        t = current
    return t
print(countAndSay(5))
