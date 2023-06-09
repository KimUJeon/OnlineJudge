import sys

ax, ay, az = map(int, sys.stdin.readline().rstrip().split())
cx, cy, cz = map(int, sys.stdin.readline().rstrip().split())

bx = cx - az
by = cy//ay
bz = cz - ax

print(bx, by, bz)