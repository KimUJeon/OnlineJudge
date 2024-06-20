import sys

N, M = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())

falls = []
n_idx = 1
result = 0
for _ in range(J):
    falls.append(int(sys.stdin.readline()))

for fall in falls:
    e_idx = n_idx + M - 1
    if n_idx <= fall and fall <= e_idx:
        pass
    elif n_idx >= fall:
        result += abs(fall - n_idx)
        n_idx = fall
    else:
        result += fall - e_idx
        n_idx = fall - (M - 1)

print(result)
