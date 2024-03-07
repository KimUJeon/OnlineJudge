import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

print(b if a >= b else a + 1)
