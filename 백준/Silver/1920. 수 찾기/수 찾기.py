N = int(input())
N_list = list(map(int,input().split()))
N_list.sort()

def binery(t):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2

        if N_list[mid] == t: # 값 찾았을때
            print(1)
            return
        elif N_list[mid] <= t: # 중앙값이 목표값보다 작을때
            start = mid + 1 # 시작을 중앙에서 1올림
        else:                  # 중앙값이 목표값보다 클때
            end = mid - 1 # 끝을 중앙에서 1내림 
    print(0)
    return

M = int(input())
M_list = list(map(int,input().split()))

for i in range(M):
    binery(M_list[i])