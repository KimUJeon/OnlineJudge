import sys

result = 0
papers = [[0] * 101 for _ in range(101)]
for _ in range(4):
    s_x, s_y, e_x, e_y = map(int, sys.stdin.readline().split())
    for i in range(s_x + 1, e_x + 1):
        for j in range(s_y + 1, e_y + 1):
            papers[i][j] = 1

for paper in papers:
    result += sum(paper)
print(result)
