import sys

M, S, G = map(int, sys.stdin.readline().rstrip().split())
A, B = map(float, sys.stdin.readline().rstrip().split())
L, R = map(int, sys.stdin.readline().rstrip().split())

left_wait = L / A
right_wait = R / B

lv = M / G + 1 if M % G else M / G
rv = M / S + 1 if M % S else M / S

if lv + left_wait < rv + right_wait:
    print("friskus")
else:
    print("latmask")
