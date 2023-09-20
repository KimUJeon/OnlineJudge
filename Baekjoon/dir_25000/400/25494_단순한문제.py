import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    print(min(a,b,c))