import sys

while True:
    weight = float(sys.stdin.readline().rstrip())
    if weight < 0:
        break
    moon_weight = weight * 0.167
    print("Objects weighing {:.2f} on Earth will weigh {:.2f} on the moon.".format(weight, moon_weight))