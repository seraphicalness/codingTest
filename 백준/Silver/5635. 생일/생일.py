lst = []
n = int(input())

for i in range(n):
    name, day, month, year = input().split()
    lst.append([str(name), int(year), int(month), int(day)])
lst = sorted(lst, key=lambda x: (x[1], x[2], x[3]))
print(lst[n-1][0],lst[0][0], sep='\n')