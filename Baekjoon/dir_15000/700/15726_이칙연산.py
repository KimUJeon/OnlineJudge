import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())
result1 = A*B/C
result2 = A/B*C

print(int(max(result1, result2)))