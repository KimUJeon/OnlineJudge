import sys

def backtrack(depth):
    if len(ans) == N:
        print(" ".join(ans))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            ans.append(str(nums[i]))
            backtrack(depth+1)
            visited[i] = False
            ans.pop()


N = int(sys.stdin.readline())
visited = [False] * N
nums = [i for i in range(1, N+1)]
ans = []

backtrack(0)