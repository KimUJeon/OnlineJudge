import sys

N = int(sys.stdin.readline())
categories = list(map(str, sys.stdin.readline()))

B = categories.count("B")
S = categories.count("S")
A = categories.count("A")

if B == S == A:
    print("SCU")
else:
    if B == max(B, S, A):
        print("B", end="")
    if S == max(B, S, A):
        print("S", end="")
    if A == max(B, S, A):
        print("A", end="")
