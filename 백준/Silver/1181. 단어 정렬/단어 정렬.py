dictn = {}
for _ in range(int(input())):
    words = input()
    dictn[words] = len(words)

res = sorted(dictn.items(), key=lambda x : (x[1], x[0]))
for i in res:
    print(i[0])