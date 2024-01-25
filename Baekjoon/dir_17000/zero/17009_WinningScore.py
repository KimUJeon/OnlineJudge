import sys

apple = []
banana = []

for i in range(3):
    apple.append(int(sys.stdin.readline().rstrip()))
apple_sum = apple[0]*3 + apple[1]*2 + apple[2]*1

for j in range(3):
    banana.append(int(sys.stdin.readline().rstrip()))
banana_sum = banana[0]*3 + banana[1]*2 + banana[2]*1

if apple_sum > banana_sum:
    print("A")
elif apple_sum < banana_sum:
    print("B")
else:
    print("T")