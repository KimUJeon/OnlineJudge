import sys

weight = float(sys.stdin.readline().rstrip())
height = float(sys.stdin.readline().rstrip())

BMI = weight/(height*height)

if BMI > 25:
    print("Overweight")
elif BMI > 18.5 and BMI <= 25:
    print("Normal weight")
else:
    print("Underweight")