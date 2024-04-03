n = int(input())
total = 1
res = 1

for i in range(n):
    if i > 0:
        total = i * (i+1)
        res = res * (total // i)

print(res)