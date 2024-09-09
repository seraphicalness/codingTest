n = int(input())
atm = sorted(list(map(int,input().split())))

hour = []
hour.append(atm[0])

for i in range(1, n):
    hour.append(hour[i-1]+atm[i])

# print(hour)
print(sum(hour))


