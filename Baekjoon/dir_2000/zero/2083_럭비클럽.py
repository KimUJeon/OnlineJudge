import sys

while True:
    member = list(map(str, sys.stdin.readline().rstrip().split()))
    if member[0] == "#":
        exit()
    else:
        if int(member[1]) > 17 or int(member[2]) >= 80:
            print(member[0], "Senior")
        else:
            print(member[0], "Junior")
