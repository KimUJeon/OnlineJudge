import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

next_limit = 60 + k

if n > next_limit:
    print((n-next_limit) * 3000 + next_limit * 1500)
else:
    print(n * 1500)