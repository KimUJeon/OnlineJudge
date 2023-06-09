import sys

bowls = []

for _ in range(3):
    bowls.append(int(sys.stdin.readline().rstrip()))

bowls.sort()

print(bowls[1])