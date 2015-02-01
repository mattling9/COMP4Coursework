import datetime, calendar

current_date = datetime.date.today()
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day
if current_day < 8:
    current_month = current_date.month
    last_month = current_month - 1
    next_month = current_month + 1
    no_days_last_month = calendar.monthrange(current_date.year, last_month)[1]
    days_to_minus = 7 - current_day
    previous_month = datetime.date(current_year, last_month, no_days_last_month)
    new_day = previous_month.day - days_to_minus
    new_date = datetime.date(current_year, last_month, new_day)

else:
    new_date = datetime.date(current_year, current_month, (current_day - 7))

print(new_date)
