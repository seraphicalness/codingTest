N = int(input())
a = ((N % 10) * 10) + (((N // 10) + (N % 10)) % 10)
count = 1

while a != N:
    a = ((a % 10) * 10) + (((a // 10) + (a % 10)) % 10)
    count += 1

print(count)