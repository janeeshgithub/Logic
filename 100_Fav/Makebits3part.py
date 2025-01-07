x = int(input())
y = list(map(int, input().split()))
t = sum(y)
if t % 3 != 0:
    print([-1, -1])
elif t == 0:
    print([0, x - 1])
else:
    a = [i for i, j in enumerate(y) if j == 1]
    pl = len(a) // 3
    i, j, k = a[0], a[pl], a[2 * pl]
    while k < x and y[i] == y[j] == y[k]:
        i += 1
        j += 1
        k += 1
    if k == x:
        print([i - 1, j])
    else:
        print([-1,-1])
