import sys

N = int(sys.stdin.readline().rstrip())
A, B, C = map(int, sys.stdin.readline().rstrip().split())

print(min(A, N)+min(B, N)+min(C, N))
