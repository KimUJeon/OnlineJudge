import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    result = 0
    d = int(sys.stdin.readline().rstrip())
    for i in range(1, d):
        remain = d - i
        if i**2 <= remain:
            result = i
    print(result)
