import sys

univs = list(map(int, sys.stdin.readline().rstrip().split()))
if sum(univs) >= 100:
    print("OK")
else:
    idx = univs.index(min(univs))
    if idx == 0:
        print("Soongsil")
    elif idx == 1:
        print("Korea")
    elif idx == 2:
        print("Hanyang")