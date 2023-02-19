import datetime
a = datetime.datetime.now() - datetime.timedelta(days=5)
b = print(a.strftime('%d-%m-%Y'))
