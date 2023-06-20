import sys

def backtrack(depth):
    if len(ans) == M:
        print(" ".join(ans))
        return
    for i in range(depth, N):
        ans.append(str(nums[i]))
        backtrack(i)
        ans.pop()


N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()
ans = []

backtrack(0)