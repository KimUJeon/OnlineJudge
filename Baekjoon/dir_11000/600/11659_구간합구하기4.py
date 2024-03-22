import sys

A, M = map(int, sys.stdin.readline().rstrip().split())
N = list(map(int, sys.stdin.readline().rstrip().split()))
new_N = [0] + N

for idx in range(1, len(N) + 1):
    new_N[idx] = new_N[idx - 1] + N[idx - 1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    if i == 1:
        print(new_N[j])
    else:
        print(new_N[j] - new_N[i - 1])
