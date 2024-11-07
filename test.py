import json
from datetime import datetime, date, timedelta

formatted_date = datetime.today().date()
day = datetime.today().weekday()
print(formatted_date,day)
NewDate = formatted_date + timedelta(days=6)
print(formatted_date, NewDate)

day = NewDate.weekday()
print(day)

if day == 1 or day ==2:
    print("TuesDay or Wednesday")


formatted_date = '2024-08-16'
days = datetime.strptime(formatted_date, '%Y-%m-%d').date().weekday()
print(days)