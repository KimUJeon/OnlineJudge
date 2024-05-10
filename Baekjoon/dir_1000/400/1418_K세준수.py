import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

primes = [1] * (N + 1)
for i in range(2, int(N**0.5) + 1):
    if primes[i]:
        for j in range(2 * i, N + 1, i):
            primes[j] = 0

k_nums = [1] * (N + 1)
for i in range(2, N + 1):
    if primes[i] and i > K:
        for j in range(i, N + 1, i):
            k_nums[j] = 0
print(sum(k_nums) - 1)
