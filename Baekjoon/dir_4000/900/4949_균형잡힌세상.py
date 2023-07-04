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
    if ans:
        print("yes")
    else:
        print("no")