burger = []
drink = []
total = []

for _ in range(3): burger.append(int(input()))

for _ in range(2): drink.append(int(input()))

for i in burger:
    for j in drink:
        total.append(i + j - 50)

print(min(total))