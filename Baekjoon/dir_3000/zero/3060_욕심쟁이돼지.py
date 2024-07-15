import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    FOOD = int(sys.stdin.readline().rstrip())
    base_day = list(map(int, sys.stdin.readline().rstrip().split()))
    consume = sum(base_day)
    day = 1

    while True:
        if consume <= FOOD:
            day += 1
            consume *= 4
        else:
            break

    print(day)
