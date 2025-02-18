import datetime
x = datetime.datetime.now()
new_data = x - datetime.timedelta(5)
print(new_data)


#2
import datetime
x = datetime.datetime.now()
yesterday = x - datetime.timedelta(1)
tomorrow = x + datetime.timedelta(1)

print(yesterday)
print(x)
print(tomorrow)

#3
import datetime
x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d %H:%M:%S"))

#4
import datetime
x = datetime.datetime(2025,2,18,23,19,45,0)
y = datetime.datetime(2025,2,18,23,19,35,0)
difference = x - y
print(difference.total_seconds())