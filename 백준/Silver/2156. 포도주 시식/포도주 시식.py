dp = [0] * 10001
glass = [0] * 10001

n = int(input())
for i in range(1, n+1):
    glass[i] = int(input())

dp[1] = glass[1] # dp[1]에 첫 포도주잔 (1번째 위치에서 가장많은 양 마시는 경우)
dp[2] = glass[1] + glass[2] # dp[2]에 첫 + 두번째 포도주잔 (2번째 위치에서 가장 많은 양 마시는 경우)
# 3번째부터는 연속 3번 마시면 안돼서 X
# for 문을 3부터 돌림 
for i in range(3, n+1): # n번째 위치에서 가장 많이 마시는 경우 
    dp[i] = max(dp[i-1], dp[i-2]+glass[i], dp[i-3]+glass[i-1]+glass[i])
# 연속 놓여진 3잔 마실수 없다

print(dp[n])