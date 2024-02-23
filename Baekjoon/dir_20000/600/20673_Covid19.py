import sys

p = int(sys.stdin.readline().rstrip())
q = int(sys.stdin.readline().rstrip())

if p <= 50 and q <= 10:
    print("White")
elif q > 30:
    print("Red")
else:
    print("Yellow")
