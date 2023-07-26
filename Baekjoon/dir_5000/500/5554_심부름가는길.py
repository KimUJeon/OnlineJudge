import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())

total = A + B + C + D
bun, cho = 0, 0

while total >= 60:
    total -= 60
    bun += 1

cho = total
print(bun)
print(cho)