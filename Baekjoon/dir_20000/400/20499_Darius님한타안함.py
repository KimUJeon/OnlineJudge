import sys

K, D, A = map(int, sys.stdin.readline().rstrip().split("/"))
if D == 0 or K+A<D:
    print("hasu")
else:
    print("gosu")