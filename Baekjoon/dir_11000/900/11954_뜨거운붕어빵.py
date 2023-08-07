import sys

N, M = sys.stdin.readline().rstrip().split()
bbang = []

for _ in range(int(N)):
    bbang.append(str(sys.stdin.readline().rstrip()))

for i in range(int(N)):
    print(bbang[i][::-1])