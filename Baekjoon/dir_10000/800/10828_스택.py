import sys

N = int(sys.stdin.readline())

stack = []
for i in range(N):
    oper = sys.stdin.readline().split()
    oper_word = oper[0]

    if oper_word == "push":
        oper_num = oper[1]
        stack.append(oper_num)

    elif oper_word == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif oper_word == "size":
        print(len(stack))

    elif oper_word == "empty":
        if len(stack) != 0:
            print(0)
        else:
            print(1)

    elif oper_word == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

'''
    스택에 대한 기본적인 개념을 이해할 수 있는 문제로 시간제한이 0.5초 라는 것을
    보고 상당히 어려울 것으로 생각을 했으나 기본적인 기능들로도 충분히 문제 풀이가
    가능하다. 대부분의 알고리즘 문제에서 시간제한이 있기 때문에 해당 문제 또한
    input 대신 sys.stdin.readline 을 사용하였다.
'''