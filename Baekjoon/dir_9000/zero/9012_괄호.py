import sys

T = int(sys.stdin.readline())

for _ in range(T):
	vpschk = 0
	value = list(map(str, sys.stdin.readline().rstrip()))

	for i in value:
		if i == "(":
			vpschk += 1
		else:
			vpschk -= 1

		if vpschk < 0:
			print("NO")
			break

	if vpschk > 0:
		print("NO")
	elif vpschk == 0:
		print("YES")

'''
	시간제한에 걸릴까봐 걱정했지만 문자열이 최대 50개라서 그런지
	문제 없이 바로 통과할 수 있었다. 문제를 간단하게 생각해 보면
	'(' 는 수십개가 있어도 뒤에 ')' 가 나타난다면 한 쌍이 이루어 지기 때문에
	우선 두고 봐야 하지만 만약 ')' 가 앞에있던 '('를 넘어선다면 그건
	절대로 한쌍이 이루어질 수 없기 때문에 카운트가 음수가 되는 순간 NO로
	판단하면 빠르게 끝낼수 있다.
'''