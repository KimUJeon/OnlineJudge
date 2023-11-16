import sys

depth = []
for _ in range(4):
    depth.append(int(sys.stdin.readline().rstrip()))
inc_depth = sorted(depth)
dec_depth = sorted(depth, reverse=True)
set_depth = list(set(depth))

if len(set(depth)) == 1:
    print("Fish At Constant Depth")
elif len(set_depth) != 4:
    print("No Fish")
elif depth == dec_depth:
    print("Fish Diving")
elif depth == inc_depth:
    print("Fish Rising")
else:
    print("No Fish")