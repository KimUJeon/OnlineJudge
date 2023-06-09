import sys

yd = list(map(str, sys.stdin.readline().rstrip()))
team_num = int(sys.stdin.readline())
team = sorted([sys.stdin.readline() for i in range(team_num)])

high_p, idx = 0, 0

for i in range(team_num):
	L = yd.count('L') + team[i].count('L')
	O = yd.count('O') + team[i].count('O')
	V = yd.count('V') + team[i].count('V')
	E = yd.count('E') + team[i].count('E')

	p = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
	if p > high_p:
		high_p = p
		idx = i

print(team[idx])

'''
	문제가 조금 난해했지만 문제만 설명해주는 블로그를 보며 이해할 수 있었다.
	항상 L O V E, 각 문자가 포함되는지를 확인하고 곱 연산으로 인해 결과값이 0 이 된다면
	사전 순으로 가장 앞서는 팀 이름이 우승확률이 높은것으로 친다고 했으므로
	팀 이름을 입력할 때 부터 sorted를 사용해 정렬을 하였다. 그래야 모두가 0일때
	가장 첫 인덱스에 있는 팀 이름이 우승팀일테니까  
'''