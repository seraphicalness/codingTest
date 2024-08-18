N, M = map(int,input().split())
lst = []
total = 0

for _ in range(N):
    lst.append(input())

for _ in range(M):
    s = input()
    if s in lst: total +=1

print(total)