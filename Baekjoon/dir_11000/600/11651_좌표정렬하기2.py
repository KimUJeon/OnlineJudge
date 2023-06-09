import sys

N = int(sys.stdin.readline())
num_list = []

for _ in range(N):
	[x, y] = map(int, sys.stdin.readline().split())
	num_list.append([x, y])

num_list.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
	print(num_list[i][0], num_list[i][1])

'''
	11650과 유사한 문제로 sort로 lambda 기능 활용을 잘 하면
	쉽게 풀 수 있는 문제다. 이번 기회에 람다 사용 방법에 대해
	학습하는게 좋을 것 같다.
'''