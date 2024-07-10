import sys

word = sys.stdin.readline().rstrip()
sep = []

for i in range(len(word) - 2):
    for j in range(i + 1, len(word) - 1):
        for k in range(j + 1, len(word)):
            group = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            sep.append(group)

# 파이썬의 min은 문자열을 가장 빠른순으로 골라주는 기능이 있어 사용함
print(min(sep))
