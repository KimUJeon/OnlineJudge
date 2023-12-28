import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
if A == B:
    print(A)
else:
    print(max(A, B))