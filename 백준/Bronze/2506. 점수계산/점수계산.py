n = int(input())
pro = list(map(int,input().split()))
# score = 0
check = [0] * (n+1)

for i in range(n):
    if pro[i] == 1:
        # score += 1
        if i == 0:
            check[i] = check[i] + 1
        check[i] = check[i-1] + 1
    else: check[i] = 0

print(sum(check))