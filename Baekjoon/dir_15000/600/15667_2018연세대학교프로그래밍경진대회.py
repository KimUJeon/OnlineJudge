import sys

N = int(sys.stdin.readline().rstrip())

for fire in range(1, N + 1):
    if 1 + fire + fire**2 == N:
        print(fire)
        break
