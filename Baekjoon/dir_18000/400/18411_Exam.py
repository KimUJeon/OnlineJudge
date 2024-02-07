import sys

scores = list(map(int, sys.stdin.readline().rstrip().split()))
scores.sort(reverse=True)

print(scores[0]+scores[1])