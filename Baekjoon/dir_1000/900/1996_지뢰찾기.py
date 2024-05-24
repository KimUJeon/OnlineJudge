import sys

N = int(sys.stdin.readline().rstrip())
field = []
answer = [[0] * N for _ in range(N)]

for _ in range(N):
    field.append(list(map(str, sys.stdin.readline().rstrip().replace(".", "0"))))

for i in range(N):
    for j in range(N):
        count = 0
        if field[i][j] != "0":
            answer[i][j] = "*"
        else:
            if i - 1 >= 0:
                if field[i - 1][j] != "0":
                    count += int(field[i - 1][j])
                if j - 1 >= 0:
                    if field[i - 1][j - 1] != "0":
                        count += int(field[i - 1][j - 1])
                if j + 1 <= N - 1:
                    if field[i - 1][j + 1] != "0":
                        count += int(field[i - 1][j + 1])

            if i + 1 <= N - 1:
                if field[i + 1][j] != "0":
                    count += int(field[i + 1][j])
                if j - 1 >= 0:
                    if field[i + 1][j - 1] != "0":
                        count += int(field[i + 1][j - 1])
                if j + 1 <= N - 1:
                    if field[i + 1][j + 1] != "0":
                        count += int(field[i + 1][j + 1])

            if j - 1 >= 0:
                if field[i][j - 1] != "0":
                    count += int(field[i][j - 1])

            if j + 1 <= N - 1:
                if field[i][j + 1] != "0":
                    count += int(field[i][j + 1])

            if count >= 10:
                answer[i][j] = "M"
            else:
                answer[i][j] = count


for ans in answer:
    for item in ans:
        print(item, end="")
    print()
