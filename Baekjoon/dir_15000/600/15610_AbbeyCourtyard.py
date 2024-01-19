import sys, math

a = int(sys.stdin.readline().rstrip())
one_line = math.sqrt(a)

print("{:.8f}".format(one_line*4))