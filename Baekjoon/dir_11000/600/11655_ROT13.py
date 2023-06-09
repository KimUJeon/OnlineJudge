sen = input()
result = ""

for i in range(len(sen)):
    num = ord(sen[i])
    if 65 <= num <= 90:
        num += 13
        if num > 90:
            num -= 26
    elif 97 <= num <= 122:
        num += 13
        if num > 122:
            num -= 26
    result += chr(num)

print(result)