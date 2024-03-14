import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
passwords = dict()

for _ in range(N):
    site, password = map(str, sys.stdin.readline().rstrip().split())
    passwords[site] = password

for _ in range(M):
    need_password = sys.stdin.readline().rstrip()
    print(passwords[need_password])
