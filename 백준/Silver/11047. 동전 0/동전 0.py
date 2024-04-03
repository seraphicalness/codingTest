N, K = map(int,input().split())

listn = []

for i in range(N):
    a = int(input())
    listn.append(a)

total = 0
listn = listn[::-1]

for i in listn:
    if i <= K:
        total = total + (K // i)
        K = K % i 

print(total)

    
