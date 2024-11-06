def dfs():
    if len(s) == m: # 출력 형식(길이)가 맞으면 s[]출력
        print(' '.join(map(str, s)))
        return # 출력하고 현재 들어온 dfs 빠져나오기 -- 2
    for i in range(1, n+1): 
        if visited[i]: # 방문했는지 확인
            continue # 방문했으면 계속
        visited[i] = True # 아니면 방문처리 
        s.append(i) # 방문하고 배열s에 넣기
        dfs() # 현재 i에 대해서 dfs -- 1
        s.pop() # 빠져나오고 이미 출력했으니까 pop -- 3
        visited[i] = False # 현재 i를 false 처리 
            

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()