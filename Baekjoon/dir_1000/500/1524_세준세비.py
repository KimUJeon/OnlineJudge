import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
	input() # 줄바꿈 부분 이부분 때문에 자꾸 런타임 에러 발생...
	N, M = sys.stdin.readline().split()
	n_soldier = deque(sorted(list(map(int, sys.stdin.readline().rstrip().split()))))
	m_soldier = deque(sorted(list(map(int, sys.stdin.readline().rstrip().split()))))

	while n_soldier and m_soldier:
		if n_soldier[0] >= m_soldier[0]:
			m_soldier.popleft()
		else:
			n_soldier.popleft()

	if n_soldier:
		print("S")
	elif m_soldier:
		print("B")
	else:
		print("C")

'''
문제는 금방 풀었지만 각 테스트 케이스는 줄 바꿈으로 구분되어 있다를 확인하지 못해 4번이나 ValueError 뽑아냈다...
항상 예제 입력과 조건을 확인하는 습관을 들이자
'''