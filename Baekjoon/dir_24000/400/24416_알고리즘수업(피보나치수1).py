import sys

n = int(sys.stdin.readline().rstrip())
# cnt_fib = 0
#
# def fib(n):
#     global cnt_fib
#     if n == 1 or n == 2:
#         cnt_fib += 1
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


def fib(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


def fibos(n):
    return n - 2


print(fib(n), fibos(n))
