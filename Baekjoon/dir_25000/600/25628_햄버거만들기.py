import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

print(min(A//2, B))