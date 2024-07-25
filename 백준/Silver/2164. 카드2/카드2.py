from collections import deque
n = int(input())

card = deque(i for i in range(n, 0, -1))


while True:
    if len(card) == 1:
        print(card[0])
        break
    card.pop()
    q = card.pop()
    card.appendleft(q)