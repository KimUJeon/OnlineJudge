import sys

N = int(sys.stdin.readline())

while True:
	valid = True
	for i in str(N):
		if i != '4' and i != '7':
			valid = False
			N -= 1
	if valid:
		print(N)
		break

'''
생각했던것 보다 정말 단순 무식한 문제였다...
'''