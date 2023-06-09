import sys

N = int(sys.stdin.readline())
queue = []

for i in range(N):
    queue_order = sys.stdin.readline().split()
    queue_word = queue_order[0]

    if queue_word == "push":
        queue_num = queue_order[1]
        queue.append(queue_num)

    elif queue_word == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif queue_word == "size":
        print(len(queue))

    elif queue_word == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif queue_word == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif queue_word == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

'''
    해당 문제는 10828 스택 과 같이
    기본적인 알고리즘 이해를 돕기위한 문제로 보임
'''
