import sys

picture = []
cat = ""

for _ in range(15):
    pic_line = list(map(str, sys.stdin.readline().rstrip().split()))
    picture.append(pic_line)
    if "w" in pic_line:
        cat = "chunbae"
    elif "b" in pic_line:
        cat = "nabi"
    elif "g" in pic_line:
        cat = "yeongcheol"

print(cat)