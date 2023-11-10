import sys

D, H, M = map(int, sys.stdin.readline().rstrip().split())
end = D*24*60 + H *60 + M
start = 11*24*60 + 11*60 + 11
result = end - start

if result >= 0:
    print(result)
else:
    print(-1)