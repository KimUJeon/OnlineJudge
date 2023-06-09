import sys
import math
from itertools import combinations

# 조합에서 나온 모든 최소 공배수를 담기 위한 리스트
ls_num: list = []

nums = list(map(int, sys.stdin.readline().rstrip().split()))
# itertools의 combination 기능을 이용해 조합 리스트 생성
c_nums = combinations(nums, 3)
for num in c_nums:
	ls_num.append(math.lcm(num[0], num[1], num[2]))

print(min(ls_num))

'''
	<브루트포스 알고리즘>
	단순 무식한 계산 방법으로 문제를 풀어야 해서 브루트포스로 분류된듯
'''