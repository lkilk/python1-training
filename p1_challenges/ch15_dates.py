from datetime import date,datetime
from datedelta import datedelta

while True:
    start_date = input("Enter subscription start date (dd/mm/yyyy) or (today): ")
    if start_date == 'today':
        start_date = date.today() 
        print(start_date)
    else:
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
    subs_dur = input("Enter the subscription duriation e.g 15w, 3m or 2y: ")
    duration_number = int(subs_dur[:-1])
    print(duration_number)
    duration_units = subs_dur[-1]
    if duration_units == "w":
        end_date = start_date + datedelta(days=duration_number * 7)
    elif duration_units == "m":
        end_date = start_date + datedelta(months=duration_number)
    elif duration_units == "y":
        end_date = start_date + datedelta(years=duration_number)
    print(end_date)
    more = input("continue searching/filtering? (y/n)")
    if more == "n":
        break
