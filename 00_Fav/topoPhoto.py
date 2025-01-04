from collections import deque, defaultdict

n, l = map(int, input().split(","))
stu = [chr(i + 65) for i in range(n)]
p = []
for _ in range(l):
    p.append(list(input().strip().split(",")))
m = False
for i in stu:
    rc = 0
    q = deque()
    v = []
    q.append(i)
    v.append(i)
    while q:
        s = q.popleft()
        for j in p:
            if s in j:
                suc = j[j.index(s) + 1:]
                for k in suc:
                    if k not in v:
                        q.append(k)
                        v.append(k)
                        rc += 1
    q.append(i)
    v.append(i)
    while q:
        s = q.popleft()
        for j in p:
            if s in j:
                pre = j[0:j.index(s)]
                for k in pre:
                    if k not in v:
                        q.append(k)
                        v.append(k)
                        rc += 1
    if rc != n - 1:
        print(i,end=" ")
        m = True
if not m:
    print("N/A");



