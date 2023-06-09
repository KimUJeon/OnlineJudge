n: int = int(input())


def factorial(n: int):
	if n > 1:
		return n * factorial(n - 1)
	else:
		return 1


facto = str(factorial(n))[::-1]
count = 0

for i in facto:
	if i == '0':
		count += 1
	else:
		print(count)
		break

'''
<최적화 풀이>
N = int(input())
print(N//5 + N//25 + N//125)

5, 25, 125가 각각 5의 배수라는 점을 이용한 풀이 방식으로 최적화된 풀이같음

출처: https://hwiyong.tistory.com/360
'''
