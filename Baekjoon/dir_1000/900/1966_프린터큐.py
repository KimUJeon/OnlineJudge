import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
	order = 0

	N, M = map(int, sys.stdin.readline().split())
	good = map(int, sys.stdin.readline().split())

	# i 는 중요도 idx는 기존 배열의 순서
	docus = deque((i,idx) for idx, i in enumerate(good))

	while True:
		if docus[0][0] == max(docus, key=lambda x:x[0])[0]:
			order += 1
			if docus[0][1] == M:
				print(order)
				break
			else:
				docus.popleft()
		else:
			docus.append(docus.popleft())

'''
	지문을 이해하는 것이 조금 어려웠다... 가끔 이런 문제는 그림 설명이라도 들어있으면 좋을텐데
	구글링을 통해 블로그에서 개념 확인 한 뒤에 deque와 반복문 사용시 인덱스도 같이 지정해주는 enumerate를
	사용해 문제풀이를 진행 하였다. 문제 이해만 한다면 쉽게 풀 수 있는 문제
'''