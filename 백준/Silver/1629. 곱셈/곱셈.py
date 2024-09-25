a, b, c = map(int,input().split())
res = 1
# b = 11
# 1011
while b>0:
    if b % 2 == 1:  # 홀수이면 
        res = res * a % c
    b //= 2  # b를 2로 나누면서 다음으로 확인 
    a = a * a % c# a를 스스로 제곱해서 다음을 검토하려고함 

print(res)