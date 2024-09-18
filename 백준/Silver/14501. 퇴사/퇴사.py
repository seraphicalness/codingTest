n = int(input())

dp = [0] * (n+1)
money = []
day = []
max_value = 0

for _ in range(n):
    a, b = map(int,input().split())
    day.append(a)
    money.append(b)

for i in range(n-1, -1, -1): # 뒤에서부터 봄 
    time = day[i] + i  # i번째 걸리는 날 + i를 더한 값
    if time <= n:  # n보다 작을때만 작동
        dp[i] = max(money[i] + dp[time], max_value)
        max_value = dp[i]
    else: dp[i] = max_value # 날짜를 초과할 경우 

print(max_value)