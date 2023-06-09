N = int(input())
prize = []
result = 0

for i in range(N):
    dice = list(map(int, input().split()))
    dice.sort()
    dice_set = set(dice)
    if len(dice_set) == 1:
        result = (10000 + dice[0]*1000)
        prize.append(result)
    elif len(dice_set) == 2:
        if dice.count(dice[0]) == 2:
            result = (1000 + dice[0]*100)
            prize.append(result)
        elif dice[0] != dice[1]:
            result = (1000 + dice[1]*100)
            prize.append(result)
    else:
        result = (dice[2]*100)
        prize.append(result)

prize.sort()
print(prize[-1])
