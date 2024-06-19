import sys 
n = int(sys.stdin.readline())
dp = [0] * 1001
dp[1] = 1  # 2 * 1 일 때, 1가지
dp[2] = 2  # 2 * 2 일 때, 2가지

for i in range(3, n+1): # 3부터 확인 
    dp[i] = (dp[i-1] + dp[i-2]) % 10007 # 앞에 두 개 더한거
    
print(dp[n])