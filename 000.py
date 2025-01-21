# Defining a 3x3 binary matrix
from collections import deque
m = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
r=3
c=3

src=(0,1)
q=deque([src])
st=[]
st.append(src)
dirs=[(1,0),(-1,0),(0,-1),(0,1)]
while st:
    x,y=st.pop()
    for i,j in dirs:
        nx=x+i
        ny=y+j
        if 0<nx<r and 0<ny<c and m[nx][ny]:
            m[nx][ny]=0
            st.append((nx,ny))
            print(st)
        #print(nx,ny)


