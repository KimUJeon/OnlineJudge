import sys

while True:
    words = sys.stdin.readline().rstrip()

    if words == "":
        break
    else:
        print(words)
