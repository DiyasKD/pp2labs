import datetime
a = datetime.datetime.now()
a = a.replace(microsecond=0)
print(a)
