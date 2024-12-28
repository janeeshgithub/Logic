arr=[1,1,1,1,1,1,1,1,1]
n=len(arr)
mi=0
mr=0
j=1
for i in range(n):
   mi=max(mi,i+arr[i])
   if i==mr:
       mr=mi
       j+=1
       if mr>=n-1:
           print(j)
           break
print(-1)