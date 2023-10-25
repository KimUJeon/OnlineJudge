import sys

T = int(sys.stdin.readline().rstrip())
scores = list(map(int, sys.stdin.readline().rstrip().split())) + [0] * (5-T)
hak_bun_1 = 0
hak_bun_2 = 0
hak_bun_3 = 0

result = 0

def re_abs(sub1, sub2):
    return abs(sub1-sub2)

if scores[0] > scores[2]:
    hak_bun_1 = re_abs(scores[0], scores[2]) * 508
elif not scores[0] > scores[2]:
    hak_bun_1 = re_abs(scores[0], scores[2]) * 108

if scores[1] > scores[3]:
    hak_bun_2 = re_abs(scores[1], scores[3]) * 212
elif not scores[1] > scores[3]:
    hak_bun_2 = re_abs(scores[1], scores[3]) * 305

if scores[4] != 0:
    hak_bun_3 = scores[4] * 707

result = (hak_bun_1 + hak_bun_2 + hak_bun_3) * 4763

print(result)