import sys

UR, TR, UO, TO = map(int, sys.stdin.readline().rstrip().split())

print(56*UR + 24*TR + 14*UO + 6*TO)