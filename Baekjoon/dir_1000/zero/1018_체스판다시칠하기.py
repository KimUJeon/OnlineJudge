import sys, time

def chess():
    for i in range(N-7):
        for j in range(M-7):
            wh = 0
            bl = 0
            for x in range(i, i+8):
                for y in range(j, j+8):
                    if (x+y) % 2 == 0:
                        if chess_board[x][y] != 'B':
                            bl += 1
                        elif chess_board[x][y] != 'W':
                            wh += 1
                    else:
                        if chess_board[x][y] != 'W':
                            bl += 1
                        elif chess_board[x][y] != 'B':
                            wh += 1
            result.append(bl)
            result.append(wh)
    print(min(result))


N, M = map(int, sys.stdin.readline().rstrip().split())
chess_board = []
result = []
for _ in range(N):
    chess_board.append(sys.stdin.readline().rstrip())
chess()