import sys

while True:
    data = float(sys.stdin.readline().rstrip())
    if data == 0:
        break
    else:
        total = 1 + data + (data*data) + (data*data*data) + (data*data*data*data)
        print("{:.2f}".format(total))