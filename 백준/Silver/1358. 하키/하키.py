import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
r = h // 2
count = 0

def is_in_circle_left(a, b, x, y, r): return (a - x) ** 2 + (b - (y + h / 2)) ** 2 <= r ** 2

def is_in_circle_right(a, b, x, y, r): return (a - (x + w)) ** 2 + (b - (y + h / 2)) ** 2 <= r ** 2

for _ in range(p):
    a, b = map(int, input().split())
    
    if is_in_circle_left(a, b, x, y, r): count += 1
    elif x <= a <= x + w and y <= b <= y + h: count += 1
    elif is_in_circle_right(a, b, x, y, r): count += 1

print(count)