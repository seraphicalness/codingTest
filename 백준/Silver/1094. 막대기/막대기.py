X = int(input())
A = [64, 32, 16, 8, 4, 2, 1]
count = 0 

for i in A:
    if i <= X:
        count += 1
        X -= i
print(count)