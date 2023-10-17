import sys

def_var = 1080

for _ in range(10):
    direct = int(sys.stdin.readline().rstrip())

    if direct == 1:
        def_var += 90
    elif direct == 2:
        def_var += 180
    else:
        def_var -= 90

def_var //= 90
def_var %= 4

if def_var == 0:
    print("N")
elif def_var == 1:
    print("E")
if def_var == 2:
    print("S")
if def_var == 3:
    print("W")