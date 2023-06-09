T = int(input())

for i in range(T):
    error, sentence = input().split()
    error = int(error)

    print(sentence[:error-1] + sentence[error:])