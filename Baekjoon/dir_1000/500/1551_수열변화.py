import sys
from collections import deque


N, K = map(int, sys.stdin.readline().rstrip().split())
A = deque(map(str, sys.stdin.readline().rstrip().split(",")))

for _ in range(K):
	for i in range(len(A)-1):
		A[i] = str(int(A[i+1]) - int(A[i]))
	A.pop()

print(",".join(A))

'''
일반적인 list 기능을 사용해도 문제 없을듯
'''