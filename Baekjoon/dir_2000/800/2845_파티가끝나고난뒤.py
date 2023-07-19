import sys

L, P = map(int, sys.stdin.readline().rstrip().split())
people = list(map(int, sys.stdin.readline().rstrip().split()))

result = []

for item in people:
    result.append(str(item - (L*P)))

print(" ".join(result))