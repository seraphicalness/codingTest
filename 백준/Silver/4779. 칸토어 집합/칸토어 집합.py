def cantor(n):
    if n == 0 :
        print("-", end="")
        return
    
    cantor(n-1)

    for i in range(3**(n-1)):
        print(" ", end="")
    
    cantor(n-1)

while True:
    try:
        n = int(input())
        cantor(n)
        print()

    except:
        break