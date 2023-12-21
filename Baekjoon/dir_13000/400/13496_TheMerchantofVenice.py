import sys

K = int(sys.stdin.readline().rstrip())

for _ in range(K):
    result = 0
    n, s, d = map(int, sys.stdin.readline().rstrip().split())
    for cnt in range(n):
        di, vi = map(int, sys.stdin.readline().rstrip().split())
        if s*d >= di:
            result += vi

    print(f"Data Set {_+1}:\n{result}\n")