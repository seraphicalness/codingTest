T = int(input())

for i in range(T):
    tri = sorted(list(map(int,input().split())))
    max_num = max(tri)
    if tri[0] + tri[1] > max_num:
        if tri[0] == tri[1] == tri[2]: print(f"Case #{i+1}: equilateral")
        elif tri[0] == tri[1] or tri[1] == tri[2] or tri[2] == tri[0]: print(f"Case #{i+1}: isosceles")
        else: print(f"Case #{i+1}: scalene")
    else:
        print(f"Case #{i+1}: invalid!")
