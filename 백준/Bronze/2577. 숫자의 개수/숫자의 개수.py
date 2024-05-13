A = int(input())
B = int(input())
C = int(input())

total = A * B * C
result = [] 
while total > 0: # result에 total을 분해해서 들어가게 반복, 0이상일때만 
    temp = total % 10
    result.insert(0, temp)
    total //= 10 
    
for i in range(10): # 0부터 9까지 
    a = result.count(i) # 원소 카운트해서 출력 
    print(a, end="\n")