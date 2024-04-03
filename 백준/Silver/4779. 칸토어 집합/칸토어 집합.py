def cantor(n):
    if n == 0 : # n이 0이 될 때
        print("-", end="") # 줄바꿈하지않고 -찍기
        return
    
    cantor(n-1) # 재귀함수 앞에 선 부분 호출해서 반복

    for i in range(3**(n-1)): # 3의 제곱 수 만큼 공백 찍기
        print(" ", end="")
    
    cantor(n-1) # 재귀함수 뒤에 선 부분 호출해서 반복

while True: # 여러번 입력받기 
    try:
        n = int(input())
        cantor(n)
        print()

    except:
        break