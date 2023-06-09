import sys

def backtrack(depth):
    global min_num, number
    if depth == len(X):
        if X == number:
            return
        elif number > X:
            min_num = min(min_num, number)
        return

    for i in range(len(X)):
        if visit[i]:
            continue
        visit[i] = True
        number += X[i]
        backtrack(depth+1)
        visit[i] = False
        number = number[:-1]


X: str = sys.stdin.readline().rstrip()
visit = [False] * len(X)
min_num = "999999"
number = ""
backtrack(0)

if min_num == "999999":
    print(0)
else:
    print(min_num)