N = int(input())
arr = []

# life = 100
# happy = 0

A = list(map(int,input().split()))
B = list(map(int,input().split()))
for i in range(N):
    arr.append((A[i], B[i]))

dp = [0 for _ in range(100)]  
# 체력이 100이므로 100 정도는 봐줘야할것같음 

for j in arr:
    a, b = j # a는 체력, b는 행복
    for k in range(99, a-1, -1):
        dp[k] = max(dp[k], dp[k-a]+b)
    # k로 들어오는 인덱스랑, k에서 체력빼주고 행복 더한거 비교
print(max(dp))