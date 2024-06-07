lst = []

for _ in range(int(input())):
    for _ in range(int(input())):
        lst.append(list(map(str, input().split())))

    lst = sorted(lst, key=lambda x : int(x[1]), reverse=True)
    print(lst[0][0])