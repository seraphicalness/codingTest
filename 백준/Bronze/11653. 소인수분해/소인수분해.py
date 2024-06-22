n = int(input())

if n == 1:
    print('')
for i in range(2, n+1):
    if n % i == 0:
        while n % i == 0: # 수 나눌 수 없을 때까지 나누기 
            print(i)
            n = n / i