import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
print("satisfactory" if m >= 8 else "unsatisfactory")