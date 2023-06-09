import sys

def backtrack(idx):
    global count
    if len(ans) == k:
        save_ans.add("".join(ans))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            ans.append(card[i])
            backtrack(idx+1)
            visited[i] = False
            ans.pop()

    return save_ans


n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
card = []
visited = [False] * n
for _ in range(n):
    card.append(str(sys.stdin.readline().rstrip()))
ans = []
save_ans = set()
count = 0

print(len(backtrack(0)))
