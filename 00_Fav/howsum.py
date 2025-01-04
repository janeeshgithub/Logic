from logging import NullHandler


def howsum(ts,num,memo):
    if ts in memo:
        return memo[ts]
    if ts==0:
        return []
    if ts<0:
        return None
    for i in num:
        r=ts-i
        rr=howsum(r,num,memo)
        if rr is not None:
            memo[ts]=[rr[:],i]
            return memo[ts]
    memo[ts]=None
    return None

def howsumdp(ts,num):
    t=[None]*(ts+1)
    t[0]=[]
    for i in range(ts+1):
        if t[i] is not None:
            for j in num:
                if i+j<=ts:
                    t[i+j]=t[i]+[j]
    return t[ts]


print(howsumdp(30,[10]))
print(howsum(30,[10],{}))