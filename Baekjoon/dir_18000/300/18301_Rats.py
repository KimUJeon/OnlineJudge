import sys, math

n1, n2, n3 = map(int, sys.stdin.readline().rstrip().split())

top = (n1+1)*(n2+1)
down = (n3+1)
N = top/down - 1
print(math.floor(N))