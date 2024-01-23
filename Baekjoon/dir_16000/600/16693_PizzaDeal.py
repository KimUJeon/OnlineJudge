import sys, math

A1, P1 = map(int, sys.stdin.readline().rstrip().split())
R1, P2 = map(int, sys.stdin.readline().rstrip().split())

per_dollar_1 = P1/A1
per_dollar_2 = P2/(R1**2*math.pi)

if per_dollar_1 < per_dollar_2:
    print("Slice of pizza")
else:
    print("Whole pizza")