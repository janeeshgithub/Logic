def Root(base,expo):
    r=1
    b=base
    while expo>0:
        if b%2==1:
            expo-=1
            r*=b
        else:
            b*=b
            expo//=2
    return r

n, m = 3, 5
print("The answer is:", Root(n, m))
