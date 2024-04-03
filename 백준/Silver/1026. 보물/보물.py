N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort(reverse=True)

listn = []

for i in range(0, N):
    result = A[i] * B[i]
    listn.append(result)

print(sum(listn))