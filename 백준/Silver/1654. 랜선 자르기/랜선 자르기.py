k, n = map(int,input().split())
lanson = []

for _ in range(k) : lanson.append(int(input()))

start, end = 0, 10000000000
answer = 0

while start <= end:
    mid = (start + end) // 2
    num = 0
    for len in lanson:
        num += len // mid  # 랜선 길이를 mid로 나눈 개수를 저장 
    if num >= n: # n 이 저장한 개수보다 작으면 
        start = mid + 1 # 중간값보다 올려줌 
        if mid > answer: 
            answer = mid 
    else:
        end = mid -1

print(answer)