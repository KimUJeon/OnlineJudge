import sys

a = int(sys.stdin.readline().rstrip())
x = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
y = int(sys.stdin.readline().rstrip())
T = int(sys.stdin.readline().rstrip())

opt_one = (T-30)*21 * x if T >= 30 else 0
opt_two = (T-45)*21 * y if T >= 45 else 0

print(opt_one+a, opt_two+b)