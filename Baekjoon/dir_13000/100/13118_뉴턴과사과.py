import sys

people = list(map(int, sys.stdin.readline().rstrip().split()))
x, y, r = map(int, sys.stdin.readline().rstrip().split())
flag = False

for person in people:
    if person == x:
        print(people.index(person)+1)
        flag = True

if not flag:
    print(0)