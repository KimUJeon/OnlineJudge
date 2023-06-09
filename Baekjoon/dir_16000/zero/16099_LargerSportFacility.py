import sys

N = int(sys.stdin.readline())
for _ in range(N):
    lt, wt, le, we = map(int, sys.stdin.readline().rstrip().split())

    if lt*wt > le*we:
        print("TelecomParisTech")
    elif lt*wt < le*we:
        print("Eurecom")
    else:
        print("Tie")