import sys

limit = int(sys.stdin.readline().rstrip())
cur_speed = int(sys.stdin.readline().rstrip())
gap = cur_speed - limit

if gap >= 31:
    print("You are speeding and your fine is $500.")
elif gap >= 21:
    print("You are speeding and your fine is $270.")
elif gap >= 1:
    print("You are speeding and your fine is $100.")
else:
    print("Congratulations, you are within the speed limit!")