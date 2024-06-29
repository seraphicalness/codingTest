import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)    
count = 1

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs = deque([R])
visited[R] = 1
while bfs:
    r = bfs.popleft()
    graph[r].sort()
    for i in graph[r]:
        if not visited[i]:
            count += 1
            visited[i] = count
            bfs.append(i)

for i in range(1, N+1):
    print(visited[i])