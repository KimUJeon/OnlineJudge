import sys

num = sys.stdin.readline().rstrip()
if num[1] == "0":
    num1 = num[:2]
    num2 = num[2:]

else:
    num1 = num[0]
    num2 = num[1:]

print(int(num1)+int(num2))