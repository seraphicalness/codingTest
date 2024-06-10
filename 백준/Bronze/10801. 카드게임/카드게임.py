Acard = list(map(int,input().split()))
Bcard = list(map(int,input().split()))

Atotal = 0
BTotal = 0
D = 0


for i in range(10):
    if Acard[i] < Bcard[i]:
        BTotal += 1
    elif Acard[i] > Bcard[i]:
        Atotal += 1
    else:
        D += 1

if Atotal == BTotal:
    print("D")
elif max(Atotal, BTotal, D) == Atotal:
    print("A")
elif max(Atotal, BTotal, D) == BTotal:
    print("B")