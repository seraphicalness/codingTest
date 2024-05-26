T = int(input())


for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [[0]*n for _ in range(k+1)]
    
    for i in range(n):
        dp[0][i] = i+1


    for i in range(1, k+1):  # 층 
        dp[i][0] = 1
        for j in range(1, n):   # 호 
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    print(dp[k][n-1])