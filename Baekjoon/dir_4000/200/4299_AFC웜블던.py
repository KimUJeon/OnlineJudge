import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
if a+b < 0 or a-b < 0 or (a+b) % 2:
    print(-1)
else:
    s = (a + b) // 2
    m = a - s
    print(max(s, m), min(s, m))