import sys

pre_x = 0
x = str(sys.stdin.readline().rstrip())

while True:
    if len(x) >= 1:
        pre_x = int(x)
        x = str(int(x[0]) * len(x))

        if pre_x == int(x):
            print("FA")
            break