import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []
n = int(sys.stdin.readline())

for _ in range(n):
	command = list(sys.stdin.readline().split())
	if command[0] == 'L':
		if st1:
			st2.append(st1.pop())
	elif command[0] == 'D':
		if st2:
			st1.append(st2.pop())
	elif command[0] == 'B':
		if st1:
			st1.pop()
	else:
		st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))

'''
	상단의 코드는 풀다 도저히 어떻게 시간을 줄일 수 있는지 생각이 나지 않아 여러 블로그들을 참고하였다.
	백준은 본인이 직접 푸는것 이 원칙이란 것을 잘 알고 있지만 오랜 시간 잡고 있기만 하고
	넘긴다면 얻는건 없기에 필자가 풀이했던 것과 비교하여 업로드 하게 되었다.
	
	스택을 두가지를 만들어 st1은 오리지널 st2는 지나간 커서 역할을 하는 리스트로
	최종적으로 들어왔던 순서의 반대로 오리지널 리스트인 st1에 돌려주어야 하기 때문에
	st1에 reversed를 extend 해 준 것이다.
'''



#
# strs = list(sys.stdin.readline().rstrip())
# M = int(sys.stdin.readline())
# for b in range(len(strs)+1):
# 	strs.insert(b * 2, "")
# cursor = int(len(strs)-1)
#
# for i in range(M):
# 	orders = sys.stdin.readline().split()
# 	if orders[0] == "L":
# 		if cursor:
# 			cursor -= 2
# 		else:
# 			pass
# 	elif orders[0] == "D":
# 		if cursor == len(strs)-1:
# 			pass
# 		else:
# 			cursor += 2
# 	elif orders[0] == "B":
# 		if cursor == 0:
# 			pass
# 		else:
# 			del strs[cursor-1]
# 			del strs[cursor-1]
# 			cursor -= 2
# 	elif orders[0] == "P":
# 			strs.insert(cursor, "")
# 			strs.insert(cursor+1, orders[1])
# 			cursor += 2
#
# print("".join(strs))
#
