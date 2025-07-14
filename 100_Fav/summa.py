
# s="janeesh"
# word=["jan","e","sh" ,"ee"]
# dp=[False]*(len(s)+1)
# dp[0]=True
# for i in range(1,len(s)+1):
#     for j in range(i):
#         if dp[j] and s[j:i] in word:
#             dp[i]=True
#             break
# print(dp)
'''
h=[15,0,10,0,5]
n=len(h)-1
l=0
r=n
lm=rm=0
w=0
while l<r:
    if h[l]<h[r]:
        if h[l]>lm:
            lm=h[l]
        else:
            w+=lm-h[l]
        l+=1
    else:
        if h[r]>rm:
            rm=h[r]
        else:
            w+=rm-h[r]
        r-=1
print(w)
'''



# s="naneeshhs"
# n=len(s)
# dp=[0]*n
# for i in range(n):
#     mc=i
#     for j in range(i+1):
#         if s[j:i+1]==s[j:i+1][::-1]:
#             mc=0 if j==0 else min(mc,dp[j-1]+1)
#         dp[i]=mc
# print(dp)

s="JANEESHP"
seen={}
l=0
ml=0
for i,j in enumerate(s):
    if j in seen and seen[j]>=l:
        l=seen[j]+1
    seen[j]
















# t=set()
# for i in range(10):
#     if i % 2 == 0:
#         t.add(i)
# print(t)

# n=10
# dp=[1]*(n+1)
# nums=[i for i in range(n)]
# nums=nums[::-1]
# for i in range(n):
#     for j in range(i):
#         if nums[j]<nums[i]:
#             dp[i]=max(dp[i],dp[j]+1)
# print(dp)

# import bisect
# s=[]
# for x in nums:
#     i=bisect.bisect_left(s,x)
#     if i==len(s):
#         s.append(x)
#     else:
#         s[i]=x
# print(s)
    