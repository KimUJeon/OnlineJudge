import sys


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


N, K = map(int, sys.stdin.readline().rstrip().split())
print(factorial(N)//(factorial(K) * factorial(N-K)))
