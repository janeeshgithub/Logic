def cansum(ts,num,memo):
    if ts in memo:
        return memo[ts]
    if ts==0:
        return True
    if ts<0:
        return False
    for i in num:
        r=ts-i
        if cansum(r,num,memo)==True:
            memo[ts]=True
            return True
    memo[ts]=False
    return False

def cansumdp(ts,num):
    t=[False]*(ts+1)
    t[0]=True
    for i in range(len(num)):
        if t[i]==True:
            for j in num:
                t[i+j]=True
    return t[-1]

print(cansum(30,[10],{}))
print(cansumdp(10,[10]))