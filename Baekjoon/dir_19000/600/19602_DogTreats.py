import sys

S = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
L = int(sys.stdin.readline().rstrip())

if S*1+M*2+L*3 >= 10:
    print("happy")
else:
    print("sad")