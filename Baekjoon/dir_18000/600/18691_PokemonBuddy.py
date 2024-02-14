import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 1:
        print((c-b)*1 if c-b>0 else 0)
    elif a == 2:
        print((c-b)*3 if c-b>0 else 0)
    else:
        print((c-b)*5 if c-b>0 else 0)
