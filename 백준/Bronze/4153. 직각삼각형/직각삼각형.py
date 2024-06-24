while True:
    i = 0
    nums = list(map(int,input().split()))
    if sum(nums) == 0:
        break
    
    max_nums = max(nums)
    nums.remove(max_nums)
    if nums[0] ** 2 + nums[1] ** 2 == max_nums ** 2:
        print("right")
    else:
        print("wrong")