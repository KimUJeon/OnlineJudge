import sys

N = int(sys.stdin.readline())
board = []

for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [[0 for _ in range(N)] for _ in range(N)]
ans = False

dir_x = [1, 0]
dir_y = [0, 1]

def bfs(x, y):
    global ans
    que = [[0, 0]]

    while que:
        x, y = que.pop()

        if board[x][y] == -1:
            ans = True
            break

        repeat = board[x][y]

        for i in range(2):
            # 쪨리가 움직일땐 한칸씩 움직이는게 아니라 바로 도착하려는 칸에 도착함
            # 이 부분때문에 어려웠던것 같음
            nx = x + dir_x[i] * repeat
            ny = y + dir_y[i] * repeat

            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                que.append([nx, ny])

bfs(0, 0)
if ans:
    print("HaruHaru")
else:
    print("Hing")