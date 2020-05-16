
#CALENDAR MODULE


import calendar
calendar.setfirstweekday(calendar.MONDAY)
mm,dd,yyyy = map(int,input().split())
weekdays = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
n = calendar.weekday(yyyy,mm,dd)
print(weekdays[n])





