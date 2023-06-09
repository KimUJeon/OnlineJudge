import sys

stu_nums = int(sys.stdin.readline())
students = []
chairman = [[0] * stu_nums for i in range(stu_nums)]

for _ in range(stu_nums):
	students.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(5):
	for j in range(stu_nums):
		for k in range(j+1, stu_nums):
			if students[j][i] == students[k][i]:
				chairman[j][k] = 1
				chairman[k][j] = 1

fin_chair = []
for item in chairman:
	fin_chair.append(item.count(1))

# 같은 반 횟수(미중복)을 집계한 리스트는 0번부터 시작하므로 n번 학생에 맞추기 위해 +1 을 해야함
# 추가로 max 함수는 가장 첫 인덱스를 뽑아 주기 때문에 가장 작은 번호만 출력한다에 적절함
print(fin_chair.index(max(fin_chair))+1)

'''
여러모로 사람 골때리게 하는 문제, 같은 반이었던 적이 한번만 집계되어야 한다는 사실을 이해하지 못하면
자꾸 틀릴수 밖에 없는 문제임
'''