import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque(range(1, N+1))
ans = []

while queue:
	for _ in range(K-1):
		queue.append(queue.popleft())
	ans.append(str(queue.popleft()))

print("<" + ", ".join(ans) + ">")

'''
	요세푸스 문제 자체를 이해하는데 조금 어려움이 있었다.
	스택과 큐의 기능을 모두 가진 deque 를 사용하여 문제를 풀이했는데
	상당히 편하긴 하다
	
	이번 기회에 deque의 기능과 스택,큐 에 대해 다시 확인해보는 것이 좋을 듯
'''