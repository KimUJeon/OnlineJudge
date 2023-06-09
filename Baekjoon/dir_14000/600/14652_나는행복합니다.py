import sys

N, M, K= map(int, sys.stdin.readline().rstrip().split())

i = K//M
j = K - (M*i)
print(i, j)
