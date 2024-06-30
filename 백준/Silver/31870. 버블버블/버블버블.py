N = int(input())
A = list(map(int,input().split()))
B = A.copy()
count1 = 0
count2 = 0

for i in range(len(A)-1,0,-1):
    for j in range(i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            count1 += 1

for i in range(len(B)-1,0,-1):
    for j in range(i):
        if B[j] < B[j+1]:
            B[j], B[j+1] = B[j+1], B[j]
            count2 += 1
count2 += 1

# print(A, count1)
# print(B, count2)
print(min(count1, count2))
