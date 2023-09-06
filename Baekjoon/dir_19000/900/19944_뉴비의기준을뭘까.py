import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

if M <= 2:
    print("NEWBIE!")
elif 2 < M <= N:
    print("OLDBIE!")
else:
    print("TLE!")