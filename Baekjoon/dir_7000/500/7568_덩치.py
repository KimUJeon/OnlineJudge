import sys

N = int(sys.stdin.readline().rstrip())
member = []
ranking = []

for _ in range(N):
    member.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    count = 0
    for j in range(N):
        if member[i][0] < member[j][0] and member[i][1] < member[j][1]:
            count += 1
    ranking.append(str(count+1))

print(" ".join(ranking))