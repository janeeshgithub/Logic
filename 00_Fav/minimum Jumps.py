x = int(input())
y = list(map(int, input().split()))
m = y[0]
s = y[0]
j = 1
if x == 1:
    print(0)
    exit()
for i in range(1, x):
    if i == x - 1:
        break
    m = max(y[i] + i, m)
    s -= 1
    if s == 0:
        j += 1
        s = m - i
print(j)
