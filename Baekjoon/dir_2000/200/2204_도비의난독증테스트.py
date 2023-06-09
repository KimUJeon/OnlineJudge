import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    words = []
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        words.append(word)
    words.sort(key=str.lower)

    print(words[0])