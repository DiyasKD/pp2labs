import datetime
a = datetime.datetime.now() - datetime.timedelta(days=1)
b = datetime.datetime.now()
c = datetime.datetime.now() + datetime.timedelta(days=1)
print("Yesterday: " + a.strftime('%d-%m-%Y'))
print("Today: " + b.strftime('%d-%m-%Y'))
print("Tomorrow: " + c.strftime('%d-%m-%Y'))
