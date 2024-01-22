import sys

first = int(sys.stdin.readline().rstrip())
second = int(sys.stdin.readline().rstrip())
third = int(sys.stdin.readline().rstrip())
fourth = int(sys.stdin.readline().rstrip())

if first >= 8 and fourth >= 8 and second == third:
    print("ignore")
else:
    print("answer")