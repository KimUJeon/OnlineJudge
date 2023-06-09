import sys

n = int(sys.stdin.readline().rstrip())
result = 0
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    result += num

print(result)