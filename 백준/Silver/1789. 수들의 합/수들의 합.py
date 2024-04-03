s = int(input())


total = 0
res = 0


while(s>0):
    if s == 0:
        break
    if s > 0:
        total = total + 1
        res = res + total
        s = s - total -1

print(total)