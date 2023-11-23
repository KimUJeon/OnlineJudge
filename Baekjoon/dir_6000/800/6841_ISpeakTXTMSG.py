import sys

forms = {"CU": "see you", ":-)": "I’m happy", ":-(": "I’m unhappy", ";-)": "wink", ":-P": "stick out my tongue", "(~.~)": "sleepy",
         "TA": "totally awesome", "CCC": "Canadian Computing Competition", "CUZ": "because", "TY": "thank-you", "YW": "you’re welcome",
         "TTYL": "talk to you later"}

while True:
    word = sys.stdin.readline().rstrip()
    if word in forms:
        print(forms[word])
    else:
        print(word)
    if word == "TTYL" or word == "":
        break