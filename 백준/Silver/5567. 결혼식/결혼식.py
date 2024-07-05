import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
friends = [[0]*(N+1) for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(int(input())):
    a, b = map(int,input().split())
    friends[a][b] = friends[b][a] = 1

def bfs(x):
    visited[x] = 1
    q = deque([x])
    while q:
        a = q.popleft()
        for i in range(1,len(friends)):
            if visited[i] == 0 and friends[a][i] == 1:
                q.append(i)
                visited[i] = visited[a] + 1 # 부모의 +1 저장

bfs(1)
answer = 0
for i in visited:
  if i>1 and i<4:
    answer+=1

print(answer)