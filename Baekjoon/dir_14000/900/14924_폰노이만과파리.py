import sys

S, T, D = map(int, sys.stdin.readline().rstrip().split())

hr = D/(S*2)
print(int(hr*T))