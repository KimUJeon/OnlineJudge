import sys

x, y = map(int, sys.stdin.readline().rstrip().split())

if y < x:
    print(x+y)
else:
    print(y-x)