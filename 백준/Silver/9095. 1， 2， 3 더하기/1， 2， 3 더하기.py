T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)

    for i in range(1, N+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])

"""
패턴 : 

dp[1] = 1
dp[2] = 2
dp[3] = 4 -> 1+1+1, 1+2, 2+1, 3
dp[4] = 7
dp[5] = 13
dp[6] = 24
dp[7] = 44

"""  