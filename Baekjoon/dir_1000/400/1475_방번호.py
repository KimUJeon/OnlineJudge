import sys

plastic = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
}
N = str(sys.stdin.readline().rstrip())

for word in N:
    if word == "6" or word == "9":
        plastic["6"] += 0.5
    else:
        plastic[word] += 1

print(max(plastic.values()).__ceil__())
