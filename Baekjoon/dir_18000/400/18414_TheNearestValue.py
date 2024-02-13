import sys

X, L, R = map(int, sys.stdin.readline().rstrip().split())
gap = 1e9
flag = 0

for idx in range(L, R+1):
    X_gap = abs(X-idx)
    if X_gap < gap:
        gap = X_gap
        flag = idx

print(flag)