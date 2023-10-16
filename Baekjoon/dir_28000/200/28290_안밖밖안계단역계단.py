import sys

inout = ["fdsajkl;", "jkl;fdsa"]
outin = ["asdf;lkj", ";lkjasdf"]
stairs = ["asdfjkl;"]
rev_stairs = [";lkjfdsa"]

words = sys.stdin.readline().rstrip()

if words in inout:
    print("in-out")
elif words in outin:
    print("out-in")
elif words in stairs:
    print("stairs")
elif words in rev_stairs:
    print("reverse")
else:
    print("molu")