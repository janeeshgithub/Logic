n=int(input())
s=[]
e=[]
for i in range(n):
    a,b=map(str,input().split())
    m=a.split(":")
    n=b.split(":")
    s.append(int(m[0])*60+int(m[1]))
    e.append(int(n[0])*60+int(n[1]))
c=0
si=0
ei=0
s.sort()
e.sort()
while (si<len(s) and ei<len(e)):
    cr=abs(si-ei)+1
    c=max(cr,c)
    if(s[si]<e[ei]):
        si+=1
    else:
        ei+=1
    while (si<len(s) and ei<len(e) and s[i]>=e[i]):
        ei+=1
print(c)