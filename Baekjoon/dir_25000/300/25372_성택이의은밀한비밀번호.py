import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    password = sys.stdin.readline().rstrip()
    if 6 <= len(password) <= 9:
        print("yes")
    else:
        print("no")