import sys
from itertools import combinations

idx = 0
result = 0
N = int(sys.stdin.readline().rstrip())
people = []

for i in range(N):
    people.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    combis = list(combinations(people[i], 3))
    t = 0
    for combi in combis:
        if sum(combi) % 10 >= t:
            t = sum(combi) % 10

    if t >= result:
        result = t
        idx = i + 1

print(idx)
