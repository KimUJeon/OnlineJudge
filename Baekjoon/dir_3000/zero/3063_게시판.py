import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().rstrip().split())
    result = (x2 - x1) * (y2 - y1) - (
        max((min(x2, x4) - max(x1, x3)), 0) * max((min(y2, y4) - max(y1, y3)), 0)
    )

    print(result)
