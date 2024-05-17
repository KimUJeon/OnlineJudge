import sys

box = [[0] * 100 for _ in range(100)]
cnt = 0
N, M = map(int, sys.stdin.readline().rstrip().split())

for _ in range(N):
    left_x, left_y, right_x, right_y = map(int, sys.stdin.readline().rstrip().split())
    for x in range(left_x, right_x + 1):
        for y in range(left_y, right_y + 1):
            box[x - 1][y - 1] += 1

for stack in box:
    for item in stack:
        if item > M:
            cnt += 1

print(cnt)
