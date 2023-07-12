import sys

T = int(sys.stdin.readline())

dir_x = [-1, 1, 0, 0]
dir_y = [0, 0, -1, 1]

def bfs(x, y):
    que = [(x, y)]
    bae_stat[x][y] = False

    while que:
        x, y = que.pop()

        for i in range(4):
            new_x = x + dir_x[i]
            new_y = y + dir_y[i]

            if new_x < 0 or new_x >= row or new_y < 0 or new_y >= col:
                continue

            if bae_stat[new_x][new_y] == 1:
                que.append((new_x, new_y))
                bae_stat[new_x][new_y] = False


for _ in range(T):
    count = 0
    row, col, baechu = map(int, sys.stdin.readline().rstrip().split())
    bae_stat = [[False for i in range(col)] for j in range(row)]

    for _ in range(baechu):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        bae_stat[x][y] = True

    for i in range(row):
        for j in range(col):
            if bae_stat[i][j]:
                bfs(i, j)
                count += 1

    print(count)