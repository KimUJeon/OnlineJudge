import sys

count = 1
while True:
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    if nums[0] == 0 and len(nums) == 1:
        break
    else:
        print(f"Case {count}: Sorting... done!")
    count += 1