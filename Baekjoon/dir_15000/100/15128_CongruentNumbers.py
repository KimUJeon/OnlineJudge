import sys

while True:
    try:
        p1, q1, p2, q2 = map(int, sys.stdin.readline().rstrip().split())
    except ValueError:
        break

    result = p1/q1 * p2/q2 / 2

    if result%1 != 0:
        print(0)
    else:
        print(1)