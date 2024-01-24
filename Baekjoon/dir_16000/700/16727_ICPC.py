import sys

p1, s1 = map(int, sys.stdin.readline().rstrip().split())
s2, p2 = map(int, sys.stdin.readline().rstrip().split())

pers = p1 + p2
esteg = s1 + s2

if pers > esteg:
    print("Persepolis")
elif pers < esteg:
    print("Esteghlal")
else:
    if p1 < s2:
        print("Persepolis")
    elif p1 > s2:
        print("Esteghlal")
    else:
        print("Penalty")