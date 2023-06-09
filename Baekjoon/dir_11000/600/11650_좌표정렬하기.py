import sys

N = int(sys.stdin.readline())
num_list = []

for _ in range(N):
	[x, y] = map(int, sys.stdin.readline().split())
	num_list.append([x, y])

num_list.sort()

for i in range(N):
	print("%s %s" %(num_list[i][0], num_list[i][1]))

'''
	단순한 정렬 문제로 sort 기능의 개념과 활용법에 대해 알려주는 문제같다.
	실수로 두번이나 틀렸습니다 가 출력되었는데 아무래도 7번 라인을 바로 리스트에
	append 했던것이 readline().split()을 하며 \n 값도 리스트에 들어간게 문제가 되지 않았을까 싶다.
	
	꼭 변수명으로 입력받을 갯수 지정해서 넣자
'''