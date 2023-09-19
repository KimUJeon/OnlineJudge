import sys

N = int(sys.stdin.readline().rstrip())
min_time = 1e9


for _ in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    if A <= B or A == B:
        min_time = min(B, min_time)

if min_time == 1e9:
    print(-1)
else:
    print(min_time)