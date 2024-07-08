import sys

last = 0
group = []
for _ in range(3):
    group.append(sys.stdin.readline().rstrip())

for i in range(3):
    try:
        item = int(group[i])
        last = item + 3 - i
        break
    except:
        pass

if last % 3 == 0 and last % 5 == 0:
    print("FizzBuzz")
elif last % 3 == 0 and last % 5 != 0:
    print("Fizz")
elif last % 3 != 0 and last % 5 == 0:
    print("Buzz")
else:
    print(last)
