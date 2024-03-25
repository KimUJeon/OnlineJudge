import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for idx in range(3, n + 1):
    dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 10007

print(dp[n])
