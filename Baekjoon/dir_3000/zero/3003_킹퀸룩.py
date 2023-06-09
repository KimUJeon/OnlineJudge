import sys

origin_nums = [1, 1, 2, 2, 2, 8]
found_nums = list(map(int, sys.stdin.readline().rstrip().split()))
need_nums = []

for i in range(6):
    need_nums.append(str(origin_nums[i]-found_nums[i]))

print(" ".join(need_nums))