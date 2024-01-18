import sys

N, A, B, C, D = map(int, sys.stdin.readline().rstrip().split())
result1 = N//A
result2 = N//C

if N%A != 0:
    result1 += 1
if N%C != 0:
    result2 += 1

print(min(result1*B, result2*D))