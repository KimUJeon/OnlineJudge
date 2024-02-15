import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    line = sys.stdin.readline().rstrip()
    flag = len(line)
    for idx, val in enumerate(line):
        if val == "D":
            flag = idx
            break
    print(flag)