import sys

N, W, H, L = map(int, sys.stdin.readline().rstrip().split())
max_cow = (W//L)*(H//L)

print(min(max_cow, N))