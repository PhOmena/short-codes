from datetime import datetime, timedelta, date
from datetime import date

# data de hoje
today = date.today()
 
 # primeiro dia do mês
data = datetime(today.year, today.month, 1)
dayOfWeek = today.weekday()
day = today.day

if (dayOfWeek == 0 and day in (1, 2, 3)) or (dayOfWeek in (1, 2, 3, 4) and day == 1):
    data = (data - timedelta(days=1)).replace(day=1)

firstDayOfMonth = data.strftime('%d/%m/%Y')
print(firstDayOfMonth)

