import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
print(min(M, K) + N - max(M, K))