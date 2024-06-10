import sys

N = int(sys.stdin.readline())
white = [[0] * 100 for _ in range(100)]
for _ in range(N):
    x1, y1 = map(int, sys.stdin.readline().rstrip().split())

    for i in range(y1, y1 + 10):
        for j in range(x1, x1 + 10):
            white[j][i] = 1

result = 0
for k in range(100):
    result += white[k].count(1)

print(result)
