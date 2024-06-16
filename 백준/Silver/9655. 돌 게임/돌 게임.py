N = int(input())
 
# 리스트 초기화 
# dp = [0 for i in range(N)]
# dp = [0] * N
dp = [0] * (1000 + 1)

dp[1] = 1 # 상근 승
dp[2] = 2 # 창영 승 
dp[3] = 1 # 상근 승 
 
for n in range(4, N+1):
    dp[n] = min(dp[n-1], dp[n-3]) + 1  # 이전의 턴 값을 이용 
    # 마지막에 이기는 사람이 이기기때문에 규칙에 따라 이전 턴 개수 + 1
    # 이전 턴에 1개 가져갔는지, 3개 가져갔는지 나눠서 생각
    # 둘 중 최소가 되는 값에 1을 더한 것이 +1이 최소 턴의 개수 
    # dp[n-3]을 연산하기 위해서 dp[1]~dp[3]까지는 값을 미리 지정
 
if dp[N] % 2 == 1:
    print('SK')
else:
    print('CY')

# 쉬운 코드 
# N = int(input())
 
# if N % 2 == 0 :
#     print("CY")
# else:
#     print("SK")