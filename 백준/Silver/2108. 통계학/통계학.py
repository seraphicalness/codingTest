import sys
input = sys.stdin.readline

# 입력
n = int(input())
lst = [int(input()) for i in range(n)]

# 1. 산술평균
print(round(sum(lst)/n))

# 2. 중앙값
lst.sort()
print(lst[n//2])

# 3. 최빈값
cnt = dict()
for i in lst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

# 최빈값이 여러 개 존재하는 경우
mx = max(cnt.values())
mx_lst = []

for i in cnt:
    if cnt[i] == mx:
        mx_lst.append(i)

# 두 번째로 작은 값을 출력
print(mx_lst[0]) if len(mx_lst) == 1 else print(mx_lst[1])
    
# 4. 범위
print(max(lst)-min(lst))
