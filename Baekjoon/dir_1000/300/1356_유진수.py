import sys

nums = []
num = list(map(int, sys.stdin.readline().rstrip()))
stop = False

for i in range(len(num)):
	f_num = 1
	b_num = 1
	for j in range(i+1):
		f_num *= num[j]
	for k in range(i+1, len(num)):
		b_num *= num[k]

	if len(num) == 1:
		break

	if f_num == b_num:
		print("YES")
		stop = True
		break

if not stop:
	print("NO")

'''
조합을 사용해 풀어야 해서 생각보다 시간이 걸릴 수 있겠다 생각해 다시 문제를 봤더니
앞에서부터 순서대로 잘라가며 나누는 것이라 별 문제 없이 바로 풀이가 가능했다.
'''