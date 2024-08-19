alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

str = input()

for a in alphabet:
    # 문자열을 찾으면, 아예 알파벳이 아닌 0으로 값 바꾸기 (replace 함수 이용)
    str = str.replace(a, "0")

# 마지막으로 문자열의 길이를 출력하면, 크로아티아 알파벳은 0으로 바뀌어있기 때문에 개수가 1개로 계산
# 크로아티아 알파벳이 아닌 것들도 그대로 개수가 계산됨.
print(len(str))