while True:
    tri = list(map(int,input().split()))
    if tri[0] == tri[1] == tri[2] == 0:
        break
    tri.sort()

    if tri[0] == tri[1] == tri[2]:
        print("Equilateral")
    elif max(tri) >= sum(tri) - max(tri):
        print("Invalid")
    elif tri[0] == tri[1] or tri[1] == tri[2] or tri[0] == tri[2]:
        print("Isosceles")
    else:
        print("Scalene")
