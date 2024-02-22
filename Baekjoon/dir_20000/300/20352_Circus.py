import sys, math

a = int(sys.stdin.readline().rstrip())
radius = math.sqrt(a / math.pi)

print("{:.9f}".format(radius * 2 * math.pi))
