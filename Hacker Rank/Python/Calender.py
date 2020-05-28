import calendar
import datetime 

print(calendar.TextCalendar(firstweekday=5).formatyear(2015))

def findDay(date): 
    born = datetime.datetime.strptime(date, '%m %d %Y').weekday() 
    return (calendar.day_name[born]) 
 
date = input()
print(findDay(date).upper())

print(dir(datetime.datetime))

