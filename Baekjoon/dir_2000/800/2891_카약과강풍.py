import sys

N, S, R = map(int, sys.stdin.readline().split())
damaged = set(map(int, sys.stdin.readline().rstrip().split()))
addition = set(map(int, sys.stdin.readline().rstrip().split()))
result = 0

group = damaged & addition
damaged = list(damaged - group)
addition = list(addition - group)

if not damaged:
    result = 0
else:
    damaged.sort()

    for dead in damaged:
        if dead - 1 in addition:
            addition.remove(dead - 1)
        elif dead + 1 in addition:
            addition.remove(dead + 1)
        else:
            result += 1

print(result)
