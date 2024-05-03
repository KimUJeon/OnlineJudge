import sys

scene = 0
result = []

while True:
    scene += 1
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    names = []
    seize = []

    for idx in range(n):
        names.append(str(sys.stdin.readline().rstrip()))

    for _ in range(2 * n - 1):
        order = list(map(str, sys.stdin.readline().rstrip().split()))
        if order[0] in seize:
            seize.remove(order[0])
        else:
            seize.append(order[0])

    for i in seize:
        result.append([str(scene), names[int(i) - 1]])

for item in result:
    print(" ".join(item))
