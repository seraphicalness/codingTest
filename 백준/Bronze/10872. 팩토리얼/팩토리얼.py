def factorial(number) -> int:
    result = 1
    for i in range(2, number+1):
        result = result * i
    return result

X = int(input())
print(factorial(X))