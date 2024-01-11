import sys

food = list(map(int, sys.stdin.readline().rstrip().split()))
people = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0

for idx in range(3):
    gap = food[idx]-people[idx]
    if gap < 0:
        result += abs(gap)

print(result)