from collections import deque

n, k = map(int,input().split())
res = []

peo = deque(i for i in range(1, n+1))


while peo:
    for _ in range(k-1):
        peo.append(peo.popleft())
    res.append(peo.popleft())


print(str(res).replace('[', '<').replace(']', '>'))