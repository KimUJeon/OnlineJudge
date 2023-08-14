import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())
sec = 0


if A < 0:
    while A < 0:
        A += 1
        sec += C
    sec += D

    while A < B:
        A += 1
        sec += E

else:
    while A < B:
        A += 1
        sec += E

print(sec)