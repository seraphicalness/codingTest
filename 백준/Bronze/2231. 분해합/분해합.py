def Num(n):
    total = 0
    while n > 0:
        temp = n % 10
        total += temp
        n //= 10
    return total

N = int(input())
# result = 0

for i in range(1, N+1):
    if (i + Num(i)) == N:
        print(i)
        break

if i == N:
    print(0)