import sys

n = int(sys.stdin.readline().rstrip())
result = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    result.append(num)
for item in result:
    print(item, item)