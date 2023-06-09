import sys

w = int(sys.stdin.readline().rstrip())
if w % 2 == 0 and w > 2:
    print("YES")
else:
    print("NO")