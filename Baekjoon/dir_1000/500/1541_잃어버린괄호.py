import sys

n = str(sys.stdin.readline().rstrip())
nums = n.split("-")
num = []

for num_element in nums:
    num_element = map(int, num_element.split("+"))
    result = sum(num_element)
    num.append(result)

answer = num[0]
for idx in range(1, len(num)):
    answer -= num[idx]

print(answer)
