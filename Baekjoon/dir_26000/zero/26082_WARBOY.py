import sys

a,b,c = map(int, sys.stdin.readline().rstrip().split())
ab = b//a
cperfo = ab * 3

result = cperfo * c
print(result)