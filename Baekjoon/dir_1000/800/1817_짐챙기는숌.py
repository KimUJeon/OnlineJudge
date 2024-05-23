import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
weight = 0

if N != 0:
    books = list(map(int, sys.stdin.readline().rstrip().split()))

    for book in books:
        weight += book
        if weight > M:
            cnt += 1
            weight = book
        elif weight == M:
            cnt += 1
            weight = 0

    if weight != 0:
        cnt += 1

print(cnt)
