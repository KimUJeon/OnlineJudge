import sys

while True:
    x, y = map(float, sys.stdin.readline().rstrip().split())
    if x == 0 and y == 0:
        print("AXIS")
        break
    elif x == 0:
        print("AXIS")
    elif x > 0:
        if y > 0:
            print("Q1")
        elif y < 0:
            print("Q4")
        elif y == 0:
            print("AXIS")
    elif x < 0:
        if y > 0:
            print("Q2")
        elif y < 0:
            print("Q3")
        elif y == 0:
            print("AXIS")
