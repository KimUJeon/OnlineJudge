money = list(map(int, input().split()))

price = money[0]*money[1]
now_money = money[2]

if price > now_money:
    print(price - now_money)
else:
    print(0)
