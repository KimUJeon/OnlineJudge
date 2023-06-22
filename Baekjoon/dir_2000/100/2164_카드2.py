import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
cards = deque([i for i in range(1, N+1)])

while True:
    if len(cards) != 1:
        cards.popleft()
        cards.rotate(-1)
    else:
        print(cards[0])
        break