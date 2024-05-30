import sys

N = int(sys.stdin.readline().rstrip())
cards = [i for i in range(1, N + 1)]
result = []

for i in range(N):
    result.append(cards.pop(0))
    if i != N - 1:
        cards.insert(len(cards), cards[0])
        cards.remove(cards[0])

for card in result:
    print(card, end=" ")
