import sys

t = int(sys.stdin.readline())

for _ in range(t):
    sys.stdin.readline()
    cnt = 0
    lines = []
    r, c = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(r):
        lines.append(list(map(str, sys.stdin.readline().rstrip())))

    for i in range(r):
        for j in range(c - 2):
            if (
                ord(lines[i][j]) == 62
                and ord(lines[i][j + 1]) == 111
                and ord(lines[i][j + 2]) == 60
            ):
                cnt += 1
    for i in range(r - 2):
        for j in range(c):
            if (
                ord(lines[i][j]) == 118
                and ord(lines[i + 1][j]) == 111
                and ord(lines[i + 2][j]) == 94
            ):
                cnt += 1

    print(cnt)
