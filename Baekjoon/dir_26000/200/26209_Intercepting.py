import sys

nums = list(map(int, sys.stdin.readline().rstrip().split()))
if 9 in nums:
    print("F")
else:
    print("S")