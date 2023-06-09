import sys

N = int(sys.stdin.readline())

deck = []
for i in range(N):
    oper = sys.stdin.readline().split()
    oper_word = oper[0]

    if oper_word == "push_front":
        deck.insert(0, oper[1])

    elif oper_word == "push_back":
        deck.append(oper[1])

    elif oper_word == "pop_front":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop(0))

    elif oper_word == "pop_back":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop())

    elif oper_word == "size":
        print(len(deck))

    elif oper_word == "empty":
        if len(deck) == 0:
            print(1)
        else:
            print(0)

    elif oper_word == "front":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])

    elif oper_word == "back":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])
