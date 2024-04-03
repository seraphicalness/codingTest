N = int(input())
for k in range(N):
    T,S = input().split()
    T = int(T)
    S =list(str(S))

    for i in S:
        j = i * T
        print(j,end="")
    print()