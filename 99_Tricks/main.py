pat="abcdef"
tar='acde'
p=len(pat)
t=len(tar)
dp=[[0]*(t+1) for _ in range(p+1)]
for i in range(1,p+1):
    for j in range(1,t+1):
        if pat[i-1]==tar[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
for i in dp:
    print(i)