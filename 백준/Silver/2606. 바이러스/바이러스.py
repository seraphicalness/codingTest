A = int(input())
B = int(input())

arr = [[]*(A+1) for _ in range(A+1)]
for i in range(B):
    p,q = map(int,input().split())
    arr[p].append(q)
    arr[q].append(p)

# 재귀적 구현
def dfs(x):
    global count
    visited[x] = True # 방문했는지 표시
    count += 1 
    for node in arr[x]: # 탐색할 인덱스 안에있는 수 순서대로
        if visited[node]: # 방문했으면 넘어감
            continue
        dfs(node) # 안했으면 계속 재귀 탐색

count = 0
visited = [False for _ in range(A+1)]
dfs(1)
print(count-1)