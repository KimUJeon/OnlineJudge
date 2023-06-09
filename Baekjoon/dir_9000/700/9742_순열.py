import sys

def backtrack(depth):
    global ans, real_ans, count
    if len(ans) == width:
        if count == int(idx):
            real_ans = "".join(ans)
            count += 1
            return real_ans
        else:
            count += 1
        return

    for i in range(width):
        if not visit[i]:
            visit[i] = True
            ans.append(word[i])
            backtrack(depth+1)
            visit[i] = False
            ans.pop()

    return real_ans


for line in sys.stdin:
    # word, idx = sys.stdin.readline().rstrip().split()
    word, idx = map(str, line.split())
    width = len(word)
    visit = [False] * width
    count = 1
    ans = []
    real_ans = ""

    if real_ans == "":
        real_ans = "No permutation"

    print("{0} {1} = {2}".format(word, idx, backtrack(0)))


'''
이번 문제는 EOF도 판별해야 하는 문제로 파이참에서는 Ctrl + D 를 통해 EOF가 된다
이전에 풀어봤던 문제들을 보면서 하니 어느정도 이해가 되는데 아예 안보고 풀려면 조금 시간이 걸릴 듯
'''