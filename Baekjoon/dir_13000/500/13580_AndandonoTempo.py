import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())
if A+C == B or A+B == C or B+C == A or A == B or A == C or B ==C:
    print("S")
else:
    print("N")