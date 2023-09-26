import sys

N = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

discounts = [P-500, int(P*0.9), P-2000, int(P*0.75)]

if N//5 == 1:
    res = discounts[0]
elif N//5 == 2:
    res = min(discounts[0], discounts[1])
elif N//5 == 3:
    res = min(discounts[0], discounts[1], discounts[2])
elif N//5 >= 4:
    res = min(discounts[0], discounts[1], discounts[2], discounts[3])
else:
    res = P

if res <= 0:
    print(0)
else:
    print(res)