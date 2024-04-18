import sys

K, L = map(int, sys.stdin.readline().rstrip().split())

flag = True
for i in range(2, L):
    if K % i == 0:
        insu = i
        flag = False
        break

if flag:
    print("GOOD")
else:
    print(f"BAD {insu}")
