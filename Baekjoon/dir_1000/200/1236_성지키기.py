import sys

N, M = map(int, sys.stdin.readline().split())
castle = []
r_cnt, c_cnt = 0, 0

for _ in range(N):
	castle.append(sys.stdin.readline().rstrip())

for i in range(N):
	if 'X' not in castle[i]:
		r_cnt += 1

for j in range(M):
	if 'X' not in [castle[i][j] for i in range(N)]:
		c_cnt += 1

print(max(r_cnt, c_cnt))

'''
	경비원이 위치한 십자 모양으로는 경비원이 더 필요없기 때문에 행렬 카운트 변수를 만들어
	비어있는 부분만 카운트 하도록 한 뒤 가장 많은 지역을 커버할 수 있는 위치가 max 로 알 수 있기 때문에
	위와같이 풀이함
'''