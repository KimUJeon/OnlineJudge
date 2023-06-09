import sys

X = int(sys.stdin.readline())
now = 64
count = 0

while True:
    if(now > X):
        now //= 2
    else:
        X -= now
        count += 1
        if X == 0:
            break

print(count)