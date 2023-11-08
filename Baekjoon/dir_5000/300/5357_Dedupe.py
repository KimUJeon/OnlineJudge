import sys

cycle = int(sys.stdin.readline().rstrip())

for _ in range(cycle):
    alpha = sys.stdin.readline().rstrip()
    result = [alpha[0]]
    for idx in range(len(alpha)-1):
        if alpha[idx] != alpha[idx+1]:
            result.append(alpha[idx+1])

    print("".join(result))