N = int(input())
total = 0

def kg(N):
    for i in range(N):
        for j in range(N):
            if N - (3*i) - (5*j) == 0:
                total = i + j
                return total
            
    
    return -1


print(kg(N))