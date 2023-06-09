import sys

N = int(sys.stdin.readline().rstrip())
asc = list(map(int, sys.stdin.readline().split()))
asc = sorted(set(asc))

for num in asc:
	print(num, end=' ')


'''
	중복값을 제거해주는 set 기능과 출력시 띄어쓰기를 같이 입력해주는 end 기능을
	알고있다면 쉽게 풀 수 있는 문제
'''