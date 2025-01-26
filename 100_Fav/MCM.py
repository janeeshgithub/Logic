# class Solution:
#     def matrixMultiplication(self, arr):
#         mem={}
#         def rec(i,j):
#             if i==j:
#                 return 0
#             if (i,j) in mem:
#                 return mem[(i,j)]
#             m=float('inf')
#             for k in range(i,j):
#                 st=arr[i-1]*arr[k]*arr[j]+rec(i,k)+rec(k+1,j)
#                 m=min(st,m)
#             mem[(i,j)]=m
#             return mem[(i,j)]
#         return rec(1,len(arr)-1)
class Solution:
    def matrixMultiplication(self, arr):
        mem=[[-1]*len(arr) for _ in range(len(arr)]
        for i in range(len(arr)):
            mem[i][i]=0
            m=float('inf')
        for i in range(len(arr)-1,0,-1):
            for j in range(i+1,len(arr)):
                for k in range(i,j):
                    st=arr[i-1]*arr[k]*arr[j]+rec(i,k)+rec(k+1,j)
                    m=min(st,m)
                mem[i][j]=m
        return mem[1][len(arr)-1]