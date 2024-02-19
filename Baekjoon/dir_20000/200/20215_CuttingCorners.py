import sys, math

a, b = map(int, sys.stdin.readline().rstrip().split())
daegak = math.sqrt(pow(a, 2) + pow(b, 2))
result = (a+b) - daegak

if int(result) == result:
    print(int(result))
else:
    print("{:.9f}".format(result))
