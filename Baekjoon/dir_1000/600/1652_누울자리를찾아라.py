import sys

N = int(sys.stdin.readline().rstrip())
w_cnt = 0
h_cnt = 0
rooms = []

for _ in range(N):
    block = list(sys.stdin.readline().rstrip())
    rooms.append(block)

for room in rooms:
    cnt = 0
    for item in room:
        if item == ".":
            cnt += 1
        else:
            if cnt >= 2:
                w_cnt += 1
            cnt = 0
    if cnt >= 2:
        w_cnt += 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if rooms[j][i] == ".":
            cnt += 1
        else:
            if cnt >= 2:
                h_cnt += 1
            cnt = 0
    if cnt >= 2:
        h_cnt += 1

print(w_cnt, h_cnt)
