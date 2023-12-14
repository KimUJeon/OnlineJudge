import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    if abs(number)%2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
