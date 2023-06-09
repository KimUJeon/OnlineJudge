import sys

word = list(sys.stdin.readline().rstrip())
words = []
for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        f = word[:i]
        s = word[i:j]
        t = word[j:]
        f.reverse()
        s.reverse()
        t.reverse()
        words.append("".join(f+s+t))

print(sorted(words)[0])