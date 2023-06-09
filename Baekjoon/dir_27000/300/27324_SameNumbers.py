import sys

N = list(sys.stdin.readline().rstrip())

if N[0] == N[1]:
    print(1)
else:
    print(0)