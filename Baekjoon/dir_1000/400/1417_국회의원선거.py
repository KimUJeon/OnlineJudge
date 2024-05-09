import sys

N = int(sys.stdin.readline().rstrip())
votes = []

for _ in range(N):
    votes.append(int(sys.stdin.readline().rstrip()))

dasom = votes[0]
votes.pop(0)
votes.sort(reverse=True)
cnt = 0

if len(votes) == 0:
    print(0)
    exit()

while True:
    if votes[0] >= dasom:
        cnt += 1
        votes[0] -= 1
        dasom += 1
    else:
        print(cnt)
        break
    votes.sort(reverse=True)
