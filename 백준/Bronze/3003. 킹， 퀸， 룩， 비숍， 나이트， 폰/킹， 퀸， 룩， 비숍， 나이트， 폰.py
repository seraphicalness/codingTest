chess = [1, 1, 2, 2, 2, 8]

inn = list(map(int, input().split()))

for i in range(len(inn)):
    print(chess[i] - inn[i], end=" ")