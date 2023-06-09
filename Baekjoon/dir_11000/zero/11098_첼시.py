n = int(input())

result = []

for i in range(n):
    p = int(input())
    player_dic = {}
    for j in range(p):
        price, player = input().split()
        player_dic[player] = int(price)
    max_key = max(player_dic, key=player_dic.get)
    print(max_key)
