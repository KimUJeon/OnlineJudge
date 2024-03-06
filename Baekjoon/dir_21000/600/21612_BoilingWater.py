import sys

B = int(sys.stdin.readline().rstrip())
result = 5 * B - 400

if result > 100:
    print(result)
    print(-1)
elif result == 100:
    print(result)
    print(0)
else:
    print(result)
    print(1)
