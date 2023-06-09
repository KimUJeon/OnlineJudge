import sys

N = int(sys.stdin.readline())

def fibo(n):
	result = 1
	i = 0
	a, b = 1, 1
	while i < n:
		a, b = b, a+b
		result = a
		i += 1
	return result

for _ in range(N):
	months = int(sys.stdin.readline())
	print(fibo(months))

'''
	기존 재귀함수 방식의 피보나치 수열은 시간이 오래걸리는것 같아
	앞 뒤 숫자만 기억하면 되도록 하는 while 문을 이용해 풀이함
'''