import sys

k, w, m = map(int, sys.stdin.readline().rstrip().split())
result = (w-k)
if result % m == 0:
    pass
else:
    result //= m
    result += 1
print(result)