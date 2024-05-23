N, K = map(int,input().split())  # 물품 수, 총 무게
items = []
for i in range(N):
    W, V = map(int,input().split()) # 무게, 가치
    items.append((W, V))

dp = [ 0 for i in range(K+1)]
for item in items:
    w, v= item
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)
         # dp의 원래 인덱스와 dp[i-무게] + 가치의 값을 비교

print(dp[-1]) # 제일 큰 가치 값 