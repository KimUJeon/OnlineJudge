import sys

paper = str(sys.stdin.readline().rstrip())
words = str(sys.stdin.readline().rstrip())

result = paper.split(words)

print(len(result) - 1)
