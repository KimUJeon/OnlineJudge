import sys

N = int(sys.stdin.readline().rstrip())
spend_time = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0

spend_time.sort()

for i in range(len(spend_time)):
    for idx in range(0, i + 1):
        result += spend_time[idx]

print(result)
