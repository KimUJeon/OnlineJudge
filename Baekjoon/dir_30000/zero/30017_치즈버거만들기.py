import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
floor = 0
A -= 1

while True:
    if A >= 1 and B >= 1:
        A -= 1
        B -= 1
        floor += 2
    else:
        break
print(floor+1)