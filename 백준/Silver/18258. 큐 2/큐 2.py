from collections import deque
import sys 
n = int(sys.stdin.readline())

queue = deque([])
for _ in range(n):
    t = sys.stdin.readline().split()
    if t[0] == "push":
        queue.append(t[1])
    elif t[0] == "pop":
        if not queue: print(-1)
        else: print(queue.popleft())
    elif t[0] == "size":
        print(len(queue))
    elif t[0] == "empty":
        if not queue: print(1)
        else: print(0)
    elif t[0] == "front":
        if not queue: print(-1)
        else: print(queue[0])
    elif t[0] == "back":
        if not queue: print(-1)
        else: print(queue[-1])