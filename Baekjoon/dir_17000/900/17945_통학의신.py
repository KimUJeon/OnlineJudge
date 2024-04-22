import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
solve = []

for i in range(-1000, 1001, 1):
    result = pow(i, 2) + (2 * A * i) + B
    if result == 0:
        solve.append(i)

    if len(solve) == 2:
        break

print(*solve)
