import sys

X, K = map(int, sys.stdin.readline().split())
l_socks = [0 for _ in range(K)]
r_socks = [0 for _ in range(K)]

socks = list(map(int, sys.stdin.readline().split()))

# 색상별로 모으기
for i in range(X):
    l_socks[socks[i] - 1] += 1
for i in range(X, X * 2):
    r_socks[socks[i] - 1] += 1

result = 0
# 색상별로 모은 양말의 갯수를 서로 다른 양말과 곱하기
for i in range(K):
    left = l_socks[i]

    for j in range(K):
        if i == j:
            continue
        result += r_socks[j] * left

print(result)
