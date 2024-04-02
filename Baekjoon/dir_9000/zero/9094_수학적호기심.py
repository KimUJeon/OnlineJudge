import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    count = 0
    n, m = map(int, sys.stdin.readline().rstrip().split())
    for i in range(1, n + 1):
        for j in range(i + 1, n):
            result = (i**2 + j**2 + m) % (i * j)
            if result == 0:
                count += 1

    print(count)
