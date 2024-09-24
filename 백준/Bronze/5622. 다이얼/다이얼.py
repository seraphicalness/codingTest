# 다이얼 나타내기
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# 알파벳 단어 입력 받기
word = list(input())
result = 0  # 결과값 초기화

# 반복문
for i in word:
    for j in dial:
        if i in str(j):  # 문자열 j에 있다면
            num = dial.index(j) + 3  # 다이얼을 걸기위한 시간
            result += num  # 걸리는 시간 모두 구하기

print(result)