n, L = map(int, input().split())
l = list(map(int, input().split()))
w = [0] * (n + 1)
w[0] = 1
for s in range(1, n + 1):
    for i in range(L):
        if s >= l[i]:
            w[s] += w[s - l[i]]
print(w[-1])
#min steps