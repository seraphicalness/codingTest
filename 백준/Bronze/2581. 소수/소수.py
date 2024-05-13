M = int(input())
N = int(input())
sum = 0
lst = []

def prime(num):
    if num < 2: # 2 밑이면 False
        return False
    else:
        i = 2 # 2부터 확인
        while i * i <= num: # 범위 확인 
            if num % i == 0: # 나눠지면 소수아님
                return False
            i += 1 # 1 증가
    # listnum.append(num)
    return True  # 위에 과정 통과하면 리턴 

for i in range(M, N+1):
    if prime(i):
        sum += i
        lst.append(i)
if sum == 0:
    print("-1")

else:
    print(sum)
    print(min(lst))