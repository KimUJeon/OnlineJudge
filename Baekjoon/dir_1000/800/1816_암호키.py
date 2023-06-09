import sys, time, math

def sosu(n):
	lst = [0, 0] + [1] * (n-1)
	for i in range(2, n+1):
		if lst[i]:
			for j in range(2*i, n+1, i):
				lst[j] = 0
	return lst

primes = sosu(1000000)

N = int(sys.stdin.readline())

for _ in range(N):
	S = int(sys.stdin.readline())
	valid = True
	for i in range(2, min(1000001, int(math.sqrt(S)+1))):
		if primes[i] and not S % i:
			valid = False
			break
	if valid:
		print("YES")
	else:
		print("NO")
		
'''
생각했던 것 보단 난이도가 조금 있던 문제로 느껴졌다
항상 시간이 문제... 에라토스테네스의 체 를 활용하는 것도 오랜만이라 기억이 안나 참고해서 풀이함
'''