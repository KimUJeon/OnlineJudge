name = list(map(str, input().split('-')))
last = ""

for word in name:
    last += word[0]

print(last)