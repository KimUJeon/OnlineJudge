import sys

while True:
    floor = int(sys.stdin.readline())
    result = 0

    if floor:
        for i in range(1, floor+1):
            result += i

        print(result)
    else:
        break