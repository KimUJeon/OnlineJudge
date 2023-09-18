import sys

N = int(sys.stdin.readline().rstrip())
A, B = map(int, sys.stdin.readline().rstrip().split())

print(min(N, (A//2+B//1)))