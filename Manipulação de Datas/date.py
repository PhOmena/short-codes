from datetime import datetime, timedelta, date
from datetime import date

# Data de hoje
today = date.today()
 
data = datetime(today.year, today.month, 1)
dayOfWeek = today.weekday()
day = today.day

# Primeiro dia do mês
if (dayOfWeek == 0 and day in (1, 2, 3)) or (dayOfWeek in (1, 2, 3, 4) and day == 1):
    data = (data - timedelta(days=1)).replace(day=1)

# Formatando as variáveis

# Primeiro dia do mês
firstDayOfMonth = data.strftime('%d/%m/%Y')
formatToday = today.strftime('%d/%m/%Y')
