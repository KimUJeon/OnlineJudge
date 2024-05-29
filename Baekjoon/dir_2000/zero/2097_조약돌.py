import sys

N = int(sys.stdin.readline().rstrip())
w, h = 0, 0

for i in range(1, N + 1):
    box = (i + 1) * (i + 1)
    if box < N:
        box = (i + 2) * (i + 1)
        if box < N:
            pass
        else:
            w = i + 1
            h = i
            break
    else:
        w, h = i, i
        break

print(w * 2 + h * 2)
