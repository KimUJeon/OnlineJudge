read = int(input())
total = 0

for i in range(9):
    price = int(input())
    total += price

noread = read - total
print(noread)