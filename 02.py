nums=[1,2,3,4,100,22,34,5,6,3,5,4,3,2,1]
t=set()
for i in nums:
    t.add(i)
l=1

for i in t:
    if i-1 not in t:
        c=1
        x=i
        while x+1 in t:
            x+=1
            c+=1
        l=max(l,c)
print(l)

n = int(input())
b = list(map(int, input().split()))
b = [1] + b + [1]
n += 2
d = [[0] * n for _ in range(n)]
for l in range(2, n):
    for i in range(n - l):
        j = i + l
        for k in range(i + 1, j):
            d[i][j] = max(d[i][j], (b[i] * b[j] * b[k]) + d[i][k] + d[k][j])

print(d[0][n - 1])
