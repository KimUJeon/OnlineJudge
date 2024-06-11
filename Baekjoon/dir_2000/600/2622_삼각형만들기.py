import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0

# 짧은, 중간, 긴
for i in range(1, N + 1):
    for j in range(i, N + 1):
        long = N - i - j
        if long >= i + j:
            continue
        else:
            if j > long:
                break
            cnt += 1
print(cnt)
