import sys

N = int(sys.stdin.readline().rstrip())
money_box = {136: 1000, 142: 5000, 148: 10000, 154: 50000}
tot_money = 0

for _ in range(N):
    width, height = map(int, sys.stdin.readline().rstrip().split())
    tot_money += money_box[width]

print(tot_money)