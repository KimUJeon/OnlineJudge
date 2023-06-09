X, Y = map(str, input().split())

X = int(X[::-1])
Y = int(Y[::-1])

result = str(X + Y)

result = int(result[::-1])

print(result)