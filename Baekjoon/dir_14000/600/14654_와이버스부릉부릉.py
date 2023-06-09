import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
people = K
for _ in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    people += (A - B)

print("비와이")
