import sys

n = int(sys.stdin.readline().rstrip())
result = []
for _ in range(n):
    num = list(map(float, sys.stdin.readline().rstrip().split()))
    result.append(num[0] * num[1] * num[2])
for item in result:
    print(f"${item:.2f}")