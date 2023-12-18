import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    per_id, strat, manage, tech = map(int, sys.stdin.readline().rstrip().split())
    result = strat + manage + tech
    if strat >= 10.5 and manage >= 7.5 and tech >= 12 and result >= 55:
            print(f"{per_id} {result} PASS")
    else:
        print(f"{per_id} {result} FAIL")