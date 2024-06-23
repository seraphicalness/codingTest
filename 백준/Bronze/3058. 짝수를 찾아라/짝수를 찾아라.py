for _ in range(int(input())):
    lst = list(map(int,input().split()))
    num = []
    for i in lst:
        if i % 2 == 0:
            num.append(i)
    print(sum(num), min(num))