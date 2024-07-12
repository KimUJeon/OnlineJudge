import sys

words = sys.stdin.readline().rstrip()
result = [".", ".", "#", ".", "."]

for n, i in enumerate(words, 1):
    kind = "#"
    if n % 3 == 0:
        kind = "*"
        result[2] = result[2][:-1] + kind

    result[0] += f".{kind}.."
    result[1] += f"{kind}.{kind}."
    result[2] += f".{i}.{kind}"
    result[3] += f"{kind}.{kind}."
    result[4] += f".{kind}.."

for row in result:
    print(row)
