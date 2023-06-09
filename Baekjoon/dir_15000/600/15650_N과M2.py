import sys

def backtrack(depth):
    if len(ans) == M:
        print(" ".join(ans))
        return
    for i in range(depth, N):
        if not visited[i]:
            if len(ans) > 0:
                if not int(ans[-1]) < nums[i]:
                    continue
            visited[i] = True
            ans.append(str(nums[i]))
            backtrack(depth+1)
            visited[i] = False
            ans.pop()


N, M = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * N
nums = [i for i in range(1, N+1)]
ans = []

backtrack(0)