import sys

A, P = map(int, sys.stdin.readline().rstrip().split())
total_A = 7 * A
total_P = 13 * P

if total_A > total_P:
    print("Axel")
elif total_P > total_A:
    print("Petra")
else:
    print("lika")
