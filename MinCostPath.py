
mat = [[5, 9, 6],
          [11, 5, 2]]  # Input matrix
n = len(mat)
m = len(mat[0])
d = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            d[i][j]=mat[i][j]
        else:
            u=mat[i][j]
            if i>0:
                u+=d[i-1][j]
            else:
                u+=10**9+7
            l = mat[i][j]
            if j > 0:
                l+= d[i][j-1]
            else:
                l+= int(1e9)
            d[i][j]=min(u,l)
for i in d:
    print(i)
for i in mat:
    print(i)


