import sys

n = int(sys.stdin.readline())

i = 1
j = 0
valid = True

stack = []
wants = []
result = [1]
stackstat = ["+"]

for _ in range(n):
	wants.append(int(sys.stdin.readline().rstrip()))

while j < n:
	if not result:
		result.append(i + 1)
		stackstat.append("+")
		i += 1
		continue

	elif result[-1] == wants[j]:
		result.pop()
		stackstat.append("-")
		j += 1
		continue

	elif i > n:
		valid = False
		break

	result.append(i+1)
	stackstat.append("+")
	i += 1

if valid:
	for k in stackstat:
		print(k)
else:
	print("NO")


'''
	시간복잡도에 대한 생각때문에 많은 생각을 하느라 시간낭비를 한 문제...
	의외로 시간복잡도는 그렇게 큰 문제가 아니였다.
	풀이한 방식이 상당히 무식해서 이번 문제는 고수들이 푼 답을 보며 복습해야 할 듯
'''