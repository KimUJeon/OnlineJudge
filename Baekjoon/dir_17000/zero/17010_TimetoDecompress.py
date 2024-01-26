import sys

count = int(sys.stdin.readline().rstrip())
for _ in range(count):
    line = list(map(str, sys.stdin.readline().rstrip().split()))
    print(int(line[0]) * line[1])