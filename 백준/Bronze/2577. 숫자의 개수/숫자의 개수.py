A = int(input())
B = int(input())
C = int(input())

total = A * B * C
result = []
while total > 0:
    temp = total % 10
    result.insert(0, temp)
    total //= 10 
    
for i in range(10):
    a = result.count(i)
    print(a, end="\n")