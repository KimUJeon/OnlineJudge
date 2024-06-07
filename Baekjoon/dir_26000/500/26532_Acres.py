import sys

x, y = map(int, sys.stdin.readline().split())
total = x * y

result = total / 4840 / 5
print(result.__ceil__())
