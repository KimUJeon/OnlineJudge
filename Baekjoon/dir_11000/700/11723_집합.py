import sys

M = int(sys.stdin.readline().rstrip())
var_all = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
S = set()

for _ in range(M):
    command_line = list(sys.stdin.readline().rstrip().split())
    if command_line[0] == "add":
        S.add(int(command_line[1]))
    elif command_line[0] == "remove":
        try:
            S.remove(int(command_line[1]))
        except KeyError:
            pass
    elif command_line[0] == "check":
        if int(command_line[1]) in S:
            print(1)
        else:
            print(0)
    elif command_line[0] == "toggle":
        if int(command_line[1]) in S:
            try:
                S.remove(int(command_line[1]))
            except KeyError:
                pass
        else:
            S.add(int(command_line[1]))
    elif command_line[0] == "all":
        S.update(var_all)
    elif command_line[0] == "empty":
        S.clear()
