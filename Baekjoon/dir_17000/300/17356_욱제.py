import sys

uk, ukje = map(int, sys.stdin.readline().rstrip().split())
M = (ukje-uk)/400

result = 1/(1+10**M)
print(result)