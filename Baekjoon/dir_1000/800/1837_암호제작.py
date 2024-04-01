import sys

flag = True
P, K = map(int, sys.stdin.readline().rstrip().split())
for i in range(2, K):
    if P % i == 0:
        flag = False
        print(f"BAD {i}")
        break

if flag:
    print("GOOD")
