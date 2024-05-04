num = list(map(int,input().split()))

min = min(num)

while True:
    count = 0
    for i in num:
        if min % i == 0:
            count += 1
    if count > 2:
        break
    min += 1

print(min)