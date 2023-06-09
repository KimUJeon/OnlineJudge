word = input()
moum = ["a", "e", "i", "o", "u"]

result = 0

for check in moum:
    if word.count(check):
        result += word.count(check)

print(result)