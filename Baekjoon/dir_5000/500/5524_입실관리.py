import sys

N = int(sys.stdin.readline().rstrip())
rooms = []
for _ in range(N):
    rooms.append(sys.stdin.readline().rstrip().lower())

for item in rooms:
    print(item)