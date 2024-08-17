n = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort() #정렬해준다!!.
s = 0  # 시작 포인터
e = n - 1  # 끝 포인터
count = 0
while s < e:  # 두 포인터가 엇갈리지 않을 때 까지

    # 만약 합이 똑같다면
    if array[s] + array[e] == x:
        count += 1  # 횟수 +1
        s += 1  # s 포인터를 한칸 앞으로 이동
    elif array[s] + array[e] > x:  # 만약 크다면
        e -= 1  # 끝 포인터를 한칸 앞으로 땡긴다.
    else:  # 만약 작다면
        s += 1  # 시작 포인터를 한칸 앞으로 땡긴다.

print(count)