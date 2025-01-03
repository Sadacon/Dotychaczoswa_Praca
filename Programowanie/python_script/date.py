import datetime
christmas_date = datetime.date(year=2024, month=12, day=24)

print(christmas_date)

today = datetime.date.today()
print(today)
print(today.year, today.month, today.day)

today = today.replace(day=14)

diff = christmas_date - today
print(f'Do swiat pozostalo {diff.days} dni')