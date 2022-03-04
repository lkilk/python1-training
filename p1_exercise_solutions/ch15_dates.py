from datetime import datetime
from datedelta import datedelta

while True:
    start_date = input("Enter the subscription start date (dd/mm/YYYY) or 'today': ")
    if start_date == "today":
        start_date = datetime.today()
    else:
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
    duration = input("Enter the subscription duration, e.g. 15w, 3m, or 2y: ")
    duration_number = int(duration[:-1])
    duration_units = duration[-1]
    if duration_units == "w":
        end_date = start_date + datedelta(days=(duration_number * 7))
    elif duration_units == "m":
        end_date = start_date + datedelta(months=duration_number)
    else:
        end_date = start_date + datedelta(years=duration_number)
    print("Subscription ends:", end_date.strftime("%d/%m/%Y"))
    more = input("More? (y/n): ")
    if more == "n":
        break
