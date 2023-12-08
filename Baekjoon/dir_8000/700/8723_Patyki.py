import sys

sticks = list(map(int, sys.stdin.readline().rstrip().split()))

def angle(a, b, c):
    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        return True
    elif pow(b, 2) + pow(c, 2) == pow(a, 2):
        return True
    elif pow(c, 2) + pow(a, 2) == pow(b, 2):
        return True

if len(set(sticks)) == 1:
    print(2)
elif angle(sticks[0], sticks[1], sticks[2]):
    print(1)
else:
    print(0)