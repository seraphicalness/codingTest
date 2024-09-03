
dp = [[0,0]] * 46
dp[0] = [1,0] # "A"
dp[1] = [0,1] # "B"
# dp[3] = [1,1] # "BA"
# dp[4] = [1,2] # "BAB"
# dp[5] = [2,3] # "BABBA"
# dp[6] = [3,5]
# dp[7] = [5,8] 
#         [8,]

n = int(input())
for i in range(2, n+1):
    dp[i] = [dp[i-1][1], dp[i-1][0]+dp[i-1][1]]

print(dp[n][0], dp[n][1],sep=" ")