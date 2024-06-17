lst = []
length = []
for _ in range(5):
    arr = input()
    lst.append(arr) 
    length.append(len(arr))  # 문자열 길이도 append

for i in range(15):
    for j in range(5):
        if i< length[j]: # j가 length[i]범위를 벗어난다면 글자추가 안일어남 
            print(lst[j][i], end="")