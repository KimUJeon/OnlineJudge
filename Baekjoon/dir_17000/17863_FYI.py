import sys

nums = str(sys.stdin.readline().rstrip())

if nums[0:3] == "555":
    print("YES")
else:
    print("NO")