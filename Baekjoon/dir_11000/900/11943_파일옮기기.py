import sys

fir = list(map(int, sys.stdin.readline().rstrip().split()))
sec = list(map(int, sys.stdin.readline().rstrip().split()))

result1 = fir[0] + sec[1]
result2 = fir[1] + sec[0]

print(min(result1, result2))


