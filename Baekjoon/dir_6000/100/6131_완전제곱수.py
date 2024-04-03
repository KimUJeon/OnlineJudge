import sys

N = int(sys.stdin.readline().rstrip())
count = 0


for B in range(1, N + 1):
    for A in range(B, N + 1):
        if A**2 == (B**2) + N:
            count += 1

print(count)
