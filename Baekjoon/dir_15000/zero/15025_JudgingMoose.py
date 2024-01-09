import sys

l, r = map(int, sys.stdin.readline().rstrip().split())

if l == r == 0:
    print("Not a moose")
elif l != r:
    print(f"Odd {max(l, r)*2}")
elif l == r:
    print(f"Even {l*2}")