import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
if a%2 == 0 or b%2 == 0:
    print(0)
else:
    print(min(a, b))