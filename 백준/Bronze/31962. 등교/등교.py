N, K = map(int,input().split())
lis = []

for i in range(N):
    S, T = map(int,input().split())
    if S+T > K: pass
    else: lis.append(S)

if len(lis) == 0: print(-1)
else: print(max(lis))
