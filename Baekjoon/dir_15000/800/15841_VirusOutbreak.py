import sys

# 입력이 최대 490개지만 0에 위치하는 값은 버리는 값이 되기 때문에 이를 반영해 +1을 함
# 인덱스의 처음부터 순서를 맞춰주고 싶다면 0번 인덱스부터 1을 넣어도 무방함
dps = [0] * 491
dps[1] = 1
dps[2] = 1
dps[3] = 2

def dp(hrs):
	for i in range(4, hrs+1):
		dps[i] = dps[i-1] + dps[i-2]

	return dps[hrs]


while True:
	hrs = int(sys.stdin.readline())
	if hrs == -1:
		break

	result = dp(hrs)

	print(f"Hour {hrs}: {result} cow(s) affected")

'''
	<DP 문제>
	결과값에 규칙이 있는 문제로 이번 문제에서는
	감염된 소는 1:1 의 비율로 다른 소를 감염시키지만 감염 증상 발현은 2시간 뒤에 일어난다.
	그래서 1시간째는 1마리(A 감염 +1) 2시간째 1마리(A 감염 + 1, B 감염 + 1) 3시간째 비로소 2마리(B 감염 +1, C 감염 + 2)가 되며
	4시간째는 3마리(C 감염 +2, D 감염 + 3) 식으로 발생하게 된다.
	
	이런 문제는 노트에 직접 그려가며 푸는게 가장 빠르고 정확하게 풀 수 있다
'''