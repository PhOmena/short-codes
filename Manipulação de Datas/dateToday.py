from datetime import datetime, timedelta, date
from datetime import date

# data de hoje
today = date.today()
# transforma no formato BRL
formatToday = today.strftime('%d/%m/%Y')
print(formatToday)