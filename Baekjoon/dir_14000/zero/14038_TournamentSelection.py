import sys

flag = 0
for _ in range(6):
    game = sys.stdin.readline().rstrip()
    if game == "W":
        flag += 1

if flag >= 5:
    print(1)
elif flag >= 3:
    print(2)
elif flag >= 1:
    print(3)
else:
    print(-1)