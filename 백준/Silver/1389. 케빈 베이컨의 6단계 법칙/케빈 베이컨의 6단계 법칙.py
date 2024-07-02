import sys
from collections import deque

N, M = map(int,input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,start):
    num = [0] * (N+1)
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:  # 방문을 안했으면
                num[i] = num[a] + 1 # pop한거에 +1
                q.append(i) # q에 append 
                visited[i] = 1 # 방문 처리 
    return sum(num)

result = []
for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    result.append(bfs(graph,i))
print(result.index(min(result))+1)

