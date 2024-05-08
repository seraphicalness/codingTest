N,M,V = map(int,input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)] # 0으로만 이뤄진 배열 
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1 # 입력 값에 방문함 1 표시

#방문 리스트 행렬
visited1 = [0]*(N+1) # dfs에 쓰일 것
visited2 = visited1.copy() # bfs에 쓰일 것

#dfs 함수 만들기 - 깊이 우선 탐색 
def dfs(V): # V부터 탐색 시작
    visited1[V] = 1 # 방문처리
    print(V, end=' ') # 방문 했으므로 출력 
    for i in range(1, N+1): # graph[V]의 i를 계속 탐색
        if graph[V][i] == 1 and visited1[i] == 0: 
            # V와 연결되거나, 방문 기록 없는 노드 찾기
            dfs(i) # 있으면 i번째에 대해서 다시 재귀 

#bfs 함수 만들기
def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue: # queue에 값이 없을 때까지 반복 
        V = queue.pop(0) # 0번째 제거하고 그 값 V에 선언 
        # 큐 - 선입선출, 먼저 들어온 0번째부터 뺌 
        print(V, end = ' ')
        for i in range(1, N+1):
            if visited2[i] == 0 and graph[V][i] == 1:
                # 방문한 적 없거나 V와 연결되는지
                queue.append(i) # 있으면 큐에 넣기
                visited2[i] = 1 # 방문처리

dfs(V)
print()
bfs(V)