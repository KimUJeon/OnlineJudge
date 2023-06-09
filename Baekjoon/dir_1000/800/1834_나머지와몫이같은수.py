import sys

ans = 0
N = int(sys.stdin.readline())
for i in range(1, N):
	ans += N * i + i # 몫과 나머지가 같은 수는 N에 몫을 곱하고 나머지를 더한 수
print(ans)