nums=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
N=len(nums)
d = [0] * len(nums)
for i in range(N):
    m = 0
    for j in range(i):
        if nums[j] < nums[i]:
            m = max(m, d[j])
    d[i] = m + 1
print(d)
r=[]
k=1
for i,j in enumerate(d):
    if i==k:
        k+=1
        r.append(nums[i])
print(r)

