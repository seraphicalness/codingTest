
N = int(input())

num = list(map(int,input().split()))

count = 0

for i in num:
    for x in range(2, i+1): # 2부터시작(1은 소수아니니까)
        if i % x == 0: # num 에있는 요소가 나눠지는지?
            if x == i: # num이랑 나눠지는 수랑 같은지
                count += 1
            break # 나눠 떨어지는게 있으면 break

print(count)