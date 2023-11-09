import sys

while True:
    name = sys.stdin.read().rstrip()
    if name == "":
        break
    else:
        for word in name:
            if word == "i":
                print("e", end="")
            elif word == "e":
                print("i", end="")
            elif word == "I":
                print("E", end="")
            elif word == "E":
                print("I", end="")
            else:
                print(word, end="")
        print()