import sys

A, C, E = map(int, sys.stdin.readline().rstrip().split())
x, y, z = map(int, sys.stdin.readline().rstrip().split())

if x >= A and y >= C and z >= E:
    print("A")
elif x >= A / 2 and y >= C and z >= E:
    print("B")
elif y >= C and z >= E:
    print("C")
elif z >= E and y >= C / 2:
    print("D")
elif z >= E:
    print("E")
