dp = [[0,0] for  _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]

T = int(input())

for _ in range(T):
    n = int(input())
    if n == 0:
        print(*dp[0])
    elif n == 1:
        print(*dp[1])
    else:
        for i in range(2, n+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
        
        print(dp[n][0],dp[n][1])