import sys

n = int(sys.stdin.readline().rstrip())
nums = [0] * 301
dp = [0] * 301


for i in range(1, n + 1):
    nums[i] = int(sys.stdin.readline().rstrip())

dp[1] = nums[1]
dp[2] = nums[1] + nums[2]
dp[3] = max(nums[1] + nums[3], nums[2] + nums[3])

for idx in range(4, n + 1):
    dp[idx] = max(dp[idx - 3] + nums[idx - 1] + nums[idx], dp[idx - 2] + nums[idx])

print(dp[n])
