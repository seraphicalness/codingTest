N = int(input())
lst = list(map(int, input().split()))
M = int(input())
result = 0  # 출력해야 하는 최대 예산
start, end = 1, max(lst)  # 1을 시작, 최댓값을 끝

while start <= end: # end가 start보다 작으면 나옴 
    mid = (start + end) // 2  # 중앙 원소 고르기
    total = 0  # 예산의 합
    for l in lst: # lst값 하나씩 탐색 
        if l > mid: # l이 설정해둔 mid 보다 높으면 
            total += mid  # total에 mid 더하기 
        else:
            total += l # 작으면 l 더하기 
    if total <= M:  # M 이하 이면 중앙값+1 ~ 끝 값 다시 위로
        result = mid 
        start = mid + 1
    else:  # M초과 이면 시작 ~ 중앙값-1 값 다시 위로
        end = mid - 1
print(result)