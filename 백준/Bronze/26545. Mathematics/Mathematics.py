
n = int(input())

# 합을 저장할 변수를 초기화
sum = 0

# n번 반복하여 정수를 입력받고 합에 더함
for _ in range(n):
    # 정수를 입력받습니다.
    num = int(input())
    # 합에 입력받은 정수를 더함
    sum += num
    
# 최종 합을 출력
print(sum)