while(True):
    nums = list(map(int, input().split()))
    if nums[0] == 0 and nums[1] == 0:
        break
    elif nums[0]%nums[1] == 0:
        print("multiple")
    elif nums[1]%nums[0] == 0:
        print("factor")

    else:
        print("neither")
