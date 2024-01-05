import sys

miles = float(sys.stdin.readline().rstrip()) * 1609.344
result = miles/3.785411784
result /= 1000
result = 100/result


print(format(result, ".6f"))
