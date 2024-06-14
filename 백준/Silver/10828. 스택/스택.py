import sys
# input = sys.stdin.readline()
stack = []
for _ in range(int(sys.stdin.readline())):
        menu = list(map(str, sys.stdin.readline().split()))
        if menu[0] == "push": stack.append(menu[1])
        elif menu[0] == "pop": 
            if len(stack) == 0: print(-1)
            else: print(stack.pop())
        elif menu[0] == "size": print(len(stack))
        elif menu[0] == "empty":
            if len(stack) == 0: print(1)
            else: print(0)
        elif menu[0] == "top":
            if len(stack) == 0 : print(-1)
            else: print(stack[-1])