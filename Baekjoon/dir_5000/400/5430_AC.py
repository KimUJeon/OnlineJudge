import re
import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
	cnt_rev = 0
	cnt_del = 0
	error_point = False

	orders = deque(sys.stdin.readline().rstrip())
	n = int(sys.stdin.readline())
	f_nums = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

	if n == 0:
		f_nums = []
	for order in orders:
		if order == "R":
			cnt_rev += 1
		else:
			if len(f_nums) < 1:
				print("error")
				error_point = True
				break
			else:
				if cnt_rev % 2 == 0:
					f_nums.popleft()
				else:
					f_nums.pop()

	if cnt_rev % 2 == 0 and error_point is False:
		print("[" + ",".join(f_nums) + "]")
	elif cnt_rev % 2 != 0 and error_point is False:
		f_nums.reverse()
		print("[" + ",".join(f_nums) + "]")

'''
	문제의 개념도 이해했고 문제 풀이 방식도 적절했지만 역시나 시간제한이 문제였다.
	count는 시간복잡도가 N이라 사용하면 안되고 당연히 시간복잡도 문제를 해결하기 위해선
	기본 pop 대신 deque의 기능을 사용해야 한다
'''