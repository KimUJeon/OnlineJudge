import sys

X = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    price, item = map(int, sys.stdin.readline().rstrip().split())
    X -= price*item

if X == 0:
    print("Yes")
else:
    print("No")