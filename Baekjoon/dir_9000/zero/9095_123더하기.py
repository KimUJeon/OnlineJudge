import sys

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
	dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(sys.stdin.readline())
for _ in range(T):
	n = int(sys.stdin.readline())
	print(dp[n])

'''
	규칙성을 찾아 DP 방식으로 풀이하는 문제
	1~4 까지 직접 개수를 세며 규칙성을 찾아보면
	f(n) = f(n-1) + f(n-2) + f(n-3) 이라는 규칙이 나온다
'''