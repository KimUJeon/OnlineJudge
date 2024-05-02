import sys

poly = ["AAAA", "BB"]
N = list(map(str, sys.stdin.readline().rstrip().split(".")))
new_result = []

for item in N:
    flag = True
    result = ""
    while True:
        if len(item) >= 4:
            result += poly[0]
            item = item[4:]
        elif len(item) >= 2:
            result += poly[1]
            item = item[2:]
        elif 0 < len(item) < 2:
            flag = False
            break
        else:
            break

    if flag == False:
        new_result.clear()
        new_result.append(str(-1))
        break

    new_result.append(result)

print(".".join(new_result))
