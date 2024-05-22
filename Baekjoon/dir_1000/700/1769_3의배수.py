import sys

X = str(sys.stdin.readline().rstrip())
cnt = 0
convert_X = 0

while True:
    if len(str(X)) >= 2:
        cnt += 1
        for item in str(X):
            convert_X += int(item)
    else:
        convert_X = int(X)

    if len(str(convert_X)) == 1:
        print(cnt)
        if convert_X % 3 == 0:
            print("YES")
            break
        else:
            print("NO")
            break

    X = convert_X
    convert_X = 0
