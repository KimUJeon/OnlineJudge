import sys

lines = []
while True:
    line = sys.stdin.readline().rstrip()
    if line == "":
        break
    else:
        lines.append(line)

print(len(lines))