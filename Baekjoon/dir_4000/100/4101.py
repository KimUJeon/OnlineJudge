while True:
    nums = list(map(int, input().split()))
    if nums[0] > nums[1]:
        print("Yes")
    elif nums[0] == 0 and nums[1] == 0:
        break
    else:
        print("No")
