N, M = map(int,input().split())
basket = list(range(1, N+1))

for k in range(M):
    i, j = map(int,input().split()) 
    change = basket[i-1:j]
    change = change[::-1]
    basket[i-1:j] = change

print(*basket)