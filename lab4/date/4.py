import datetime
s1 = str(input())
date2 = datetime.datetime.strptime(s1, '%d-%m-%Y').date()
s2 = str(input())
date1 = datetime.datetime.strptime(s2, '%d-%m-%Y').date()
diff = date2 - date1
print("Difference in seconds: ", diff.total_seconds())
