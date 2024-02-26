import sys

N = int(sys.stdin.readline().rstrip())
result = 0

for i in range(1, N + 1):
    result += pow(i, 3)
print(result)
