import sys

w, h = map(int, sys.stdin.readline().split())
w_slice = [h]
h_slice = [w]
T = int(sys.stdin.readline())

for _ in range(T):
    type, slice = map(int, sys.stdin.readline().split())
    if type == 0:
        w_slice.append(slice)
    else:
        h_slice.append(slice)

w_slice.sort()
h_slice.sort()

w_sc = []
h_sc = []
w = h = 0
for w_idx in w_slice:
    w_sc.append(w_idx - w)
    w = w_idx
for h_idx in h_slice:
    h_sc.append(h_idx - h)
    h = h_idx

print(max(w_sc) * max(h_sc))
