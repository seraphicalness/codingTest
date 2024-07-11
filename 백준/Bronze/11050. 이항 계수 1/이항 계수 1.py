N, K = map(int,input().split())

def factorial(a):
    if a == 1 or a == 0:
        return 1
    return a * factorial(a-1)

print(factorial(N) // (factorial(K) * factorial(N-K)))