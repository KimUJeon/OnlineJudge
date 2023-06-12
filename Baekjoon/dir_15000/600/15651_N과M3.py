import sys

def backtrack(depth):
    if len(ans) == M:
        print(" ".join(ans))
        return
    for i in range(depth, N):
        ans.append(str(nums[i]))
        backtrack(depth)
        ans.pop()


N, M = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * N
nums = [i for i in range(1, N+1)]
ans = []

backtrack(0)