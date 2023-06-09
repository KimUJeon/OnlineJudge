import sys
import itertools

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0

for i in range(1, N+1):
	combi = itertools.combinations(nums, i)

	for j in combi:
		if S == sum(j):
			count += 1

print(count)

'''
	itertools에서 제공하는 combinations로 조합을 만들어
	해당 조합들을 각각 더해서 원하는 결과인 S와 동일하면 갯수를 늘리는 방식으로 구현
'''