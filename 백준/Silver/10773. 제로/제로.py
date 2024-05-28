K = int(input())
lst = []
total = 0

for _ in range(K):
    n = int(input())
    lst.append(n)
    if n == 0:
        lst.pop()
        lst.pop()
    else:
        continue

for i in range(len(lst)):
    total += lst[i]

print(total)