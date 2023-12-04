import sys

n = int(sys.stdin.readline().rstrip())

result = 1
for item in range(1, 1+n, 1):
    result *= item
print(list(str(result))[-1])