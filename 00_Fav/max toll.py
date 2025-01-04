def hmc(n,d,k,td,tf):
    r=[0]*n
    ti=0
    for i in range(1,n+1):
        if(td[ti]==i):
            if i<=d:
                r[i]=max(r[i-1],tf[ti])
            else:
                r[i]=max(r[i-1],tf[ti]+r[i-d-1])
            ti+=1
            if ti==k:
                return r[i];
        else:
            r[i]=r[i-1]
    return r[-1]
n,d=map(int,input().split())
k=int(input())
td=list(map(int,input().split()))
tf=list(map(int,input().split()))
print(hmc(n,d,k,td,tf))