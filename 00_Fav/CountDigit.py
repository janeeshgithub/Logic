n=int(input())
d=int(input())
ct=0
p=1
while n//p>0:
    h=n//(p*10)
    c=(n//p)%10
    l=n%p
    if c<d:
        ct+=h*p
    elif c==d:
        ct+=h*p+(l+1)
    else:
        ct+=(h+1)*p
    p*=10
print(ct)