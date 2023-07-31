import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
degree = [a, b, c]

if a+b+c != 180:
    print("Error")
else:
    flag = 0
    for item in degree:
        if degree.count(item) == 2:
            flag = 0
        elif degree.count(item) == 3:
            flag = 1
        else:
            flag = 2

    if flag == 0:
        print("Isosceles")
    elif flag == 1:
        print("Equilateral")
    else:
        print("Scalene")