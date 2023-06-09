import sys

M, N = map(int, sys.stdin.readline().rstrip().split())

if M == N:
	print(2*(N-1))
else:
	if M > N:
		print(2 * (N-1) + 1)
	else:
		print(2*(M-1))

# x_start, y_start, x_end, y_end = 0, 0, (N-1), (M-1)
# end = M * N - 2
# count = 0
# x, y, rev = True, False, False
# x_pos, y_pos = 0, 0
#
# while end > 0:
# 	if rev:
# 		if x:
# 			x_pos -= 1
# 			if x_pos == x_start:
# 				count += 1
# 				x_start += 1
# 				x, y = False, True
# 		if y:
# 			if y_pos == y_start:
# 				count += 1
# 				y_end -= 1
# 				x, y = True, False
# 				rev = False
# 			y_pos -= 1
# 		print(x_pos, y_pos, end, "입니다")
# 	else:
# 		if x:
# 			x_pos += 1
# 			if x_pos == x_end:
# 				count += 1
# 				x_end -= 1
# 				x, y = False, True
# 		if y:
# 			if y_pos == y_end:
# 				count += 1
# 				y_start += 1
# 				x, y = True, False
# 				rev = True
# 			y_pos += 1
# 		print(x_pos, y_pos, end, "입니다2")
# 	end -= 1
#
#
# print(count)
#
#

'''
수학으로 접근한다면 정사각형과 열 > 행 인 경우는 2 * (한 변 길이 -1)
행 > 열 인 경우는 2 * (작은 변 길이 - 1) + 1 을 하면 풀이가 가능하다

주석처리된 코드는 구현방식으로 풀이하려고 했으나 난이도 대비 투자 시간이 많은 것 같아 우선 패스
'''