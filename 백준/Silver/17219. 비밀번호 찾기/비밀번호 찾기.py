import sys 
input = sys.stdin.readline

A, B = map(int,input().strip().split())
dictn = {}

for _ in range(A):
    k, v = input().strip().split()
    dictn[k] = v

for _ in range(B):
    k = input().strip()
    print(dictn[k])