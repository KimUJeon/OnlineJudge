import sys

tot_result = 0
while True:
    bet = int(sys.stdin.readline())
    if bet == -1:
        break
    tot_result += bet

print(tot_result)