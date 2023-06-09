import sys

while True:
	parallelogram = list(map(float, sys.stdin.readline().rstrip().split()))

	if parallelogram:
		# 쉽게 계산하기 위해 2번째 3번째에 위치하는 좌표값이 일치하는지 확인해야 함
		cord1 = [parallelogram[0], parallelogram[1]]
		cord2 = [parallelogram[2], parallelogram[3]]
		cord3 = [parallelogram[4], parallelogram[5]]
		cord4 = [parallelogram[6], parallelogram[7]]

		while True:
			if cord2 == cord3:
				break
			# 2번과 3번좌표가 동일하지 않은 경우 1번과 2번의 자리를 바꿈
			cord1, cord2 = cord2, cord1
			if cord2 == cord3:
				break
			cord3, cord4 = cord4, cord3

		# 이제 좌표 순서는 맞춰졌으니 x좌표와 y좌표의 차이를 이용해 구하면 된다
		x_gapcord = cord2[0] - cord1[0]
		y_gapcord = cord2[1] - cord1[1]

		x_cord = cord4[0] - x_gapcord
		y_cord = cord4[1] - y_gapcord

		print("{0:.3f} {1:.3f}".format(x_cord, y_cord))
	else:
		break

'''
조금은 생각해봐야 하는 문제이자 평행사변형의 특징을 생각해내면 쉽게 접근 가능한 문제라고 생각함
마주보고 있는 변과 평행하고 길이가 같기 때문에 x와 y를 각각 구해주면 되는데 입력값에서 각 좌표들이
몇번째 순서인지는 제시하지 않았기 때문에 1,2,3,4 번째 순서를 맞춘뒤에 풀이해야 올바른 값이 나온다
'''