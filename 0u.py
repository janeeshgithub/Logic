import heapq

x=list(map(int,input().split(",")))
k=len(x)-1
heapq.heapify(x)
while k:
    heapq.heappop(x)
    k-=1
print(heapq.heappop(x))

