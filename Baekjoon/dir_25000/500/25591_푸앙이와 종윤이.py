import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

a = 100 - A
b = 100 - B
c = 100 - a - b
d = (a * b)
q = d//100
r = d%100

print(a, b, c, d, q, r)
print(c+q, r)