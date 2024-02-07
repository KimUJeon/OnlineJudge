import sys

nums = list(map(int, sys.stdin.readline().rstrip().split()))
print(1 if nums.count(1) > nums.count(2) else 2)