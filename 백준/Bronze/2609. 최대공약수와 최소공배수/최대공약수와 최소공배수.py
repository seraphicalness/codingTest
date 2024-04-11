a, b = map(int,input().split())

def gcd(a, b): # 최대공약수
    if b == 0: # b가 0이면 a 반환
        return a
    else: # b가 아니면 재귀 호출, 자리바꿔서 
        # a 자리에 b를 넣고 b 자리에 a 나머지 b 를 넣어서
        # b가 0이 될때까지 호출 
        return gcd(b, a % b) 
    

def lcm(a, b): # 최소공배수 
    res = (a * b) // gcd(a, b) # a b 를 곱하고 최대공약수로 나눠줌
    return res

print(gcd(a, b))
print(lcm(a, b))

        