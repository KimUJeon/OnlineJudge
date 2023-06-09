import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
if N < M/100:
    print("No")
else:
    print("Yes")