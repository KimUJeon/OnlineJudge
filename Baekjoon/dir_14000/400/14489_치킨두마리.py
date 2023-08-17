import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
C = int(sys.stdin.readline().rstrip())

two_chick = C * 2
if A+B >= two_chick:
    print((A+B)-two_chick)
else:
    print(A+B)