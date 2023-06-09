import sys

name = sys.stdin.readline().rstrip()

for i in range(3):
    outstr = ""
    for j in range(3):
        if i == 1 and j == 1:
            outstr += ":{0}:".format(name)
        else:
            outstr += ":fan:"
    print(outstr)