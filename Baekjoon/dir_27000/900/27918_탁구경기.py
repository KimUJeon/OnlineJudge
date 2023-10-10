import sys

x, y = 0, 0
flag = False
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    score = sys.stdin.readline().rstrip()
    if score == "D":
        x += 1
    else:
        y += 1

    if abs(x-y) >= 2:
        print(f"{x}:{y}")
        flag = True
        break

if flag:
    pass
else:
    print(f"{x}:{y}")