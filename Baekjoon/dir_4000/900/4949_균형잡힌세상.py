import sys
from collections import deque

while True:
    item_stack = deque()
    ans = True
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break

    for item in sentence:
        if item == "(" or item == "[":
            item_stack.append(item)
        elif item == ")":
            if not item_stack or item_stack[-1] == "[":
                ans = False
                break
            else:
                item_stack.pop()
        elif item == "]":
            if not item_stack or item_stack[-1] == "(":
                ans = False
                break
            else:
                item_stack.pop()
    if ans and not item_stack:
        print("yes")
    else:
        print("no")

'''
처음에 26번 라인에 not item_stack을 빼고 제출해서 왜 틀린건지 이해가 되질 않았는데 질문 게시판을 둘러보다가
[. ). 와 같은 반례를 입력하는데 자꾸 yes가 나오길래 고민해보니 스택이 비어있어야 모두 짝이 맞는것으로 간주해야 한다는것을
간과하고 풀이하였다
'''