W = []
K = []

for _ in range(20):
    if _ < 10:
        W.append(int(input()))
    else:
        K.append(int(input()))

W.sort()
K.sort()

W_result = W[-1] + W[-2] + W[-3]
K_result = K[-1] + K[-2] + K[-3]

print(W_result, K_result)