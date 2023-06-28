import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
people = deque([i for i in range(1, N+1)])
yose = []
count = 1

while True:
    if len(people) > 0:
        if count == K:
            yose.append(str(people.popleft()))
            count = 1
        else:
            people.rotate(-1)
            count += 1
    else:
        break

print("<"+", ".join(yose)+">")