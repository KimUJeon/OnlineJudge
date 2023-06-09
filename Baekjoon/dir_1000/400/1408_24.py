h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

time_gap = h2*3600+m2*60+s2 - (h1*3600+m1*60+s1)
if time_gap < 0:
    time_gap += 60*60*24
h = time_gap//3600
m = (time_gap%3600)//60
s = time_gap%60
print("%02d:%02d:%02d" % (h,m,s))