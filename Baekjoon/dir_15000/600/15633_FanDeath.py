import sys

n = int(sys.stdin.readline().rstrip())
result = 0

for i in range(1, n + 1):
    if n % i == 0:
        result += i

result = result * 5 - 24
print(result)
