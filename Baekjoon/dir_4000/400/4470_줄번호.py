import sys

N = int(sys.stdin.readline().rstrip())
sentence = []

for _ in range(N):
    sentence.append(sys.stdin.readline().rstrip())

for i in range(N):
    print(f"{i+1}. {sentence[i]}")