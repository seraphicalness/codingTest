n = int(input())

for i in range(n):
    lst = input()
    total = 0   
    score = 0
    
    for j in lst:    
        if j == "O":
            score +=1 
        else:
            score = 0    
        total += score

    print(total)

       