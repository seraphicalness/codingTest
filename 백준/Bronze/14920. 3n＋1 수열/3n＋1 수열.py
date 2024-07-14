c = int(input())
n = 1

while c > 1:
    if c % 2 == 0: 
        c //= 2
        n += 1
    else: 
        c = 3*c + 1
        n += 1

print(n)