N, K = map(int, input().split())
coins = []
used_coin = 0

for _ in range(N):
    coins.append(int(input()))

coins.sort()
coins.reverse()

for now_coin in coins:
    if K == 0:
        break
    valid_divide = K//now_coin
    if valid_divide >= 1:
        K -= now_coin * valid_divide
        used_coin += valid_divide

print(used_coin)