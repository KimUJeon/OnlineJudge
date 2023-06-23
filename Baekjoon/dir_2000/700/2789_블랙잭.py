import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
cards.sort()
max_value = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_data = cards[i] + cards[j] + cards[k]
            if sum_data <= M and max_value <= sum_data:
                max_value = sum_data

print(max_value)