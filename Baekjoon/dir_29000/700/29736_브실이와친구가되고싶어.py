import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
K, X = map(int, sys.stdin.readline().rstrip().split())
cnt = 0

for i in range(A, B+1):
    if i >= (K-X) and i <= (K+X):
        cnt += 1
    else:
        pass

if cnt == 0:
    print("IMPOSSIBLE")
else:
    print(cnt)