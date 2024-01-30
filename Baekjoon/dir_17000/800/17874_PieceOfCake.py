import sys

n, h, v = map(int, sys.stdin.readline().rstrip().split())
hori1 = h
hori2 = n-h
verti1 = v
verti2 = n-v

cake1 = hori1 * verti1 * 4
cake2 = hori1 * verti2 * 4
cake3 = hori2* verti1 * 4
cake4 = hori2 * verti2 * 4

print(max(cake1, cake2, cake3, cake4))