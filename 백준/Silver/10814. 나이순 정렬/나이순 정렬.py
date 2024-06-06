li = []

for _ in range(int(input())):
    li.append(list(map(str, input().split())))

li = sorted(li, key=lambda x : int(x[0])) # 매개변수 x의 0번째부터 본다

for i in li:
    print(i[0], i[1])