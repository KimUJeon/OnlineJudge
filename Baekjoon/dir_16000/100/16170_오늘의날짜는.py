import datetime

utctime = datetime.datetime.utcnow()
timelist = str(utctime.date())
timelist = timelist.split("-")

for item in timelist:
    print(item)