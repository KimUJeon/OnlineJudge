import sys

T = int(sys.stdin.readline().rstrip())
lines = list(map(int, sys.stdin.readline().rstrip().split()))

print(lines.count(T))