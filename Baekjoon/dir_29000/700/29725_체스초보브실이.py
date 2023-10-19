import sys

black_chess = {'k':0, 'p':1, 'n':3, 'b':3, 'r':5, 'q':9}
white_chess = {'K':0, 'P':1, 'N':3, 'B':3, 'R':5, 'Q':9}

w_score = 0
b_score = 0

for i in range(8):
    line = sys.stdin.readline().rstrip()
    for soldier in line:
        if soldier in white_chess:
            w_score += white_chess[soldier]
        elif soldier in black_chess:
            b_score += black_chess[soldier]

print(w_score-b_score)