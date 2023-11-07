import sys

N = int(sys.stdin.readline().rstrip())
row_team = []
for i in range(1, N+1):
    row_team.append(str(i))
    if i % 6 == 0:
        row_team.append("Go!")
if row_team[-1] != "Go!":
    row_team.append("Go!")

print(" ".join(row_team))