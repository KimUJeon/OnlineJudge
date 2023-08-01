import sys

month = int(sys.stdin.readline().rstrip())
date = int(sys.stdin.readline().rstrip())
target_m = 2
target_d = 18

if month < target_m:
    print("Before")
elif month > target_m:
    print("After")
else:
    if date == target_d:
        print("Special")
    elif date < target_d:
        print("Before")
    else:
        print("After")