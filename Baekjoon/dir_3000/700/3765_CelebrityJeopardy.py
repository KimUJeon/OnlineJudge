import sys

while True:
    input_data = sys.stdin.read().rstrip()
    if input_data == "":
        break
    else:
        print(input_data)