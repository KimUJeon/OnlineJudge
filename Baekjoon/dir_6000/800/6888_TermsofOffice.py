import sys, math

X = int(sys.stdin.readline().rstrip())
Y = int(sys.stdin.readline().rstrip())

lcm = math.lcm(4, 2, 3, 5)
count = 0

for year in range(X, Y+1):
    if count == 0 or count == lcm:
        print(f"All positions change in year {year}")
        count = 0
    count += 1