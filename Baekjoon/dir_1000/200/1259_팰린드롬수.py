import sys

while True:
	word = list(map(str, sys.stdin.readline().rstrip()))
	rv_word = word[::-1]

	if word == ['0']:
		break
	else:
		if word == rv_word:
			print("yes")
		else:
			print("no")

'''
	[::-1] 이 되는걸 보아 reverse 사용해도 무관할 듯 하다
	단순한 리스트 문제
'''