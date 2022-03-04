import datetime as dt

# Create date(time) objects
today = dt.date.today() 
todayTS = dt.datetime.today()

print(f'today: {today} - type(today): {type(today)}')
print(f'todayTS: {todayTS} - type(todayTS): {type(todayTS)}')

nextChristmas = dt.date(2022,12,25)

# Date arithmetic
print(f"\nDays till Christmas: {nextChristmas - today}")

one_week = dt.timedelta(weeks=1)
print(f"Next Week: {today + one_week}")

import datedelta as dd
two_years_one_month = dd.datedelta(years=2,months=1)
print(f"Future date: {today + two_years_one_month}")

# Format a date i.e. present/convert to a formatted string
today_str = today.strftime("%d/%m/%Y")
print("another formatted date:",  today.strftime("%A, %d of %B %Y") )

tomorrow_str = "14-01-2022"
tomorrow = dt.datetime.strptime(tomorrow_str, "%d-%m-%Y")

print(f'tomorrow: {tomorrow} - type(tomorrow): {type(tomorrow)}')

