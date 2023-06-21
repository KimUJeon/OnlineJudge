import sys

def backtrack(depth):
    global count
    if len(ans) == N:
        ans_group.append(sum(ans))
        return

    for i in range(depth, 4):
        ans.append(nums[i])
        backtrack(i)
        ans.pop()

N = int(sys.stdin.readline())
nums = [1, 5, 10, 50]
ans = []
ans_group = []
backtrack(0)

print(len(set(ans_group)))