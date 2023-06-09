word = input()
word_len = len(word)
avg = int(word_len/2)
count = 0

for i in range(avg):
    if word[i] == word[-i-1]:
        count += 1
    else:
        count = 0
        break


if word_len <= 1:
    print(1)
elif count == 0:
    print(0)
else:
    print(1)
