import sys

S = str(sys.stdin.readline().rstrip())
group = {"0": 0, "1": 0}

for idx, char in enumerate(S):
    if idx == 0:
        group[char] += 1
    else:
        if char != S[idx - 1]:
            group[char] += 1

print(min(group.values()))
