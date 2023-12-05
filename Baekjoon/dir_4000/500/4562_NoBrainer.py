import sys

tries = int(sys.stdin.readline().rstrip())
for _ in range(tries):
    have, need = map(int, sys.stdin.readline().rstrip().split())

    if have < need:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")