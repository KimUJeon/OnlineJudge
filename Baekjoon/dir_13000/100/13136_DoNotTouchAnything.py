import sys

R, C, area = map(int, sys.stdin.readline().rstrip().split())
if R%area != 0:
    R = R//area + 1
else:
    R //= area
if C%area != 0:
    C = C//area + 1
else:
    C //= area

result = R * C
print(result)