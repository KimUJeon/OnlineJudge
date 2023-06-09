import sys

n = int(sys.stdin.readline())
result = ""
five = n//5
one = n%5

for _ in range(five):
    result += "V"
for _ in range(one):
    result += "I"
print(result)