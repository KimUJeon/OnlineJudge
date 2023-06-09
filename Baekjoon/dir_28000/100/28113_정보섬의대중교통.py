import sys

N,A,B = map(int, sys.stdin.readline().rstrip().split())

if A < N:
    print("Bus")
elif A > N or A == N:
    if A == B:
        print("Anything")
    elif A > B:
        print("Subway")
    elif A < B:
        print("Bus")
elif A == N:
    if A == B:
        print("Anything")
    elif A > B:
        print("Subway")
    elif A < B:
        print("Bus")