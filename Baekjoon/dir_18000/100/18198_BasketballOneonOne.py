import sys

score_list = []
alice, barbara = 0, 0
score_line = str(sys.stdin.readline().rstrip())
for idx in range(0, len(score_line), 2):
    score_list.append(score_line[idx:idx+2])

for score in score_list:
    if score[0] == "A":
        alice += int(score[1])
    else:
        barbara += int(score[1])

if alice > barbara:
    print("A")
else:
    print("B")