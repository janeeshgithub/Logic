n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,n,2):
    j=l.index(l[i]^1)
    l[i+1],l[j]=l[j],l[i+1]
    s+=l[j]!=l[i+1]
print(s)