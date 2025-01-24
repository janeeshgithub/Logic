from collections import Counter

N=2
def rec(i):
    print(i)
    if i==N:
        return
    return rec(i+1)
a=[1,2,3]
rec(0)

a=[1,2,3,4,43,2,5,6,7,7]
t=Counter(a)
h={}
for j in a:
    h[j]=h.get(j,0)+1
a=max(h.values())
for i,j in h.items():
    if j==a:
        print(i,j)
