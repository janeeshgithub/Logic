from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def inorder(r, arr):
    if r is None:
        return
    inorder(r.left, arr)
    arr.append(r.val)  # Append values to the provided list
    inorder(r.right, arr)

def preorder(r,arr):
    if r is None:
        return
    arr.append(r.val)
    preorder(r.left,arr)
    preorder(r.right,arr)
def postorder(r,arr):
    if r is None:
        return
    postorder(r.left, arr)
    postorder(r.right, arr)
    arr.append(r.val)

def jan(r):
    a=[]
    b=[]
    c=[]
    inorder(r,a)
    preorder(r,b)
    postorder(r,c)
    return  a,b,c# Return the list after inorder traversal

def dfs(node):
    if node==None:
        return []
    b=dfs(node.right)
    a=dfs(node.left)
    return [min([node.val]+a+b)]

def bfs(node):
    if node==None:
        return []
    v=[]
    q=deque([node])
    while q:
        c=q.popleft()
        v.append(c.val)
        if c.left!=None:
            q.append(c.right)
            q.append(c.left)
    return v

def maxpath(node):
    if node.val==None:
        return 0
    if node.left==None and node.right==None:
        return node.val
    m=max(maxpath(node.left),maxpath(node.right))
    return m+node.val

a=Node(10)
b=Node(20)
c=Node(30)
d=Node(40)
e=Node(50)
a.right=b
a.left=c
b.left=d
b.right=e
print(dfs(a))
print(bfs(a))
print(maxpath(a))


