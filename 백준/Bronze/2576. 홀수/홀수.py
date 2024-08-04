lst = []
odd = []
for _ in range(7): lst.append(int(input()))
for i in range(len(lst)):
    if lst[i] % 2 == 1: 
        odd.append(lst[i])

if len(odd) == 0:
    print(-1)
else:
    odd.sort()
    print(sum(odd),odd[0],sep="\n")