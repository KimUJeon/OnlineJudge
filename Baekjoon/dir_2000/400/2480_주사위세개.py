dice = list(map(int, input().split()))
dice.sort()
prize = 0
dice_set = set(dice)

if len(dice_set) == 1:
    prize = 10000 + dice[0]*1000
elif len(dice_set) == 2:
    if dice.count(dice[0]) == 2:
        prize = 1000 + dice[0]*100
    elif dice[0] != dice[1]:
        prize = 1000 + dice[1]*100
else:
    prize = dice[2]*100

print(prize)

