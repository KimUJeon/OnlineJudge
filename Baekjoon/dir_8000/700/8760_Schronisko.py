import sys

Z = int(sys.stdin.readline().rstrip())



for _ in range(Z):
    W, K = map(int, sys.stdin.readline().rstrip().split())
    square = W * K
    result = square//2
    print(result)