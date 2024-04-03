# 3052
listn = []
i = 0
while i < 10:
    N = int(input())
    listn.append(N)
    i+=1

list2 = []
for j in listn:
    k = j % 42 
    list2.append(k)

k = set(list2)
print(len(k))