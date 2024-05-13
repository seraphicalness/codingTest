N = int(input())

i = list(map(int,input()))

total = 0
for k in range(N):
    total = total + i[k]
    
print(total)