import sys

K = int(sys.stdin.readline())
list_str = []
answer =""
password = list(sys.stdin.readline().rstrip())
len_password = len(password)

for i in range(int(len_password/K)):
	if i%2:
		rev_password = password[(i * K):(i * K) + K:]
		list_str.append(rev_password[::-1])
	else:
		list_str.append(password[(i * K):(i * K) + K])

for j in range(K):
	for i in range(len(list_str)):
		answer += list_str[i][j]

print(answer)

