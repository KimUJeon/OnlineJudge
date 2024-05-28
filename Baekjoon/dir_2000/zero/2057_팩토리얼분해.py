import sys

N = int(sys.stdin.readline().rstrip())
fact_nums = [1, 1]

for i in range(2, 21):
    fact_nums.append(fact_nums[i - 1] * i)

result = 0


for i in range(20, -1, -1):
    if result + fact_nums[i] < N:
        result += fact_nums[i]
    elif result + fact_nums[i] == N:
        print("YES")
        exit(0)

print("NO")
