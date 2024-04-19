import sys

while True:
    B, N = map(int, sys.stdin.readline().rstrip().split())
    if B == N == 0:
        break
    if N == 1:
        print(B)
        continue
    ans = [-1, 1e9]
    for i in range(1, B + 1):
        result = abs(B - i**N)
        if ans[1] > result:
            ans = [i, result]
    print(ans[0])
