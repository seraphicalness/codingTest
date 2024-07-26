from collections import deque
n, k = map(int,input().split())
lst = deque([i for i in range(1, n+1)])
res = []

while len(lst) != 0:
    for _ in range(k-1):
        lst.append(lst.popleft())
    res.append(str(lst.popleft()))

print('<'+', '.join(res)+'>')