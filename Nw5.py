x=[[i*j+j for i in range(5)] for j in range(5)]
print(x)
t=[]
for i in zip(*x):
    t.append(i)
print(t)


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

a=Node('A')
b=Node('B')
c=Node('C')
a.next=b
b.next=c
head=a
while head:
    print(head.val)
    head=head.next