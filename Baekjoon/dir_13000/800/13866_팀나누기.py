import sys

people = list(map(int, sys.stdin.readline().rstrip().split()))
people.sort()

team1 = people[0] + people[3]
team2 = people[1] + people[2]

print(abs(team2 - team1))
