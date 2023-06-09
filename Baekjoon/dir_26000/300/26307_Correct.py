import sys

H, M = map(int, sys.stdin.readline().rstrip().split())
H = H - 9

print(60*H + M)