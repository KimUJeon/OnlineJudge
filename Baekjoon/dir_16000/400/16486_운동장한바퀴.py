import sys
from math import pi

d1 = int(sys.stdin.readline())
d2 = int(sys.stdin.readline())

result = (d1*2)+((d2*2)*pi)
print(f"{result:.8}")