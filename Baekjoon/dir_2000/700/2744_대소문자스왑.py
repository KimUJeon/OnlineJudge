words = input()
new_words = ""

for word in words:
    if word.isupper():
        new_words += word.lower()
    else:
        new_words += word.upper()


print(new_words)