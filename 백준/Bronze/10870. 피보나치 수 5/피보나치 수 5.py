n = int(input())

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)
#  n에 3을 넣으면 fibo(1) + fibo(2)로 나오고 ,
# fibo(2)가 fibo(1)+ fibo(0)이 됨

print(fibo(n))