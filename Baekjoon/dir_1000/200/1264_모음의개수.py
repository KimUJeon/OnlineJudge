import sys

target = ["a", "e", "i", "o", "u"]


while True:
    words = sys.stdin.readline().rstrip().lower()
    count = 0
    if words != "#":
        for item in words:
            if item in target:
                count += 1
        print(count)
    else:
        break