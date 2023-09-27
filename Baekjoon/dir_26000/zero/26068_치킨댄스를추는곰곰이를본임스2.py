import sys

N = int(sys.stdin.readline().rstrip())
gifticons = [""]
count = 0

for _ in range(N):
    gifticons.append(sys.stdin.readline().rstrip())

for i in range(1, N+1):
    gifticon = gifticons[i].split("-")
    if int(gifticon[1]) <= 90:
        count += 1

print(count)