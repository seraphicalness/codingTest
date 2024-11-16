lowerRainbow = ["r", "o", "y", "g", "b", "i", "v"]
upperRainbow = ["R", "O", "Y", "G", "B", "I", "V"]

N = int(input())
word = input()
lowerCheck = upperCheck = True

for i in range(7):
    if lowerRainbow[i] not in word:
        lowerCheck = False
    if upperRainbow[i] not in word:
        upperCheck = False

if lowerCheck and upperCheck:
    print("YeS")
elif lowerCheck:
    print("yes")
elif upperCheck:
    print("YES")
else:
    print("NO!")
