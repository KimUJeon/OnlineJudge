import sys

N, K = map(int, sys.stdin.readline().split())
for _ in range(K):
    S, T, R = map(int, sys.stdin.readline().rstrip().split())
    OTR = S * T
    result = cnt = 0

    while True:
        if N - cnt <= OTR:
            result += ((N - cnt) / S).__ceil__()
            break
        else:
            cnt += OTR
            result += T + R

    print(result)
