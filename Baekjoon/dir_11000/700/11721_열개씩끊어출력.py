sentence = input()
remain = len(sentence)
i = 1
while True:
    if remain//10 >= 1:
        print(sentence[10*(i-1):10*i])
        remain -= 10
    else:
        print(sentence[10*(i-1):(10*i)+remain])
        break
    i += 1
