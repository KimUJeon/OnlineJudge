import sys

young = int(sys.stdin.readline().rstrip())
mid = int(sys.stdin.readline().rstrip())

old = mid + (mid-young)
print(old)