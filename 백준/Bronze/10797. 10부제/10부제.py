num = int(input())
lst = list(map(int,input().split()))
count = 0

for i in lst:
    if i == num:
        count += 1
    else:
        continue
print(count)