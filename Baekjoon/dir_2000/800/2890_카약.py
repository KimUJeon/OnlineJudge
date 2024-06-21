import sys

R, C = map(int, sys.stdin.readline().split())
team_gap = []
for _ in range(R):
    team = 0
    gap = 0
    road = sys.stdin.readline().rstrip()
    if road.count(".") != C - 2:
        for word in road:
            if word == ".":
                gap += 1
            elif 49 <= ord(word) and ord(word) <= 57:
                team = int(word)
                gap = 0
            elif word == "F":
                team_gap.append([team, gap, 0])

grade = 1
for i in range(C - 1):
    flag = False
    for team in team_gap:
        if team[1] == i:
            flag = True
            team[2] = grade
    if flag:
        grade += 1

team_gap.sort(key=lambda x: x[0])
for team in team_gap:
    print(team[2])
