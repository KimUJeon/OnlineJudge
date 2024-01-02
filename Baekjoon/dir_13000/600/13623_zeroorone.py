import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

if A == B == C:
    print("*")
else:
    if A == B:
        print("C")
    elif B == C:
        print("A")
    elif A == C:
        print("B")