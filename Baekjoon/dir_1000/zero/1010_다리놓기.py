import sys, math

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    result = math.comb(M, N)
    print(result)