a, b = map(int,input().split())
lis = list(map(int,input().split()))

total = 0
res = 0

for i in lis:
    total += i
    if total >= b:
        res += 1
    if total < 0:
        total = 0

print(res)