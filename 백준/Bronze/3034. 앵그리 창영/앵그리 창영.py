n, w, h = map(int,input().split())

ran = w**2 + h**2

for _ in range(n):
    a = int(input())
    if a**2 > ran: print("NE")
    else: print("DA")